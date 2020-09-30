
# Time to achieve the answer: 3.6815096s
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

def genAllPandigitals(a=0,b=9):
    s = "0123456789"
    t = []
    for x in list(itertools.permutations(s[a:b+1],r=len(s[a:b+1]))):
        s = ''.join(x)
        t.append(s)
    return t

def sub(s, i):
    return s[i-1:i+2]

def solution(n):
    s=0
    pan = genAllPandigitals()
    for x in pan:
        if int(sub(x, 2))%2==0 and int(sub(x, 3))%3==0 and int(sub(x, 4))%5==0 and int(sub(x, 5))%7==0 and int(sub(x, 6))%11==0 and int(sub(x, 7))%13==0 and int(sub(x, 8))%17==0:
            s+=int(x)
    return s

if __name__ == "__main__":
    n=0
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG