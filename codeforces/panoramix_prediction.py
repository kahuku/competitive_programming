def prime(x):
    if x > 1:
        for i in range(2, x // 2 + 1):
            if x % i == 0:
                return False
        return True
    return False

n, m = [int(i) for i in input().split()]
for num in range(n + 1, m + 1):
    if num != m:
        if prime(num):
            s = "NO"
            break
    else:
        s = "YES" if prime(num) else "NO"
print(s)