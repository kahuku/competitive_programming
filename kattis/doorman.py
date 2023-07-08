dif = int(input())
m, w = 0, 0
s = list(input())
for i in range(len(s)):
    if s[i] == 'M':
        if abs(m + 1 - w) > dif:
            if i != len(s) - 1 and s[i + 1] == 'W':
                w += 1
                s = list(s)
                s[i + 1] = 'M'
            else:
                break
        else:
            m += 1
    else:
        if abs(m - w - 1) > dif:
            if i != len(s) - 1 and s[i + 1] == 'M':
                m += 1
                s[i + 1] = 'W'
            else:
                break
        else:
            w += 1
print(m + w)