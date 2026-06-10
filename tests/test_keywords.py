from nlp.keywords import extract_keywords


def test_extract_keywords():

    tagged_tokens = [
        ("Alice", "NNP"),
        ("Rabbit", "NNP"),
        ("Rabbit", "NNP"),
        ("run", "VB"),
    ]

    result = extract_keywords(tagged_tokens)

    words = [word for word, count in result]

    assert "alice" in words
    assert "rabbit" in words
