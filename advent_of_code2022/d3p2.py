import string
import sys
priorities = [0] + list(string.ascii_lowercase) + list(string.ascii_uppercase)

with open("advent_of_code2022/d3p1input.txt") as file:
    one, two, three = file.readline().strip(), file.readline().strip(), file.readline().strip()
    sum = 0

    while True:
        set1, set2, set3 = set(), set(), set()
        for item in one:
            set1.add(item)
        for item in two:
            set2.add(item)
        for item in three:
            set3.add(item)

        try:
            shared = list(set1.intersection(set2).intersection(set3))[0]
            # print(shared)
            priority = priorities.index(shared)
            sum += priority
        except Exception as e:
            print(sum)
            sys.exit(0)

        one, two, three = file.readline().strip(), file.readline().strip(), file.readline().strip()