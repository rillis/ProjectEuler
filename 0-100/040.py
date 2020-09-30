
# Time to achieve the answer: 36.3472738s
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

def genIrrational(n):
    st=""
    for x in range(1,1000000):
        st+=str(x)
        if len(st)>=n: break
    return st

def getNth(nth):
    return int(irra[nth-1])

def solution(n):
    return getNth(1)*getNth(10)*getNth(100)*getNth(1000)*getNth(10000)*getNth(100000)*getNth(1000000)

if __name__ == "__main__":
    n=0
    start_t = timeit.default_timer()  # DEBUG
    irra = genIrrational(1000000)
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG