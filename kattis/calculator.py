from sys import stdin
for line in stdin.readlines():
    print('{:.2f}'.format(eval(line)))