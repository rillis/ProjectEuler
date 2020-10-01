
# Time to achieve the answer: 17.8584945s
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

def primos(nth):
    a = [True] * (nth+1)
    a[0] = a[1] = False
    for i,isPrime in enumerate(a):
        if isPrime:
            for n in range(i*i, nth+1, i):
                a[n] = False
    return a

factors_memory = {}
def fatores(n): #INT
    if n in factors_memory: return factors_memory[n]
    i = 2
    fac = {}
    d = 1
    while i <= n:
        if i%2==1: d=2
        for i in range(i, n+1, d):
            if (n % i) == 0:
                if not i in fac: fac[i] = 0
                fac[i] += 1
                n //= i
                break
    factors_memory[n]=fac
    return fac

def solution(n, c):
    conse=1
    last=-1
    for x in range(1, n+1):
        f = fatores(x)
        if len(f)==last: conse+=1
        else: conse = 1
        print("X:",x,"Tamanho:",len(f),"Consecutivo:",conse)
        if len(f)==c and conse==c: break
        last = len(f)


if __name__ == "__main__":
    n=1000000
    start_t = timeit.default_timer()  # DEBUG
    primo = primos(n)
    print(solution(n, 4))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG