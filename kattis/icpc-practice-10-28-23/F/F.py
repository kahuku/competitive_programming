# code credit: Josh Taylor

from collections import *
from heapq import *
from sys import *
setrecursionlimit(1000000)
def rn():
    return int(input())
def rl():
    return list(map(int,input().split()))
n,k=rl()
d=defaultdict(lambda: defaultdict(int))
t = 0
def dfs(a, parent, r):
    l=[]
    m = 0
    for child in d[a]:
        if child == parent:
            continue
        x, y = dfs(child, a, d[a][child])
        l.append(x)
        m=max(y, m)
    l.sort()
    if not l:
        return r, m
    if len(l) == 1:
        return r+l[0], m
    return r+max(l), max(m, sum(l[-2:]))


for i in range(n-1):
    a,b,c = rl()
    t+=c
    d[a][b]=c
    d[b][a]=c
if k > 1:
    print(t)
    quit()
print(max(dfs(1, 0, 0)))

