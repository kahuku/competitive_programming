# code credit: Josh Taylor

from collections import *
from heapq import *
from sys import *
def rn():
    return int(input())
def rl():
    return list(map(int,input().split()))
for line in stdin:
    line = line.strip()
    s=set(line)
    d=defaultdict(int)
    best = len(line)
    l = r = 0
    a=set()
    while l < len(line):
        if len(d)==len(s):
            while d[line[l]]!=1:
                d[line[l]]-=1
                l+=1
            a.add(line[l:r])
            best = min(best, r-l)
            d[line[l]]-=1
            if d[line[l]] == 0:
                del d[line[l]]
            l+=1
        else:
            if r >= len(line):
                break
            d[line[r]]+=1
            r+=1
    if line in a:
        a.remove(line)
    print(len(a))
            



