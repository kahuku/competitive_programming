prev = 1
for _ in range(int(input())):
    a, op, b = input().split()
    if op == '+':
        res = int(a) + int(b) - prev
    elif op == '-':
        res = (int(a) - int(b)) * prev
    elif op == '*':
        res = (int(a) * int(b)) ** 2
    else:
        a = int(a)
        if a % 2 == 0:
            res = a // 2
        else:
            res = (a + 1) // 2
    print(res)
    prev = res