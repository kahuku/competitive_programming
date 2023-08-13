#!/bin/python3

# Goldman Sachs 2023 intern application

import math
import os
import random
import re
import sys



#
# Complete the 'isPossible' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER c
#  4. INTEGER d
#

def dfs(a, b, c, d):
    if a == c and b == d:
        return True
    elif a > c or b > d:
        return False
    else:
        return dfs(a + b, b, c, d) or dfs(a, a + b, c, d)

def isPossible(a, b, c, d):
    return "Yes" if dfs(a,b,c,d) else "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = int(input().strip())

    b = int(input().strip())

    c = int(input().strip())

    d = int(input().strip())

    result = isPossible(a, b, c, d)

    fptr.write(result + '\n')

    fptr.close()
