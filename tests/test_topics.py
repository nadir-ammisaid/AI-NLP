from topics.lda import extract_topics


def test_extract_topics():

    documents = [
        ["alice", "rabbit", "queen"],
        ["alice", "rabbit", "hatter"],
        ["queen", "king", "court"],
    ]

    topics = extract_topics(documents, num_topics=2, words_per_topic=3)

    assert len(topics) == 2
