from sys import stdin
for line in stdin.readlines():
    n = int(line.strip())
    print(2 * n - 2 if n > 1 else 1)