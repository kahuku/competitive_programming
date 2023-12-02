from sys import stdin

s = 0
nums = list(map(str, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
for line in stdin.readlines():
    line = [c for c in line if c in nums]
    s += int(''.join([line[0], line[-1]]))
print(s)