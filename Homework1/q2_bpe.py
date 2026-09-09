from collections import Counter

# Toy corpus given in the assignment
text = """
low low low low low lowest lowest
newer newer newer newer newer newer
wider wider wider new new
"""

# Count how many times each word occurs
word_freq = Counter(text.split())

# Split each word into characters and add "_" as end-of-word marker
corpus = {}

for word, freq in word_freq.items():
    tokens = tuple(list(word) + ["_"])
    corpus[tokens] = freq


# Count all adjacent token pairs in the corpus
def get_pair_counts(corpus):
    pair_counts = Counter()

    for tokens, freq in corpus.items():
        for i in range(len(tokens) - 1):
            pair = (tokens[i], tokens[i + 1])
            pair_counts[pair] += freq

    return pair_counts


# Merge a selected pair everywhere in the corpus
def merge_pair(corpus, pair):
    new_corpus = {}

    for tokens, freq in corpus.items():
        new_tokens = []
        i = 0

        while i < len(tokens):

            if (
                i < len(tokens) - 1
                and tokens[i] == pair[0]
                and tokens[i + 1] == pair[1]
            ):
                new_token = tokens[i] + tokens[i + 1]
                new_tokens.append(new_token)
                i += 2

            else:
                new_tokens.append(tokens[i])
                i += 1

        new_corpus[tuple(new_tokens)] = freq

    return new_corpus


# Create the initial vocabulary
vocabulary = set()

for tokens in corpus:
    vocabulary.update(tokens)

print("Initial Vocabulary:", sorted(vocabulary))
print("Initial Vocabulary Size:", len(vocabulary))
print()


# Learn BPE merges
number_of_merges = 10
merges = []

for step in range(number_of_merges):

    pair_counts = get_pair_counts(corpus)

    if not pair_counts:
        break

    # Select the most frequent adjacent pair
    best_pair, count = pair_counts.most_common(1)[0]

    # Save the merge
    merges.append(best_pair)

    # Merge the pair in the corpus
    corpus = merge_pair(corpus, best_pair)

    # Add the new merged token to the vocabulary
    new_token = best_pair[0] + best_pair[1]
    vocabulary.add(new_token)

    print("Step", step + 1)
    print("Top Pair:", best_pair)
    print("Frequency:", count)
    print("New Token:", new_token)
    print("Vocabulary Size:", len(vocabulary))
    print()


# Display all learned merges
print("Learned Merges")
print("--------------")

for i, pair in enumerate(merges, 1):
    print(i, pair)

print()


# Segment a word using the learned BPE merges
def segment_word(word, merges):

    # Start with individual characters
    tokens = list(word) + ["_"]

    # Apply each learned merge in order
    for pair in merges:
        new_tokens = []
        i = 0

        while i < len(tokens):

            if (
                i < len(tokens) - 1
                and tokens[i] == pair[0]
                and tokens[i + 1] == pair[1]
            ):
                new_token = tokens[i] + tokens[i + 1]
                new_tokens.append(new_token)
                i += 2

            else:
                new_tokens.append(tokens[i])
                i += 1

        tokens = new_tokens

    return tokens


# Words required for Q2.2
test_words = [
    "new",
    "newer",
    "lowest",
    "widest",
    "newestest"
]

print("Word Segmentation")
print("-----------------")

for word in test_words:
    tokens = segment_word(word, merges)
    print(word, "->", " | ".join(tokens))