a, b, c = map(int, input().split())
count = [0] * 101
for _ in range(3):
    start, end = map(int, input().split())
    for i in range(start, end):
        count[i] += 1
total = 0
for i in range(101):
    if count[i] == 1:
        total += a
    elif count[i] == 2:
        total += b * 2
    elif count[i] == 3:
        total += c * 3
print(total)