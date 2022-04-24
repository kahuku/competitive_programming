n = int(input())
s = 0
for num in range(n):
    on = input()
    p = int(on[-1])
    b = int(on[:len(on) -1])
    s += (b**p)
print(s)
