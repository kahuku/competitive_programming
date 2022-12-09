n = int(input())
score = 0
for _ in range(n):
    a, b = [float(num) for num in input().split()]
    score += a * b
print(score)