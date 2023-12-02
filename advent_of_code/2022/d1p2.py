with open("advent_of_code2022/d1p1input.txt") as file:
    s = 0
    cals = []
    line = file.readline()
    while line != '':
        if line == '\n':
            cals.append(s)
            s = 0
        else:
            s += int(line)

        line = file.readline()

print(sum(sorted(cals, reverse=True)[0:3]))