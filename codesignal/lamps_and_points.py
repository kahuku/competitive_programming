# Visa 2024 summer intern application

# given a list of ranges of a line a lamp covers, find out how many lamps cover each control point

# TLE
def solve(lamps, points):
    line = [0] * ((10 ** 5) + 1)
    for lamp in lamps:
        for i in range(lamp[0], lamp[1] + 1):
            line[i] += 1
    return [line[point] for point in points]

# Faster solution (did not get)
def solve(lamps, points):
    line = [0] * ((10 ** 5) + 1)
    for lamp in lamps:
        line[lamp[0]] += 1
        line[lamp[1] + 1] -= 1
    for i in range(1, len(line)):
        line[i] += line[i - 1]
    return [line[point] for point in points]