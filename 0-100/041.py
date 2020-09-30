
# Time to achieve the answer: 0.57452s
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

def pandigital(n):
    st = sorted(str(n))
    i=0
    for x in st:
        i += 1
        if int(x)!=i: return 0
    return i



def sieveEratos(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for i,isPrime in enumerate(a):
        if isPrime:
            for n in range(i*i, limit, i):
                a[n] = False
    return a


def solution(n):
    for x in range(len(primo)):
        if primo[x] and pandigital(x): print(x)

if __name__ == "__main__":
    n=7652414
    start_t = timeit.default_timer()  # DEBUG
    primo = sieveEratos(n)
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG