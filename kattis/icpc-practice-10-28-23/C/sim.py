from collections import *
def dec(l):
    t = 0
    for i in range(len(l)):
        t+=l[i]*2**i
    return t
d=defaultdict(list)
z=[0]*4
x=10
for i in range(10):
    z[0]=i
    for j in range(10):
        z[1]=j
        for k in range(10):
            z[2]=k
            for l in range(10):
                z[3]=l
                d[dec(z)].append(z.copy())
for k in sorted(d.keys()):
    print(k)
    for l in d[k]:
        print(l[::-1])
    if k > 9:
        break

