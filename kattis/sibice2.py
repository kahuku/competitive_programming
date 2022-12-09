n, x, y = [int(i) for i in input().split()]
for _ in range(n):
    a = int(input())
    if a <= ((x**2 + y**2)**.5):
        print("DA")
    else:
        print("NE")