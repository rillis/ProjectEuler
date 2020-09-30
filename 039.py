
# Time to achieve the answer: 1.6909546s
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

def genTriagles(p):
    t = []
    for a in range(1,p-1):
        for b in range(a+1, p-1):
            c = math.sqrt(a**2+b**2)
            if c.is_integer() and a+b+c == p: t.append([a,b,c])
    return len(t)

def solution(n):
    m1=m2=0

    for x in range(1, n+1):
        g = genTriagles(x)
        if g >= m1:
            m1=g
            m2=x

    return m2

if __name__ == "__main__":
    n=999
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG