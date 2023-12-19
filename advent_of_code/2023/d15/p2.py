from sys import stdin
from collections import defaultdict

def hash(s):
    curr_val = 0
    for i in range(len(s)):
        curr_val += ord(s[i])
        curr_val *= 17
        curr_val %= 256
    return curr_val

def find(d, box, label):
    if box in d:
        for i in range(len(d[box])):
            if d[box][i][0] == label:
                return i
    return None

def action(d, label, box, focal=None):
    if focal:
        # add lens
        ind = find(d, box, label)
        if ind is not None:
            # already exists
            d[box][ind] = (label, focal)
        else:
            d[box].append((label, focal))
    else:
        # remove lens
        ind = find(d, box, label)
        if ind is not None:
            del d[box][ind]
            if len(d[box]) == 0:
                del d[box]

line = stdin.readline().strip()
codes = line.split(',')
d = defaultdict(list)

for i in range(len(codes)):
    focal = None
    if codes[i].count('-') == 1:
        label = codes[i][:-1]
    else:
        label, focal = codes[i].split('=')
    action(d, label, hash(label), focal)

s = 0
for k, v in d.items():
    for i in range(len(v)):
        num = (int(k) + 1) * (i + 1) * int(v[i][1])
        s += num
print(s)