for _ in range(int(input())):
    a, b, c = map(int, input().split())
    d = b ** 2 - 4 * a * c
    print("YES" if d >= 0 and round(d ** 0.5) == d ** 0.5 else "NO")
    # print(['NO', 'YES'][d >= 0 and round(d ** 0.5) == d ** 0.5])