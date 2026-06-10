from sentence_transformers.util import cos_sim

from utils.helpers import get_embedding_model


# Extraction de la partie la plus informative d'un livre en sélectionnant les paragraphes les plus proches du centre de gravité des embeddings
def generate_summary(paragraphs, top_k=5):
    model = get_embedding_model()

    # Encoder tous les paragraphes
    embeddings = model.encode(paragraphs, convert_to_tensor=True)

    # Trouver le centre de gravité des embeddings
    centroid = embeddings.mean(dim=0)

    # Calculer la similarité de chaque paragraphe au centroid
    scores = cos_sim(centroid, embeddings)[0]

    # Sélectionner les top_k paragraphes
    ranked = sorted(zip(paragraphs, scores), key=lambda x: float(x[1]), reverse=True)

    summary = " ".join(
        paragraph.replace("\n", " ") for paragraph, score in ranked[:top_k]
    )

    return summary
