
# Time to achieve the answer: 0.0215593s
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

def cortar(a,b):
    sa = str(a)
    sb = str(b)
    l = ""
    if sa.count(sb[0]) > 0:
        l = sb[0]
    elif sa.count(sb[1]) > 0:
        l = sb[1]

    if l!="":
        sa = sa.replace(l, "", 1)
        sb = sb.replace(l, "", 1)
        return int(sa)/int(sb) if sb!="0" else 1000
    return 1000

def coriousFractions():
    di = {}
    for x in range(10, 100):
        for y in range(10, 100):
            if cortar(x,y)==x/y and x!=y and (x%10>0 or y%10>0): di[x+y]=x/y
    return di

def solution(n):
    di = coriousFractions()
    t = 1
    for x in di:
        t*=di[x]
    return int(t)

if __name__ == "__main__":
    n=0
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG