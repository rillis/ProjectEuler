
# Time to achieve the answer: 1.4702285s
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

def pandigital(a,b,c):
    return sorted(''.join([str(a), str(b), str(c)])) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def solution(n):
    di = {}
    for a in range(1, n+1):
        for b in range(a+1, n+1):
            c=a*b
            if pandigital(a,b,c): di[c] = c
    return sum(di.values())

if __name__ == "__main__":
    n=2000
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG