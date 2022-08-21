_ = input()
inp = [int(i) for i in input().split()]
max, min = inp[0], inp[0]
amazing = 0
for i in inp[1:]:
    if i > max:
        amazing += 1
        max = i
    elif i < min:
        amazing += 1
        min = i
print(amazing)