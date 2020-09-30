
# Time to achieve the answer: 4.5577685s
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

number_memory = {}
abundantes = [False]*28124
somaabundantes = {}

def isAbundant(n):
    if n in number_memory: return number_memory[n]
    if n == 1: return 0
    s=1
    i=2 if n%2==0 else 3
    d=1 if n%2==0 else 2
    for x in range(i,n,d):
        s += x if n%x==0 else 0
    return s>n

def solution(n):
    for x in range(1, len(abundantes)):
        abundantes[x] = isAbundant(x)

    for x in range(0, len(abundantes)):
        for y in range(0, len(abundantes)):
            if abundantes[x] and abundantes[y] and x+y not in somaabundantes and x+y<=28123:
                somaabundantes[x+y] = 1

    s=0
    for x in range(1, max(somaabundantes)):
        if x not in somaabundantes:
            s+=x

    print(s)





if __name__ == "__main__":
    n=0
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG