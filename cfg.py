import nltk
import sys

TERMINALS = """
skr -> "sakura"
vb -> "search" | "open" | "check" | "send" | "launch" | "start" | "add" | "change"
app -> "spotify" | "discord" | "code" | "application" | "genshin" 
web -> "wikipedia" | "youtube" | "google"
msg -> "email"
upd -> "time" | "username" | "app" | "contact"
prp -> "to"
N -> "kyle" | "matthew" | "ian" 
"""

NONTERMINALS = """
S -> skr NP
NP -> vb app | vb web | vb msg PP | vb upd
PP -> prp N
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)



def cfg_checker(query):

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = query

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks

    for tree in trees:
        # tree.pretty_print()

        for np in np_chunk(tree):
            str = " ".join(np.flatten())
            return str


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    sentence = sentence.lower()
    tokens = nltk.word_tokenize(sentence)
    tokens = filter(lambda string: any(c.isalpha() for c in string), tokens)
    return tokens


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    chunks_list = []

    for subtree in tree.subtrees():
        if subtree.label() == 'NP' and not any(s.label() == 'NP' for s in subtree.subtrees(lambda t: t != subtree)):
            chunks_list.append(subtree)

    return chunks_list


# if __name__ == "__main__":
#     cfg_checker()