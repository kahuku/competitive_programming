houses = [int(input()) for _ in range(int(input()))]
m = float('inf')
for i in range(len(houses) + 2):
    m = min(m, houses[i % len(houses)] + houses[(i - 2) % len(houses)])
print(m)