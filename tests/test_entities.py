from nlp.entities import extract_entities


def test_extract_entities():

    text = """
Alice met Alice.
Alice saw Bob.
Bob met Bob.
Paris is beautiful.
Paris is in France.
Paris is famous.
"""

    entities = extract_entities(text)

    assert "Alice" in entities["characters"]
    assert "Bob" in entities["characters"]
    assert "Paris" in entities["places"]
