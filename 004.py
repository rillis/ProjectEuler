
# Points 100/100
# Notes: -

# 
# ProjectEuler - HackerRank
# Copyright (c) ProjectEuler - rillis. All rights reserved.
# 
# https://github.com/rillis/ProjectEuler
# 

import math
import os
import random
import re
import sys
import itertools

def gen_palindromes():
    pa = []
    for x in range(100, 1000):
        for y in range(100, 1000):
            t = y*x
            if t == int(str(t)[::-1]): pa.append(t)
    pa.sort(reverse=True)
    return pa

def largest_palindrome(n, pa):
    if n <= 10201: return 0
    a = 0
    for x in pa:
        if x < n: 
            a = x
            break 
    return a

if __name__ == "__main__":
    pa = gen_palindromes()
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(largest_palindrome(n, pa))