# Time to achieve the answer: 3.1529905s
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
    ar2 = []
    a = [True] * (nth+1)
    a[0] = a[1] = False
    for i,isPrime in enumerate(a):
        if isPrime:
            for n in range(i*i, nth+1, i):
                a[n] = False
    for x,y in enumerate(a):
        if y:
            ar2.append(x)
    return a,ar2

def isPrime(n): #AKS
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    i = 5
    w = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6-w
    return True

def checkPerm(ar):
    ok = True
    sar = [str(i) for i in ar]
    for x in list(itertools.permutations(sar,2)):
        if not isPrime(int(x[0]+x[1])): return False

    return True

def findMin():
    for al in range(len(primo_ar) - 4):
        a = primo_ar[al]
        for bl in range(al+1, len(primo_ar) - 3):
            b = primo_ar[bl]
            if checkPerm([a,b]):
                for cl in range(bl+1, len(primo_ar) - 2):
                    c = primo_ar[cl]
                    if checkPerm([a,b,c]):
                        for dl in range(cl+1, len(primo_ar) - 1):
                            d = primo_ar[dl]
                            if checkPerm([a,b,c,d]):
                                for el in range(dl+1, len(primo_ar)):
                                    e =primo_ar[el]
                                    if checkPerm([a,b,c,d,e]):
                                        return [a,b,c,d,e]

def solution(n):
    ar = findMin()
    return sum(ar)




if __name__ == "__main__":
    n=10000
    start_t = timeit.default_timer()  # DEBUG
    primo_b, primo_ar = primos(n)
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG