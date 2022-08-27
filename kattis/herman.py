import math

def euclidian(i):
    return math.pi * i ** 2

def taxicab(i):
    return 2 * i ** 2

i = int(input())
print(euclidian(i))
print(taxicab(i))