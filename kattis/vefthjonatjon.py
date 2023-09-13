counts = [0, 0, 0]
for _ in range(int(input())):
    a, b, c = input().split()
    if a == 'J':
        counts[0] += 1
    if b == 'J':
        counts[1] += 1
    if c == 'J':
        counts[2] += 1
print(min(counts))