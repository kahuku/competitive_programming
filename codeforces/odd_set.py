# 1542A

for _ in range(int(input())):
    input()
    l = list(map(int, input().split()))
    l2 = [i % 2 for i in l]
    print("Yes" if l2.count(0) == l2.count(1) else "No")