a, b = input().split()
a_i, b_i = None, None
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            a_i, b_i = i, j
            break
    if a_i is not None:
        break
for i in range(len(b)):
    if i == b_i:
        print(a)
    else:
        print('.' * a_i + b[i] + '.' * (len(a) - a_i - 1))