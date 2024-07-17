# 1800A

# does not work

order = ['m', 'e', 'o', 'w']

for _ in range(int(input())):
    input()
    index = 0
    meow = input()
    good = True
    for c in meow:
        c = c.lower()
        if index < 3:
            if c == order[index]:
                continue
            elif c == order[index + 1]:
                index += 1
            else:
                good = False
                break
        else:
            if c != 'w':
                good = False
    if index != 3:
        good = False
    print("YES" if good else "NO")