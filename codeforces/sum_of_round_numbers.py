cases = int(input())
for i in range(cases):
    case = input()[::-1]
    out = []
    for i in range(len(case)):
        digit = case[i]
        if digit != "0":
            out.append(digit + "0" * i)
    print(len(out))
    print(' '.join(out))
