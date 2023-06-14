s = input()
out = s[0]
for char in s[1:]:
    if char != out[-1]:
        out += char
print(out)

# solution 2
s = input()
out = ''.join(char for i, char in enumerate(s) if char != s[i-1])
print(out)