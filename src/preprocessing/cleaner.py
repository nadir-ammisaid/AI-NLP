import re


# Nettoyer le texte: extraire contenu, fusionner espaces, normaliser
def clean_text(text):
    # Extraire la zone entre le header et footer
    start = text.find("*** START")
    end = text.find("*** END")

    if start != -1:
        start = text.find("\n", start) + 1

    if start != -1 and end != -1:
        text = text[start:end]

    # Normaliser les fins de ligne
    text = text.replace("\r\n", "\n")

    # Cas spécifique pour Alice in Wonderland qui a un header très long
    chapter_start = text.find("CHAPTER I.\nDown the Rabbit-Hole")
    if chapter_start != -1:
        text = text[chapter_start:]

    # Fusionner les sauts de ligne multiples
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Nettoyer les espaces superflus
    text = re.sub(r"[ \t]+", " ", text)

    return text.strip()
