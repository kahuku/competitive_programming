for i in range(int(input())):
    x, y, n = [int(i) for i in input().split()]
    print(n - ((n - y) % x))