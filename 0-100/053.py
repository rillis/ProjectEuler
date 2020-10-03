
# Time to achieve the answer: 0.1172198s
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

def comb(n,r):
    return fatorial(n)//(fatorial(r)*fatorial(n-r))

def fatorial(n): #INT
    if n == 0: return 1
    if n<=1:
        return 1
    else:
        return n*fatorial(n-1)

def solution(c=0, n=1):
    if n==101: return c
    for r in range(n+1):
        co = comb(n, r)
        if co>1000000:
            c+=1
    return solution(c, n+1)


if __name__ == "__main__":
    start_t = timeit.default_timer()  # DEBUG
    print(solution())
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG