
# Time to achieve the answer: 0.0720476s
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

def triangle(n):
    return n*(n+1)//2

def pentagonal(n):
    return n*(3*n-1)//2

def hexagonal(n):
    return n*(2*n-1)

p={}
h={}
def pregen(i=60000):
    for x in range(1, i+1):
        p[pentagonal(x)] = x
        h[hexagonal(x)] = x

def solution(n):
    pregen()
    for x in range(286, n+1):
        tr = triangle(x)
        if tr in p and tr in h: print(tr)

if __name__ == "__main__":
    n=60000
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG