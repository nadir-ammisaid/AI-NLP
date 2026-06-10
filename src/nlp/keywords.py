from collections import Counter


# Extraire les noms (mots clés pertinents)
def extract_nouns(tagged_tokens):
    allowed_tags = ("NN", "NNS", "NNP", "NNPS")
    return [word.lower() for word, tag in tagged_tokens if tag.startswith(allowed_tags)]


# Retourner les noms les plus fréquents
def extract_keywords(tagged_tokens, top_n=20):
    nouns = extract_nouns(tagged_tokens)
    counts = Counter(nouns)
    return counts.most_common(top_n)
