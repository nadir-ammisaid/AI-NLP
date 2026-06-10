from pathlib import Path

import requests


# Télécharger un livre depuis Project Gutenberg par son ID
def download_book(book_id):
    url = f"https://www.gutenberg.org/" f"cache/epub/{book_id}/pg{book_id}.txt"

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    # Sauvegarder dans le dossier data/downloads
    Path("data/downloads").mkdir(
        parents=True,
        exist_ok=True,
    )

    output_file = Path("data/downloads") / f"{book_id}.txt"
    output_file.write_text(response.text, encoding="utf-8")

    return output_file
