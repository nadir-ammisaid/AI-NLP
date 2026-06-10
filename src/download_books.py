import sys

from gutenberg.download import download_book

# Télécharger les livres depuis Project Gutenberg
if len(sys.argv) < 2:
    print("Usage: python src/download_books.py " "<book_id> [book_id...]")
    sys.exit(1)

# Traiter chaque ID passé en ligne de commande
for book_id in sys.argv[1:]:
    try:
        path = download_book(int(book_id))
        print(f"Downloaded -> {path}")
    except Exception as error:
        print(f"Failed {book_id}: {error}")
