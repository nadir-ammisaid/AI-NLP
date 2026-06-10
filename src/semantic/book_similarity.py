from pathlib import Path

from sklearn.metrics.pairwise import cosine_similarity

from semantic.embeddings import create_embeddings
from gutenberg.metadata import extract_metadata
from preprocessing.cleaner import clean_text

# Les livres analysés dans le projet
SUBJECT_BOOKS = {
    11,
    12,
    16,
    55,
    113,
    120,
    236,
    108,
    834,
    863,
    1661,
    61262,
    69087,
    70114,
    35,
    36,
    84,
    159,
    164,
    345,
    68283,
}


# Trouver les livres les plus similaires à un livre donné
def find_similar_books(
    target_book_id,
    books_directory="data/downloads",
    top_k=5,
):
    # Charger et préparer tous les livres
    books = []
    texts = []

    for file in Path(books_directory).glob("*.txt"):
        book_id = int(file.stem)
        if book_id not in SUBJECT_BOOKS:
            continue

        text = file.read_text(encoding="utf-8")
        metadata = extract_metadata(text)
        cleaned = clean_text(text)

        books.append((book_id, metadata["title"]))
        texts.append(cleaned)

    # Encoder les textes en vecteurs
    embeddings = create_embeddings(texts)

    # Trouver l'index du livre cible
    target_index = next(
        i for i, (book_id, _) in enumerate(books) if book_id == target_book_id
    )

    # Calculer les similarités cosinus
    similarities = cosine_similarity([embeddings[target_index]], embeddings)[0]

    # Classer par similarité décroissante
    ranked = sorted(zip(books, similarities), key=lambda x: x[1], reverse=True)

    # Retourner les top_k (sans le livre lui-même)
    result = []
    for (book_id, title), score in ranked:
        if book_id != target_book_id:
            result.append(title)
        if len(result) == top_k:
            break

    return result
