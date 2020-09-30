
# Time to achieve the answer: 0.5799121s
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
di = {}
amigavel = [False]*10001

def somaDivisores(n):
    if n in di: return di[n]
    if n == 1: return 1
    s=1
    i=2 if n%2==0 else 3
    d=1 if n%2==0 else 2
    for x in range(i,n,d):
        s += x if n%x==0 else 0
    return s


def solution(n):
    s=0
    for x in range(1,n+1):
        r = somaDivisores(x)
        di[x] = r
        for y in di:
            if y == r and somaDivisores(y) == x and x!=y: s+=x+y
    return s

if __name__ == "__main__":
    n=10000
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG