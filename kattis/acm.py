from collections import defaultdict
line = input()
total = 0
count = 0
wrongs = defaultdict(int)
while line != '-1':
    mins, problem, result = line.split()
    mins = int(mins)
    if result == 'wrong':
        wrongs[problem] += 1
    else:
        total += mins
        count += 1
        if wrongs[problem] > 0:
            total += 20 * wrongs[problem]
            wrongs[problem] = 0
    line = input()
print(count, total)