
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

def sieveEratos(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for i,isPrime in enumerate(a):
        if isPrime:
            for n in range(i*i, limit, i):
                a[n] = False
    return a
primo = sieveEratos(1000001)

def allCircular(word):
    t = [""]*len(word)
    t[0] = word[1:]+word[0]
    for i in range(1,len(word)):
        t[i]=t[i-1][1:]+t[i-1][0]
    return t

def solution(n):
    c=0
    for x in range(1, n+1):
        if primo[x]:
            circular = True
            for y in allCircular(str(x)):
                if not primo[int(y)]: circular = False
            if circular:
                #print(x)
                c+=1
    return c

if __name__ == "__main__":
    n=1000000
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG