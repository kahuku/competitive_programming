m, s = input().split()
o = ''
i = 0
if m == 'E':
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        o += s[i] + str(j - i)
        i = j
elif m == 'D':
    while i < len(s):
        o += s[i] * int(s[i + 1])
        i += 2
print(o)