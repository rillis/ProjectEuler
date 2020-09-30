
# Time to achieve the answer: 0.2111553s
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

def sieveEratos(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for i,isPrime in enumerate(a):
        if isPrime:
            for n in range(i*i, limit, i):
                a[n] = False
    return a

primos = sieveEratos(1998001)

def equation(a, b, n=0, c=0):
    s = abs(n**2+a*n+b)
    if primos[s]: return equation(a,b,n+1,c+1)
    else: return c


def solution(n):
    for a in range(-1000, 1000):
        for b in range(-1000,1001):
            n_primos = equation(a,b)
            if not n_primos in di and n_primos > 0: di[n_primos] = a*b
    return di[max(di)]


if __name__ == "__main__":
    n=0
    start_t = timeit.default_timer()  # DEBUG

    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG