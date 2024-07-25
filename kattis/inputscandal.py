from sys import stdin
inp = [line.strip() for line in stdin.readlines()]
print(len(inp))
print(*inp, sep='\n')