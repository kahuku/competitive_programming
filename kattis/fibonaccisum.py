fib = [1, 1]
n = int(input())
for i in range(2, 1000):
    fib.append(fib[i-1] + fib[i-2])
    if fib[i] >= n:
        break

out = []
for i in range(len(fib) - 1, -1, -1):
    if n >= fib[i]:
        out.append(fib[i])
        n -= fib[i]

print(' '.join(map(str, sorted(out))))