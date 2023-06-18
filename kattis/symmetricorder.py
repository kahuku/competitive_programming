n = int(input())
j = 1
while n != 0:
    names = []
    for i in range(n):
        names.append(input())
    print("SET", j)
    for i in range(0, n, 2):
        print(names[i])
    if n % 2 == 1:
        n -= 1
    for i in range(n-1, 0, -2):
        print(names[i])
    n = int(input())
    j += 1