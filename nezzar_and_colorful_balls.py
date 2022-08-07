from collections import Counter
cases = int(input())
for case in range(cases):
    _, balls = input(), [int(i) for i in input().split()]
    print(max(Counter(balls).values()))