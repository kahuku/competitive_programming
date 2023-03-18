from collections import *
from heapq import *
from bisect import *
from math import *
from sys import stdin
def rl(f=int):
    # read a line and return a list of ints (or other type if specified)
    return list(map(f, input().split()))
def rn(f=int):
    # read a line and return a single int (or other type if specified)
    return f(input())
def rls():
    # read the whole stdin and return a list of lines
    return [line.strip() for line in stdin.readlines()]