
# Time to achieve the answer: 0.249163s
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

positive= {}

def test(n):
    q= 0
    for x in range(11):
        t =x**n
        l=len(str(t))
        if l==n and t>0:
            q+=1
            positive[t]=1
        elif l>n: return q

def solution(n):
    t=[]
    for x in range(1,1000):
        r=test(x)
        if r>0: t.append(r)
    return len(positive)


if __name__ == "__main__":
    n=0
    #f = open("text/XXX.txt", "r")
    #n = f.read().strip().split()
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG