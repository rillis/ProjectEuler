
# Time to achieve the answer: 0.0174179s
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

def pandigital(st):
    return sorted(st) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def solution(limit):
    pandigitals = {}
    for x in range(1,limit+1):
        st = ""
        for y in range(1, 1000):
            z  = x*y
            sz = str(z)
            if len(st)+len(sz)<=9:
                st+=sz
            else:
                break
        if pandigital(st): pandigitals[x] = st
    return max(pandigitals.values())

if __name__ == "__main__":
    n=10000
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG