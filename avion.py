l = []
for i in range(5):
    inp = input()
    if "FBI" in inp:
        l.append(i + 1)
s = ''
for num in l:
    if num != l[len(l) - 1]:
        s += str(num) + ' '
    else:
        s += str(num)
if s != '':
    print(s)
else:
    print("HE GOT AWAY!")
