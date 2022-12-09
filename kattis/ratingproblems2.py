judges, voted = [int(i) for i in input().split()]
s, n = 0, judges - voted
for _ in range(voted):
    s += int(input())
print(((s - 3 * n) / judges), ((s + 3 * n) / judges))