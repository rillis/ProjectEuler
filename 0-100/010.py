
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

def sieveEratosthenesSum(limit):
    suml = [0] * limit
    a = [True] * limit
    a[0] = a[1] = False
    for i, isprime in enumerate(a):
        if isprime:
            suml[i] = suml[i-1] + i
            for n in range(i*i, limit, i):
                a[n] = False
        else:
            suml[i] = suml[i-1]
    return suml

def solution(n, sumsSieve):
    if n<2: return 0
    return(sumsSieve[n])

if __name__ == "__main__":
    t = int(input().strip())

    ns=[]
    for _ in range(t):
        ns.append(int(input().strip()))
    
    sumsSieve = sieveEratosthenesSum(max(ns)+1)
    
    for n in ns:
        print(solution(n, sumsSieve))
