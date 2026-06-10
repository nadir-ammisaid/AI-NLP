# Mots courants à exclure pour ne pas les considérer comme des personnages
COMMON_WORDS = {
    "said",
    "well",
    "yes",
    "no",
    "chapter",
    "sir",
    "miss",
    "mrs",
    "mr",
    "lady",
    "lord",
    "thing",
    "time",
    "way",
    "day",
    "man",
    "woman",
    "boy",
    "girl",
    "wolf",
    "pack",
    "law",
    "panther",
    "thou",
}

# Titres nobiliaires
TITLES = {
    "Majesty",
    "Highness",
    "Sir",
    "Lady",
    "Lord",
}

INVALID_CHARACTERS = {}

# Exemples de lieux extraits à tort comme entités
INVALID_LOCATIONS = {
    "Dinah",
    "Akela",
    "Tabaqui",
}


def is_common_word(entity):
    return entity.lower() in COMMON_WORDS


def is_title(entity):
    return entity in TITLES


def is_valid_character(entity):
    return entity not in INVALID_CHARACTERS


def is_valid_location(entity):
    return entity not in INVALID_LOCATIONS
