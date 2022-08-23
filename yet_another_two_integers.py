cases = int(input())
for case in range(cases):
    a, b = [int(i) for i in input().split()]
    print((abs(a - b) + 9) // 10)