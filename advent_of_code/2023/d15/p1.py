from sys import stdin

def hash(s):
    curr_val = 0
    for i in range(len(s)):
        curr_val += ord(s[i])
        curr_val *= 17
        curr_val %= 256
    return curr_val

line = stdin.readline().strip()
codes = line.split(',')
s = 0
for i in range(len(codes)):
    s += hash(codes[i])
print(s)