from sys import stdin
for i, line in enumerate(stdin.readlines()):
    x = list(map(int, line.split()))[1:]
    print(f"Case {i + 1}: {min(x)} {max(x)} {max(x) - min(x)}")