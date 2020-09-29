
# Time to achieve the answer: 0.0717779s
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

def fatorial(n):
    if n<=1:
        return 1
    else:
        return n*fatorial(n-1)

def procurarFatorial(n):
    c=0
    for i in range(3, n+1):
        s=0
        for x in str(i):
           s+=fatorial(int(x))
        if s == i: c+=i
    return c

def solution(n):
    return procurarFatorial(n)

if __name__ == "__main__":
    n=50000
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG