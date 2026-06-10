from utils.helpers import get_embedding_model


# Encoder des textes en vecteurs numériques pour la similarité
def create_embeddings(texts):
    model = get_embedding_model()
    return model.encode(texts, convert_to_numpy=True)
