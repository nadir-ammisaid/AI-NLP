from collections import Counter
from math import sqrt, log


# Calculer les métriques de diversité lexicale
def lexical_metrics(tokens):

    # tok = nombre total de tokens
    tok = len(tokens)

    if tok == 0:
        return {}

    # typ = nombre de types uniques (vocabulaire)
    typ = len(set(tokens))

    counts = Counter(tokens)

    hap = sum(1 for count in counts.values() if count == 1)

    ttr = typ / tok

    root_ttr = typ / sqrt(tok)

    corrected_ttr = typ / sqrt(2 * tok)

    herdan = log(typ) / log(tok)

    maas = (log(tok) - log(typ)) / (log(tok) ** 2)

    mwl = sum(len(word) for word in tokens) / tok

    # Fréquence moyenne des mots : total / unique
    mwf = tok / typ

    return {
        "tok": tok,  # tok = nombre total de tokens (mots)
        "typ": typ,  # typ = nombre de types uniques (taille du vocabulaire)
        "hap": hap,  # Hapax legomena - mots apparaissant exactement une fois
        "ttr": round(ttr, 4),  # TTR (Type-Token Ratio) : mots uniques / total
        "root_ttr": round(root_ttr, 4),  # Root TTR normalisé par sqrt(tokens)
        "corrected_ttr": round(
            corrected_ttr, 4
        ),  # TTR corrigé normalisé par sqrt(2*tokens)
        "herdan": round(herdan, 4),  # Mesure de Herdan : log(types) / log(tokens)
        "maas": round(
            maas, 4
        ),  # Mesure de Maas : (log(tokens) - log(types)) / log(tokens)²
        "mwl": round(mwl, 4),  # Longueur moyenne des mots (caractères par token)
        "mwf": round(mwf, 4),  # Fréquence moyenne des mots : total / unique
    }
