from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

lemmatizer = WordNetLemmatizer()


# Convertir les tags POS en tags WordNet pour la lemmatisation
def get_wordnet_pos(tag):
    if tag.startswith("J"):
        return wordnet.ADJ
    if tag.startswith("V"):
        return wordnet.VERB
    if tag.startswith("N"):
        return wordnet.NOUN
    if tag.startswith("R"):
        return wordnet.ADV
    return wordnet.NOUN


# Réduire les mots à leur forme canonique
# Par exemple, "running" devient "run", "better" devient "good"
def lemmatize_tokens(tagged_tokens):
    lemmas = []
    for word, tag in tagged_tokens:
        lemma = lemmatizer.lemmatize(word, get_wordnet_pos(tag))
        lemmas.append(lemma)
    return lemmas
