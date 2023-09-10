positive = list(range(1, 10_001))
odd = list(range(1, 20_001, 2))
even = list(range(2, 20_001, 2))
for i in range(int(input())):
    n = int(input().split()[1])
    print(i + 1, sum(positive[:n]), sum(odd[:n]), sum(even[:n]))