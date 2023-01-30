n = int(input())
for i in range(n):
    a, b = input(), input()
    x = []
    for c_a, c_b in zip(a, b):
        if c_a == c_b:
            x.append('.')
        else:
            x.append("*")
    print(a + "\n" + b + "\n" + ''.join(x) + "\n")