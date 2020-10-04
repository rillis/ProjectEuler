
# Time to achieve the answer: Xs
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

def nDig(n):
    return len(str(n))

def expression(k):
    n=3
    d=2
    for _ in range(k-1):
        n=n+2*d
        d=n-d
    return nDig(n)-nDig(d)

def solution():
    t = 0
    for x in range(1,1001):
        if expression(x)>0: t+=1

    print(t)

if __name__ == "__main__":
    start_t = timeit.default_timer()  # DEBUG
    print(solution())
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG