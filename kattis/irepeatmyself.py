for _ in range(int(input())):
    s = input()
    n = len(s)
    found = False
    for i in range(1, n):
        if s[:i] * (n // i) + s[:(n % i)] == s:
            print(i)
            found = True
            break
    if not found:
        print(n)