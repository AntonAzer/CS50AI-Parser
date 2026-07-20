import nltk
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "holmes" | "home" | "mess" | "paint" | "palm" | "pipe" | "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat" | "smiled" | "were"
"""

NONTERMINALS = """
S -> NP VP | S Conj S
NP -> N | Det N | AP N | Det AP N | NP PP
VP -> V | Adv VP | VP Adv | V NP | V PP | VP PP | VP Conj VP
AP -> Adj | Adj AP
PP -> P NP
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()
    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

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
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(document):
    """
    Convert document into a list of lowercase words,
    leaving out any words that don't contain at least one alphabetic character.
    """
    words = nltk.word_tokenize(document.lower())
    
    cleaned_words = [word for word in words if any(char.isalpha() for char in word)]
    
    return cleaned_words


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as an NP subtree that does not
    contain any other NP subtrees within it.
    """
    chunks = []
    
    for subtree in tree.subtrees():
        if subtree.label() == "NP":
            if len(list(subtree.subtrees(lambda t: t.label() == "NP"))) == 1:
                chunks.append(subtree)
                
    return chunks

if __name__ == "__main__":
    main()
