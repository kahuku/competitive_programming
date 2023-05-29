a, b = input(), input()
c = 0
for la, lb in zip(a, b):
    if la != lb: c += 1
print(2 ** c)

# simplified 
a, b = input(), input()
c = sum(1 for la, lb in zip(a, b) if la != lb)
print(2 ** c)