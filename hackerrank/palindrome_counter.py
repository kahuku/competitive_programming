#!/bin/python3

# Too slow

import math
import os
import random
import re
import sys



#
# Complete the 'countPalindromes' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromes(s, window_size):
    count = 0
    for window_start in range(len(s) - window_size + 1):
        s2 = s[window_start:window_start + window_size]
        if s2 == s2[::-1]:
            count += 1
    return count

def countPalindromes(s):
    count = len(s)
    for window_size in range(2, len(s) + 1):
        count += palindromes(s, window_size)
    return count

if __name__ == '__main__':

    s = input()

    result = countPalindromes(s)

    print(result)
