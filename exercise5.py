import random

a = []
b = []

for x in range(0,10):
    n = random.randint(0,15)
    a.append(n)

for y in range(0,10):
    n = random.randint(0,15)
    b.append(n)
    
c = []

for elem in a:
    if (elem in b):
        c.append(elem)
print(a)
print(b)
print(c)
