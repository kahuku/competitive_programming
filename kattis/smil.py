import re
s = input()
x = []
for smile in [":)", ";)", ":-)", ";-)"]:
    x.extend([m.start() for m in re.finditer(re.escape(smile), s)])
# x = [m.start() for smile in smiles for m in re.findall(re.escape(smile), s)]
for i in sorted(x):
    print(i)