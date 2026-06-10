from config import (
    SUMMARY_TOP_K,
    ENTITY_TEXT_LIMIT,
    TOPIC_WORDS,
)

from pathlib import Path

from preprocessing.cleaner import clean_text
from preprocessing.tokenizer import tokenize
from preprocessing.stopwords import remove_stopwords
from preprocessing.lemmatizer import lemmatize_tokens

from nlp.pos import tag_tokens
from nlp.keywords import extract_keywords, extract_nouns
from nlp.entities import extract_entities

from lexdiv.metrics import lexical_metrics

from semantic.summarizer import generate_summary
from semantic.book_similarity import find_similar_books

from gutenberg.metadata import extract_metadata

from topics.lda import extract_topics
from topics.chapters import split_into_chapters
from topics.sections import split_into_sections

from bookcard.builder import build_book_card
from bookcard.exporter import export_book_card


# Pipeline complet : chargement, nettoyage, analyses NLP et génération de carte
def process_book(book_id):

    # Charger le fichier du livre
    book_file = Path(f"data/downloads/{book_id}.txt")

    if not book_file.exists():
        raise FileNotFoundError(f"Book {book_id} not found")

    raw_text = book_file.read_text(encoding="utf-8")

    # Extraire les métadonnées
    metadata = extract_metadata(raw_text)

    # Prétraitement textuel
    cleaned_text = clean_text(raw_text)

    paragraphs = [p.strip() for p in cleaned_text.split("\n\n") if len(p.strip()) > 100]

    # Découpage en chapitres ou sections
    chapters = split_into_chapters(cleaned_text)

    if len(chapters) < 2:
        sections = split_into_sections(
            paragraphs,
            section_count=3,
        )
    else:
        sections = chapters

    # Tokenisation et nettoyage
    tokens = tokenize(cleaned_text)

    tokens = remove_stopwords(tokens)

    tagged_tokens = tag_tokens(tokens)

    tokens = lemmatize_tokens(tagged_tokens)

    # Extraction des topics
    topics = {}

    for index, chapter in enumerate(
        sections,
        start=1,
    ):

        section_documents = []

        chapter_paragraphs = [
            p.strip() for p in chapter.split("\n\n") if len(p.strip()) > 100
        ]

        for paragraph in chapter_paragraphs:

            paragraph_tokens = tokenize(paragraph)

            paragraph_tokens = remove_stopwords(paragraph_tokens)

            paragraph_tagged = tag_tokens(paragraph_tokens)

            doc_tokens = extract_nouns(paragraph_tagged)

            if len(doc_tokens) > 5:
                section_documents.append(doc_tokens)

        section_topics = extract_topics(
            section_documents,
            num_topics=1,
            words_per_topic=TOPIC_WORDS,
        )

        topics[str(index)] = section_topics[0] if section_topics else []

    # Analyses NLP et sémantiques
    metrics = lexical_metrics(tokens)

    keywords = extract_keywords(tagged_tokens)

    entities = extract_entities(cleaned_text[:ENTITY_TEXT_LIMIT])

    summary = generate_summary(
        paragraphs,
        top_k=SUMMARY_TOP_K,
    )

    similar_books = find_similar_books(book_id)

    # Construire la carte du livre
    card = build_book_card(
        book_id,
        metadata,
        metrics,
        keywords,
        entities,
        summary,
        topics,
        similar_books,
    )

    # Export JSON
    output = export_book_card(
        book_id,
        card,
    )

    return {
        "card": card,
        "output": str(output),
        "statistics": metrics,
        "characters": entities["characters"],
        "places": entities["places"],
        "topics": topics,
        "summary": summary,
        "similar_books": similar_books,
    }
