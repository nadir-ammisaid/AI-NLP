import re


# Extraire titre, auteur et autres métadonnées du texte project gutenberg
def extract_metadata(text):
    metadata = {"title": None, "author": None, "language": None, "release_date": None}

    # Parser les champs via regex
    title_match = re.search(r"Title:\s*(.+)", text)
    author_match = re.search(r"Author:\s*(.+)", text)
    language_match = re.search(r"Language:\s*(.+)", text)
    release_match = re.search(r"Release date:\s*(.+?)\s*\[", text)

    if title_match:
        metadata["title"] = title_match.group(1).strip()
    if author_match:
        metadata["author"] = author_match.group(1).strip()
    if language_match:
        metadata["language"] = language_match.group(1).strip()
    if release_match:
        metadata["release_date"] = release_match.group(1).strip()

    return metadata
