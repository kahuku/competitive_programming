# code credit: Josh Taylor

from collections import *
from heapq import *
from sys import stdin
from math import *
def rn():
    return int(input())
def rl():
    return list(map(int,input().split()))
for line in stdin:
    a,b=line.split()
    a=int(a)
    b=float(b)
    print(round(sqrt(a*(b+.16)/0.067)))
