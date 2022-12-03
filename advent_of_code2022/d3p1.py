import string
priorities = [0] + list(string.ascii_lowercase) + list(string.ascii_uppercase)

with open("advent_of_code2022/d3p1input.txt") as file:
    sum = 0
    line = file.readline()
    while line != '':
        set1, set2 = set(), set()
        one, two = line[:len(line)//2], line[len(line)//2:]
        for letter in one:
            set1.add(letter)
        for letter in two:
            set2.add(letter)

        shared = list(set1.intersection(set2))[0]
        priority = priorities.index(shared)
        sum += priority

        line = file.readline()

print(sum)