# 1977A

for _ in range(int(input())):
    a, b = map(int, input().split())
    if b > a:
        print("No")
    else:
        print("Yes" if (a - b) % 2 == 0 else "No")