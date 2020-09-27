
# Note: running in PyPy3

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

def prod(a):
    n = a[0]
    for x in a[1:]:
        n*=x
    return n


def genPhyt(n):
    squares = [i**2 for i in range(1,n//2)]

    nums = {}
    cont=1
    for a in range(1,n//2):
        for b in range(a+1,n//2):
            if (a**2+b**2) in squares:
                t = [a,b,int(math.sqrt(a**2+b**2))]
                nums[sum(t)] = t
        cont+=1
    return nums

def pythagoreanTriplet(n, trips):
    if n<12: return -1
    
    try:
        return prod(trips[n])
    except:
        return -1

if __name__ == "__main__":
    
    t = int(input().strip())

    ns = []
    for a0 in range(t):
        ns.append(int(input().strip()))
    
    trips = genPhyt(max(ns))
    
    for n in ns:
        print(pythagoreanTriplet(n, trips))
