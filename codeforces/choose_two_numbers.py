def func(a, b):
    for num1 in a:
        for num2 in b:
            if num1 + num2 not in a and num1 + num2 not in b:
                return num1, num2
    return -1

_, a, _, b = input(), [int(i) for i in input().split()], input(), [int(i) for i in input().split()]
a.sort(reverse=True);b.sort(reverse=True)
result = func(a, b)
print(result[0], result[1])
