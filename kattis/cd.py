import sys

input = sys.stdin.read  # Use read to gather all input at once
data = input().splitlines()

i = 0
while i < len(data):
    n, m = map(int, data[i].split())
    if n == 0 and m == 0:
        break

    jack = [int(x) for x in data[i + 1: i + 1 + n]]
    jill = [int(x) for x in data[i + 1 + n: i + 1 + n + m]]

    count = 0
    j, k = 0, 0
    while j < n and k < m:
        if jack[j] == jill[k]:
            count += 1
            j += 1
            k += 1
        elif jack[j] < jill[k]:
            j += 1
        else:
            k += 1
    print(count)
    
    i += 1 + n + m