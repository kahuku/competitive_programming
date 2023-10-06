from collections import defaultdict
inp = defaultdict(list)
for _ in range(int(input())):
    entry = input().split()
    name, words = entry[0], entry[1:]
    inp[name].extend(words)
all_used = set(list(inp.values())[0])
for v in inp.values():
    new_set = set(v)
    all_used = all_used.intersection(new_set)
d2 = defaultdict(int)
for v in inp.values():
    for word in v:
        if word in all_used:
            d2[word] += 1
for word, count in sorted(d2.items(), key=lambda x: (-x[1], x[0])):
    print(word)
if len(all_used) == 0:
    print("ALL CLEAR")