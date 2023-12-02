import re

with open("advent_of_code2022/d4p1input.txt") as file:
    line = file.readline()
    count = 0
    while line != '':
        a, b, c, d = re.split(r',|-', line)
        a, b, c, d = int(a), int(b), int(c), int(d)
        
        if a <= c and b >= d or c <= a and d >= b:
            count += 1

        line = file.readline()

print(count)