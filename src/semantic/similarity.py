from sklearn.metrics.pairwise import cosine_similarity

from semantic.embeddings import create_embeddings


def find_most_similar(query, texts, top_k=5):

    query_embedding = create_embeddings([query])

    text_embeddings = create_embeddings(texts)

    similarities = cosine_similarity(query_embedding, text_embeddings)[0]

    ranked = sorted(zip(texts, similarities), key=lambda x: x[1], reverse=True)

    return ranked[:top_k]
