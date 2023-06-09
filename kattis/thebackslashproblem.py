from sys import stdin
lines = stdin.readlines()
for i in range(0, len(lines), 2):
    rounds = int(lines[i])
    s = lines[i + 1].strip()
    out = ''
    slashes = 2 ** rounds - 1
    for c in s:
        if ord('!') <= ord(c) <= ord('*') or ord('[') <= ord(c) <= ord(']'):
            out += slashes * '\\'
        out += c
    print(out)