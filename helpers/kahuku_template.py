from sys import stdin

def rl(f=int):
    # read a line and return a list of ints (or other type if specified)
    return list(map(f, input().split()))

def rls():
    # read the whole stdin and return a list of lines
    return [line.strip() for line in stdin.readlines()]