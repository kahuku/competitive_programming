from sys import stdin
for line in stdin.readlines():
    zeros = 0
    ones = 0
    for char in line.strip():
        c_ord = ord(char)
        zeros += 7 - bin(c_ord).count('1')
        ones += bin(c_ord).count('1')
    print('free' if zeros % 2 == 0 and ones % 2 == 0 else 'trapped')