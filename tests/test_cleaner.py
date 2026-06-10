from src.preprocessing.cleaner import clean_text


def test_clean_text():

    text = """
    Alice was beginning to get very tired of sitting by her sister on the bank.
    """

    cleaned = clean_text(text)

    assert isinstance(cleaned, str)
    assert len(cleaned) > 0
    assert "alice" in cleaned.lower()
