
# Time to achieve the answer: 0.07149s
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

def cf(n):
    mn = 0.0
    dn = 1.0
    a0 = int(math.sqrt(n))
    an = int(math.sqrt(n))
    period = 0
    if a0 != math.sqrt(n):
        while an != 2*a0:
            mn = dn*an - mn
            dn = (n - mn**2)/dn
            an = int((a0 + mn)/dn)
            period += 1
    return period


def solution(n):
    odd=0
    for x in range(1,10001):
        c = cf(x)
        if c%2==1:
            odd+=1
    return odd

if __name__ == "__main__":
    n=0
    #f = open("text/XXX.txt", "r")
    #n = f.read().strip().split()
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG