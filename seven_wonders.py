inp = input()
t, c, g = 0, 0, 0
for letter in inp:
    if letter == 'T':
        t += 1
    elif letter == 'C':
        c += 1
    elif letter == 'G':
        g += 1
print(t ** 2 + c ** 2 + g ** 2 + 7 * min([t, c, g]))