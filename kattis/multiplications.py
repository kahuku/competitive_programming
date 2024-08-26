p = 1
for _ in range(int(input())):
    p *= int(input())
print(p % (10 ** 9 + 7))