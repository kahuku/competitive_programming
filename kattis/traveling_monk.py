from sys import stdin
from collections import *
def rn(f=int):
    return f(stdin.readline())
def rns(n, f=int):
    return [rn(f) for _ in range(n)]
def rl(f=int):
    return list(map(f, stdin.readline().split()))
def rls(n, f=int):
    return [rl(f) for _ in range(n)]
def rs():
    return stdin.readline.strip()

def position(time, scent):
    diff = 0
    time_acc = 0
    for h, t in scent:
        if t + time_acc < time:
            time_acc += t
            diff += h
        else:
            time_left = time - time_acc
            diff += time_left / t * h
            return diff
    return diff

a, d = rl()
ascent = rls(a)
descent = rls(d)
low = 0
high = sum(row[1] for row in descent)
total = sum(row[0] for row in ascent)
while low < high - 1e-6:
    mid = (low + high) / 2
    if position(mid, ascent) < total - position(mid, descent):
        low = mid
    else:
        high = mid
print(low)
