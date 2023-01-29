
# Time to achieve the answer: 0.0002s
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

def solution(n):
    fibo = [1, 2]
    while True:
        t = fibo[-1] + fibo[-2]
        if t >= n: break
        fibo.append(t)
    s = sum([x for x in fibo if x%2==0])

    return s

if __name__ == "__main__":
    n=4000000
    #f = open("text/XXX.txt", "r")
    #n = f.read().strip().split()
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG]
    final_time = stop_t - start_t
    if(final_time < 0.0001):
        print("TOTAL RUNTIME: <0.0001 s:", final_time)
    else:
        print("TOTAL RUNTIME:", round(final_time, 4), "s")
