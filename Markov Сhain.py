import networkx as nx
from collections import defaultdict

def get_transition_weight(word):
    if word not in G.nodes:
        print(f"No such word or no transitions found for word: {word}")
        return
    successors = list(G[word])
    if not successors:
        print(f"No successors found for word: {word}")
        return
    for succ in successors:
        weight = G[word][succ]['weight']
        print(f"Transition from '{word}' to '{succ}' has weight: {weight:.2f}")


sentence = "one fish two fish red fish blue fish"
words = sentence.split()
G = nx.DiGraph()
transitions = defaultdict(int)
word_counts = defaultdict(int)

for i in range(len(words) - 1):
    transitions[(words[i], words[i + 1])] += 1
    word_counts[words[i]] += 1

for (word1, word2), count in transitions.items():
    weight = count / word_counts[word1]
    G.add_edge(word1, word2, weight=weight)

word = input("Enter a word: ").strip()
get_transition_weight(word)