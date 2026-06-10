from nltk.corpus import stopwords

english_stopwords = set(stopwords.words("english"))


# Enlever les mots vides (articles, prépositions comme "the", "and", "is"...)
def remove_stopwords(tokens):
    return [token for token in tokens if token.lower() not in english_stopwords]
