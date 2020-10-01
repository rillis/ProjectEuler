
# Time to achieve the answer: 0.0721034s
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

def primos(nth): #INT [bool] (true=primo) 0 até nth
    a = [True] * (nth+1)
    a[0] = a[1] = False
    for i,isPrime in enumerate(a):
        if isPrime:
            for n in range(i*i, nth+1, i):
                a[n] = False
    return a

def solution(n):

    di = {}
    for x in range(2,n+1):
        if primo[x]:
            s = 0
            c = 0
            for y in range(x+1, n+1):
                if primo[y]:
                    if s+y > n: break
                    else:
                        s+=y
                        c+=1
            if primo[s]:
                di[c] = [x,s]



    return di[max(di)][1]

if __name__ == "__main__":
    n=999999
    start_t = timeit.default_timer()  # DEBUG
    primo = primos(n)
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG