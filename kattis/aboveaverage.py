for _ in range(int(input())):
    l = list(map(int, input().split()))
    n, l = l[0], l[1:]
    avg = sum(l) / n
    c = 0
    for num in l:
        if num > avg: c += 1
    print('{:.3%}'.format(c / n))