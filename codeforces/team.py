problems = int(input())
solves = 0
for problem in range(problems):
    sures = [int(i) for i in input().split()].count(1)
    if sures >= 2:
        solves += 1
print(solves)