
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

fibonacci = [0,1]

def gen_fibo(n):
    k = 8
    fibo = [1,2,3,5]
    while(k<n):
        fibo.append(k)
        k+=fibo[-2]
    return fibo

def solution(n):
    while fibonacci[-1]<10**(n-1):
        fibonacci.append(fibonacci[-2]+fibonacci[-1])
    return len(fibonacci)-1

if __name__ == "__main__":
    n=1000
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG