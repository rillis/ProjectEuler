
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

def solution(n):
    return n

if __name__ == "__main__":
    t = int(input().strip())

    ns=[]
    for _ in range(t):
        ns.append(int(input().strip()))

    start_t = timeit.default_timer()  # DEBUG
    for n in ns:
        start = timeit.default_timer() #DEBUG
        s = solution(n)
        stop = timeit.default_timer() #DEBUG
        print(n, "-", s, "- runtime:", stop - start) #DEBUG
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG