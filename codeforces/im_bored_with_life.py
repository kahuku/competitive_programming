# 822A
a, b = map(int, input().split())
x = 1
for i in range(1, min(a, b) + 1):
    x *= i
print(x)