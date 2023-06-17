n = input()
while n != "0":
    n = int(n)
    i = 11
    while sum(map(int, str(n))) != sum(map(int, str(n * i))):
        i += 1
    print(i)
    n = input()