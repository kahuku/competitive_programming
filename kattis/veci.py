import itertools
s = input()
a = sorted(list(itertools.permutations([*s], len(s))), key=lambda x: int(''.join(x)))
for num in a:
    if int(''.join(num)) > int(s):
        print(int(''.join(num)))
        exit(0)
print(0)