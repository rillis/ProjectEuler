
# Time to achieve the answer: 0.0339639s
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

def primos(nth): #INT [bool] (true=primo) 0 até nth
    a = [True] * (nth+1)
    a[0] = a[1] = False
    for i,isPrime in enumerate(a):
        if isPrime:
            for n in range(i*i, nth+1, i):
                a[n] = False
    return a

def solution(n):
    di = {}

    for x in range(1000, n+1):
        if primo[x]: di[x] = 1

    di2 = {}
    for x in di:
        di2[x] = 0
        num = x
        p = list([int(''.join(i)) for i in itertools.permutations(str(x))])
        while num < 10000:
            num+=3330
            if num in di and num in p:
                di2[x]+=1

    for x in di2:
        if di2[x] == 2 and x != 1487: return str(x)+str(x+3330)+str(x+6660)
    return 0

if __name__ == "__main__":
    n=9999
    start_t = timeit.default_timer()  # DEBUG
    primo = primos(n)
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG