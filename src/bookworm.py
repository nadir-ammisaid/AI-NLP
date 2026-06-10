import argparse
import json

from pipeline.processor import process_book


# Gestionnaire d'erreurs personnalisé pour l'affichage
class BookwormArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        print(f"Error: {message}")
        print("Use --help for usage information.")
        raise SystemExit(2)


def main():
    # Parser CLI avec différents modes d'analyse
    parser = BookwormArgumentParser(
        description=(
            "Bookworm NLP engine for Project Gutenberg books\n\n"
            "Examples:\n"
            "  python src/bookworm.py --card 11\n"
            "  python src/bookworm.py --lexdiv 1661\n"
            "  python src/bookworm.py --topics 11\n"
            "  python src/bookworm.py --entities 1661\n"
            "  python src/bookworm.py --summarize 11\n"
            "  python src/bookworm.py --similar 1661"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "--version",
        action="version",
        version="bookworm 1.0",
    )

    # On peut choisir un seul mode d'analyse à la fois
    group = parser.add_mutually_exclusive_group(required=True)

    # Génération de la book card
    group.add_argument(
        "--card",
        type=int,
        help="Generate complete book card for a Gutenberg book ID",
    )

    # Calcul des métriques de diversité lexicale
    group.add_argument(
        "--lexdiv",
        type=int,
        help="Compute lexical diversity metrics for a book ID",
    )

    # Extraction des topics principaux
    group.add_argument(
        "--topics",
        type=int,
        help="Extract main topics from a book ID",
    )

    # Extraction des personnages et lieux
    group.add_argument(
        "--entities",
        type=int,
        help="Extract characters and locations from a book ID",
    )

    # Génération du résumé du livre
    group.add_argument(
        "--summarize",
        type=int,
        help="Generate summary for a book ID",
    )

    # Recherche des livres les plus similaires
    group.add_argument(
        "--similar",
        type=int,
        help="Find 5 similar books from the collection",
    )

    args = parser.parse_args()

    # Récupérer l'ID du livre depuis le mode sélectionné
    book_id = (
        args.card
        or args.lexdiv
        or args.topics
        or args.entities
        or args.summarize
        or args.similar
    )

    # Traiter le livre
    try:
        result = process_book(book_id)
    except FileNotFoundError as error:
        print(error)
        return

    # Afficher le résultat selon le mode demandé
    if args.card:
        print(
            json.dumps(
                result["card"],
                indent=4,
                ensure_ascii=False,
            )
        )
    elif args.lexdiv:
        print(
            json.dumps(
                result["statistics"],
                indent=4,
                ensure_ascii=False,
            )
        )
    elif args.topics:
        print(
            json.dumps(
                result["topics"],
                indent=4,
                ensure_ascii=False,
            )
        )
    elif args.entities:
        print(
            json.dumps(
                {
                    "characters": result["characters"],
                    "locations": result["places"],
                },
                indent=4,
                ensure_ascii=False,
            )
        )
    elif args.summarize:
        print(result["summary"])
    elif args.similar:
        print(
            json.dumps(
                result["similar_books"],
                indent=4,
                ensure_ascii=False,
            )
        )


if __name__ == "__main__":

    main()
