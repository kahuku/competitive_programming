inp = input()
x = inp.split('-')
y = []
for name in x:
    y.append(name[0])
out = ''
for letter in y:
    out = out + letter
print(out)
