v = 7
for _ in range(int(input())):
    if input() == 'Skru op!':
        v += 1 if v < 10 else 0
    else:
        v -= 1 if v > 0 else 0
print(v)