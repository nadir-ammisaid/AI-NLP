from gutenberg.metadata import extract_metadata


def test_extract_metadata():

    text = """
Title: My Book
Author: John Doe
Language: English
Release date: January 1, 2020 [eBook]
"""

    metadata = extract_metadata(text)

    assert metadata["title"] == "My Book"
    assert metadata["author"] == "John Doe"
    assert metadata["language"] == "English"
    assert metadata["release_date"] == "January 1, 2020"
