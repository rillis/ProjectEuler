
# Time to achieve the answer: 1.7544907s
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
def pentagonal(nth):
    return (nth*(3*nth-1))/2

def genPentagonal(limit):
    t = {}
    for x in range(1, limit+1):
        t[pentagonal(x)] = x
    return t



def solution(limit):
    for i in pent:
        for j in pent:
            if i-j in pent and i+j in pent: return abs(i-j)
    return 0

if __name__ == "__main__":
    n=3000
    start_t = timeit.default_timer()  # DEBUG
    pent = genPentagonal(n)
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG