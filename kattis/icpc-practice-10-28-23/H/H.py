# code credit: Kim KangJin

from collections import *
from sys import stdin
from heapq import *
from math import *
def rn():
    return int(input())
def rl():
    return list(map(int,input().split()))

lines = stdin.readlines()
inp = [float(line) for line in lines]

tf = inp[0]
tr = inp[1]
init = inp[2]
precede = []

for i in range(2,len(inp)):
    s = inp[i]
    i = floor(s)
    j = ceil(s)
    ans = 0
    # first input 0
    if(s == 0):
        ans = 0
        print(ans)
    elif s < 1 and s > 0:
        ans = 1
        print(ans)
    elif i <= s and s <= i + tf:
        ans = i
        print(ans)
    elif i + tr <= s and s <= j:
        ans = j
        print(ans)
    elif i + tf <= s and s <= i +tr:
        prevVal = 0
        for idx in range(len(precede)-1, -1, -1):
            if precede[idx] < i + tf or precede[idx] > i + tr:
                prevVal = precede[idx]
                break
        #print("Prev is " + str(prevVal))
        if prevVal < i + tr:
            ans = i
            print(ans)
        elif prevVal > i + tr:
            ans = j
            print(ans)

    precede.append(ans) # store prev val
    '''
    print("precede")
    for i in precede:
        print(i)
    '''

    
    
    #print(s)

