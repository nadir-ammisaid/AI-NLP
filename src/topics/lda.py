from gensim import corpora
from gensim.models import LdaModel


# Extraction de topics via LDA (Latent Dirichlet Allocation)
def extract_topics(
    documents,
    num_topics=5,
    words_per_topic=5,
):
    # Construire le dictionnaire et convertir en BoW (Bag of Words)
    dictionary = corpora.Dictionary(documents)

    if len(dictionary) == 0:
        return []

    corpus = [dictionary.doc2bow(doc) for doc in documents]

    # Entraîner le modèle LDA
    lda = LdaModel(
        corpus=corpus,
        id2word=dictionary,
        num_topics=num_topics,
        random_state=42,
        passes=20,
    )

    # Extraire les mots-clés pour chaque topic
    topics = []

    for topic_id in range(num_topics):
        words = lda.show_topic(
            topic_id,
            topn=words_per_topic,
        )
        topics.append([word for word, score in words])

    return topics
