# This is so slow it won't finish in time

from sys import stdin

def rl(line):
    return list(map(int, line.strip().split()))

def convert(seed, conv):
    # print("conv", seed, conv)
    for arr in conv:
        if arr[1] <= seed <= arr[1] + arr[2]:
            diff = seed - arr[1]
            return arr[0] + diff
    return seed

def convert_all(seed, convs):
    soil, fert, water, light, temp, humid, loc = convs
    soil = convert(seed, soil)
    fert = convert(soil, fert)
    water = convert(fert, water)
    light = convert(water, light)
    temp = convert(light, temp)
    humid = convert(temp, humid)
    loc = convert(humid, loc)
    return loc

part = 0
seeds = []
seed_to_soil, soil_to_fert, fert_to_water, water_to_light, light_to_temp, temp_to_humid, humid_to_loc = [], [], [], [], [], [], []
for line in stdin.readlines():
    if part == 0:
        line = line.split()[1:]
        seeds = [int(i) for i in line]
        part = 1
    elif part % 2:
        part += 1
    elif part == 2:
        if line == '\n':
            part = 3
        elif line[0].isdigit():
            seed_to_soil.append(rl(line))
    elif part == 4:
        if line == '\n':
            part = 5
        elif line[0].isdigit():
            soil_to_fert.append(rl(line))
    elif part == 6:
        if line == '\n':
            part = 7
        elif line[0].isdigit():
            fert_to_water.append(rl(line))
    elif part == 8:
        if line == '\n':
            part = 9
        elif line[0].isdigit():
            water_to_light.append(rl(line))
    elif part == 10:
        if line == '\n':
            part = 11
        elif line[0].isdigit():
            light_to_temp.append(rl(line))
    elif part == 12:
        if line == '\n':
            part = 13
        elif line[0].isdigit():
            temp_to_humid.append(rl(line))
    elif part == 14:
        if line == '\n':
            part = 15
        elif line[0].isdigit():
            humid_to_loc.append(rl(line))

m = float('inf')

temp = []
for i in range(0, len(seeds), 2):
    for j in range(seeds[i + 1]):
        temp.append(seeds[i] + j)

seeds = temp

for seed in seeds:
    # print("Seed start:", seed)
    seed = convert_all(seed, [seed_to_soil, soil_to_fert, fert_to_water, water_to_light, light_to_temp, temp_to_humid, humid_to_loc])
    # print("Seed end:", seed)
    # print()

    m = min(m, seed)
print(m)