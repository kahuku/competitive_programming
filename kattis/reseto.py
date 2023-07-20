n, k = map(int, input().split())
sieve = [True] * (n + 1)
crosses = 0
sieve[0] = sieve[1] = False
for i in range(2, n + 1):
    if sieve[i]:
        for j in range(i, n + 1, i):
            if not sieve[j]:
                continue
            sieve[j] = False
            crosses += 1
            if crosses == k:
                print(j)
                exit(0)