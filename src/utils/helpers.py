from sentence_transformers import SentenceTransformer

_embedding_model = None


# Charger le modèle d'embeddings une seule fois (singleton)
def get_embedding_model():
    global _embedding_model
    if _embedding_model is None:
        _embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
    return _embedding_model
