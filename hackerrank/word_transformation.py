#!/bin/python3

# Too slow
# Lucid 2023 summer intern application

import math
import os
import random
import re
import sys



#
# Complete the 'getTransformedLength' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING word
#  2. INTEGER t
#

import string

alphabet = list(string.ascii_lowercase)
alphabet.append("ab")

def transformLetter(letter):
    return alphabet[alphabet.index(letter) + 1]

def helper(word, t):
    while t > 0:
        s = ""
        i = 0
        for letter in word:
            if i == 0:
                print(f"Moves: {alphabet.index(letter) + t}")
            i += 1
            s += transformLetter(letter)
        t -= 1
        word = s
        print(t, word)
    return word

def getTransformedLength(word, t):
    return len(helper(word, t)) % (10 ** 9 + 7)

if __name__ == '__main__':
    word = input()
    t = int(input())
    print(getTransformedLength(word, t))