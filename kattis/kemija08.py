inp = input()
i = 0
s = ''
while i < len(inp):
    s += inp[i]
    if inp[i] in "aeiou":
        i += 3
    else:
        i += 1
print(s)