import re

with open("advent_of_code2022/d4p1input.txt") as file:
    line = file.readline()
    count = 0
    while line != '':
        a, b, c, d = re.split(r',|-', line)
        a, b, c, d = int(a), int(b), int(c), int(d)
        
        x, y = set(range(a, b + 1)), set(range(c, d + 1))
        if len(x.intersection(y)):
            count += 1

        line = file.readline()

print(count)