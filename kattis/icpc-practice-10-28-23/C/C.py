# code credit: Josh Taylor

from collections import *
from heapq import *
from sys import *
def rn():
    return int(input())
def rl():
    return list(map(int,input().split()))
n,t=rl()
m = 998244353
cache = {}
def ways(num, pos):
    if pos == 0:
        return 1 if num <= t else 0
    if num == 0:
        return 1
    if (num, pos) in cache:
        return cache[(num, pos)]
    bound = 0
    for i in range(pos):
        bound += t * 2**i
    w = 0
    for i in range(0, t+1):
        nn = num - i*2**pos
        if nn > bound:
            continue
        if nn >= 0:
            w += ways(nn, pos-1)
            w %= m
    cache[(num, pos)] = w
    return cache[(num, pos)]
print(ways(n, n.bit_length()))

    
