from sys import stdin
s = set()
for line in stdin.readlines():
    for word in line.split():
        if word.lower() in s:
            print('.', end=' ')
        else:
            print(word, end=' ')
            s.add(word.lower())
    print()