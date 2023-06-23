from sys import stdin
lines = stdin.readlines()
words = set()
for line in lines:
    words.update(line.split())
words = sorted(list(words))
compound_words = set()
for i in range(len(words)):
    for j in range(len(words)):
        if i != j:
            compound_words.add(words[i] + words[j])
print("\n".join(sorted(list(compound_words))))