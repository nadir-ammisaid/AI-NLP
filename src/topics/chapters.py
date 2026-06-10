import re


# Diviser le texte en chapitres en cherchant des patterns spécifiques
def split_into_chapters(text):
    # Essayer différents patterns de chapitres
    patterns = [
        r"\n\s*CHAPTER\s+[IVXLCDM]+\.",
        r"\n\s*Chapter\s+\d+",
        r"\n\s*[IVXLCDM]+\.\s+[A-Z]",
    ]

    for pattern in patterns:
        chapters = re.split(
            pattern,
            text,
            flags=re.IGNORECASE,
        )

        # Filtrer les chapitres trop courts
        chapters = [
            chapter.strip() for chapter in chapters if len(chapter.strip()) > 1000
        ]

        # Accepter si au moins 5 chapitres trouvés
        if len(chapters) >= 5:
            return chapters

    return []
