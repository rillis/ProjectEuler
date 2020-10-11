
# Time to achieve the answer: 29.9513334s
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

cubes = {}
def pregen(n=10000):
    for x in range(1, n+1):
        cubes[x**3]=x

def isPerm(a,b):
    st = [str(a),str(b)]
    if len(st[0])!=len(st[1]): return False
    for x in st[0]:
        if st[0].count(x) != st[1].count(x): return False
    return True

def permsCube(c):
    t=[]
    for x in cubes:
        if x!=c and isPerm(c,x): t.append(x)
    return t

def solution(n):
    pregen()

    for y,x in enumerate(cubes):
        p = permsCube(x)
        if len(p)==4: return [x,p]

    return 0

if __name__ == "__main__":
    n=0
    #f = open("text/XXX.txt", "r")
    #n = f.read().strip().split()
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG