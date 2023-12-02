with open("advent_of_code2022/d1p1input.txt") as file:
    sum = 0
    max = 0
    line = file.readline()
    while line != '':
        if line == '\n':
            if sum > max:
                max = sum
            sum = 0
        else:
            sum += int(line)

        line = file.readline()

print(max)