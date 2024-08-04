s = set(['keys', 'phone', 'wallet'])
for _ in range(int(input())):
    x = input()
    if x in s:
        s.remove(x)
if len(s) == 0:
    print("ready")
else:
    print('\n'.join(sorted(list(s))))