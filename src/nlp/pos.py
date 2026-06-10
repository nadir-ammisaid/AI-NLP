from nltk.tag import pos_tag


# Utiliser les étiquettes de Penn Treebank (POS tagging: NN, VB, JJ...)
def tag_tokens(tokens):
    return pos_tag(tokens)
