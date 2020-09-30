
# Time to achieve the answer: 0.0502014s
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

def primos(nth):
    a = [True] * (nth+1)
    a[0] = a[1] = False
    for i,isPrime in enumerate(a):
        if isPrime:
            for n in range(i*i, nth+1, i):
                a[n] = False
    return a

def solution(n):
    di = {}
    for y in range(2, len(primo)):
        if primo[y]:
            for z in range(1,500):
                di[y+2*z**2] = 1

    for x in range(33, len(primo)):
        if not primo[x] and x%2==1 and not x in di: return x


if __name__ == "__main__":
    n=1000
    primo = primos(6000)
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG