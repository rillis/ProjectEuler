
# Time to achieve the answer: 0.0004136s
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

def solution(n,s=0):
    if len(n)==1: return s+int(n)
    return solution(n[1:], s+int(n[0]))

if __name__ == "__main__":
    n=str(fatorial(100))
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG