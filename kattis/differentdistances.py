n = input()
while n != '0':
    n = list(map(float, n.split()))
    n, p = n[:-1], n[-1]
    print((abs(n[0] - n[2])**p + abs(n[1] - n[3])**p)**(1/p))
    n = input()