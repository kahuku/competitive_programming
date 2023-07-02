n = int(input())
while n != 0:
    names = []
    for _ in range(n):
        names.append(input())
    names.sort(key=lambda x: x[:2])
    for name in names:
        print(name)
    n = int(input())
    if n != 0:
        print()