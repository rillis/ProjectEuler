
# Time to achieve the answer: 0.0001318s
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

def solution(n,m):
    return fatorial(n+m)/(fatorial(n)*fatorial(m))

if __name__ == "__main__":
    n=20
    m=20
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n,m))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG