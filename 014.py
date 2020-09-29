
# Time to achieve the answer: 0.9317158s
# Notes: Running in PyPy3

#
# ProjectEuler
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
import timeit

limit = 5000001
chainSize_memory = {}
max_chainSize_memory = [3, 1, 2]
max_chainSize_memory.extend([-1] * limit)

def calculate(n):
    return n//2 if n%2==0 else 3*n+1

def chainSize(start):
    if start in chainSize_memory: return chainSize_memory[start]
    initial = start
    size=0
    while start>1:
        start = calculate(start)
        size+=1
        if start in chainSize_memory:
            size+=chainSize_memory[start]
            start = 1
    chainSize_memory[initial] = size
    return size

def solution(n):
    ini = max_chainSize_memory[0]
    if ini>n: return max_chainSize_memory[n]
    maxi_cs = chainSize(max_chainSize_memory[ini-1]) #pega ultimo recorde
    maxi = max_chainSize_memory[ini-1] #pega o x do ultimo recorde
    for x in range(ini, n+1):
        cs = chainSize(x)
        if cs>=maxi_cs:
            maxi_cs = cs
            maxi = x
        max_chainSize_memory[x] = maxi
        max_chainSize_memory[0] = x+1
    return max_chainSize_memory[n]


if __name__ == "__main__":
    t = int(input().strip())

    ns=[]
    for _ in range(t):
        ns.append(int(input().strip()))

    start_t = timeit.default_timer()  # DEBUG
    for n in ns:
        start = timeit.default_timer() #DEBUG
        s = solution(n)
        stop = timeit.default_timer() #DEBUG
        print(n, "-", s, "- runtime:", stop - start) #DEBUG
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG