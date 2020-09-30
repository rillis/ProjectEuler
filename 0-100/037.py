
# Time to achieve the answer: 0.1942178s
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
def sieveEratos(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for i,isPrime in enumerate(a):
        if isPrime:
            for n in range(i*i, limit, i):
                a[n] = False
    return a
primo = sieveEratos(2000001)

def allTrucate(n):
    ns = str(n)
    if len(ns)==2: return [int(ns[0]), int(ns[1])]
    t = [n]*(len(ns)*2-1)
    for i in range(1, len(ns)):
        t[i] = int(ns[0:i])
    for i in range(1, len(ns)):
        t[len(ns)+i-1] = int(ns[::-1][0:i][::-1])
    return t

def solution(n):
    s=0
    for x in range(8,2000001):
        if primo[x]:
            truncatable = True
            for y in allTrucate(x):
                if not primo[y]:
                    if x == 739397: print("-------",y)
                    truncatable = False
                    break
            if truncatable: s+=x
    return s

if __name__ == "__main__":
    n=739397
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG