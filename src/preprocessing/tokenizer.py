from nltk.tokenize import word_tokenize


# Diviser le texte en tokens alphabétiques
def tokenize(text):
    tokens = word_tokenize(text)
    return [token for token in tokens if token.isalpha()]
