import json
from pathlib import Path


# Exporter la carte du livre en JSON
def export_book_card(book_id, card):
    Path("data/output").mkdir(
        parents=True,
        exist_ok=True,
    )

    output_file = Path("data/output") / f"{book_id}.json"
    output_file.write_text(
        json.dumps(card, indent=4, ensure_ascii=False), encoding="utf-8"
    )

    return output_file
