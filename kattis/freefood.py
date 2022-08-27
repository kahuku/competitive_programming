n = int(input())

days = []
for i in range(n):
    inp = [int(i) for i in input().split()]
    startDate = inp[0]
    endDate = inp[1]
    diff = endDate - startDate
    days.append(startDate)
    for j in range(diff + 1):
        days.append(startDate + j)
days.sort()
days = list(set(days))
print(len(days))
