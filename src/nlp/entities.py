import spacy
from collections import Counter
from nlp.entity_filters import (
    is_common_word,
    is_valid_character,
    is_valid_location,
    is_title,
)

nlp = spacy.load("en_core_web_sm")


# Vérifier si une entité est valide (pas un mot commun, pas trop courte...)
def is_valid_entity(entity):

    entity = entity.strip()

    if len(entity) < 3:
        return False

    if "\n" in entity:
        return False

    if "CHAPTER" in entity.upper():
        return False

    if entity.isupper():
        return False

    if entity.islower():
        return False

    if is_common_word(entity):
        return False

    if is_title(entity):
        return False

    if not entity.replace(" ", "").isalpha():
        return False

    if len(entity.split()) > 4:
        return False

    if entity.endswith("’s"):
        return False

    if entity.endswith("'s"):
        return False

    return True


# Supprimer les entités imbriquées (ex: "John" dans "John Smith")
def remove_nested_entities(entities):
    entities = sorted(entities, key=len, reverse=True)
    filtered = []

    for entity in entities:
        if not any(entity != other and entity in other for other in filtered):
            filtered.append(entity)

    return filtered


# Extraire les personnages et lieux d'un texte
def extract_entities(text):
    doc = nlp(text)

    # Compter les occurrences de chaque entité
    characters = Counter()
    places = Counter()

    for ent in doc.ents:
        entity = ent.text.strip()
        if not is_valid_entity(entity):
            continue

        if ent.label_ in ("PERSON",):
            characters[entity] += 1
        elif ent.label_ in ("GPE", "LOC"):
            places[entity] += 1

    # Filtrer par fréquence et validité
    characters = [
        entity
        for entity, count in characters.most_common()
        if count >= 3 and is_valid_character(entity)
    ]
    characters = remove_nested_entities(characters)

    places = [
        entity
        for entity, count in places.most_common()
        if count >= 3 and is_valid_location(entity) and entity not in characters
    ]

    return {
        "characters": characters,
        "places": places,
    }
