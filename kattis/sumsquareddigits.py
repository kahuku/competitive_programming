for i in range(int(input())):
    a, b, n = map(int, input().split())
    ans = 0
    while n > 0:
        ans += (n % b) ** 2
        n //= b
    print(a, ans)