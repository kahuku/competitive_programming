inp = int(input())

flag = False
while not flag:
    s = 0
    for i in str(inp):
        s += int(i)
    if (int(inp) % s) == 0:
        print(inp)
        flag = True
    inp += 1
