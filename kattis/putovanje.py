n, c = map(int, input().split())
fruits = list(map(int, input().split()))
max_fruits = 0
for i in range(n):
    eaten = 0
    eaten_fruits = 0
    for j in range(i, n):
        if eaten + fruits[j] <= c:
            eaten += fruits[j]
            eaten_fruits += 1
    max_fruits = max(max_fruits, eaten_fruits)
print(max_fruits)