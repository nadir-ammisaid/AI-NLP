from gutenberg.bookshelves import BOOKSHELVES


# Assembler toutes les analyses en une carte du livre
def build_book_card(
    book_id,
    metadata,
    metrics,
    keywords,
    entities,
    summary,
    topics,
    similar_books,
):
    return {
        "info": {
            "id": str(book_id),
            "authors": metadata["author"],
            "bookshelves": BOOKSHELVES.get(str(book_id)),
        },
        "lexdiv": metrics,
        "topics": topics,
        "entities": {
            "characters": entities["characters"],
            "locations": entities["places"],
        },
        "summary": summary,
        "similar": similar_books,
    }
