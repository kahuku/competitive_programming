from sys import stdin
lines = stdin.readlines()
lines = [line.strip() for line in lines]
n = max(len(line) for line in lines)
print(sum((n - len(line)) ** 2 for line in lines[:-1]))