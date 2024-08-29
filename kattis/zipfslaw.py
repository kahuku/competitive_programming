import re
from sys import stdin
input = stdin.readline

def proc(text):
    return re.sub(r'[^a-zA-Z ]', ' ', text).lower().strip().split()

def solve(text, n):
    d = {}
    for line in text:
        for word in line:
            if word not in d:
                d[word] = 0
            d[word] += 1
    d = sorted([k for k, v in d.items() if v == n])
    if len(d) > 0:
        for line in d:
            print(line)
    else:
        print("There is no such word.")

n = int(input())
while n:
    lines = []
    while True:
        line = input().strip()
        if line == 'EndOfText': break
        if not line: continue
        lines.append(proc(line))
    solve(lines, n)
    n = int(input() or 0)
    if n != 0:
        print()