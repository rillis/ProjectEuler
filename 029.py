
# Time to achieve the answer: 0.0181588s
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

def removeDup(l):
    return list(dict.fromkeys(l))

def solution(n):
    li = [0]*9801
    c = 0
    for a in range(2,101):
        for b in range(2,101):
            li[c] = a**b
            c+=1
    li = removeDup(li)
    return len(li)


if __name__ == "__main__":
    n=0
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG