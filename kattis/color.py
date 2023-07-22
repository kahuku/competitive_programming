s, c, k = map(int, input().split())
l = sorted(list(map(int, input().split())))
machines = 1
in_machine = 1
lowest = l[0]
for i in range(1, len(l)):
    if l[i] - lowest > k or in_machine == c:
        machines += 1
        in_machine = 1
        lowest = l[i]
    else:
        in_machine += 1
print(machines)