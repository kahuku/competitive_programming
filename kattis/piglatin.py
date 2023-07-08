from sys import stdin

def v_index(word):
    for i in range(len(word)):
        if word[i] in 'aeiouy':
            return i
    return len(word)

def piglatin(word):
    if word[0] in 'aeiouy':
        return word + 'yay'
    else:
        i = v_index(word)
        return word[i:] + word[:i] + 'ay'

lines = stdin.readlines()
for line in lines:
    words = line.split()
    for word in words:
        print(piglatin(word), end=' ')
    print()
