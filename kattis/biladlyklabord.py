s = input()
x = [s[0]]
for i in range(1, len(s)):
    if s[i] != x[-1]:
        x.append(s[i])
print(''.join(x))