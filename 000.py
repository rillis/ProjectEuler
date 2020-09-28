
# Points X/100
# Notes: Running in PyPy3

# 
# ProjectEuler - HackerRank
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
    return n

if __name__ == "__main__":
    t = int(input().strip())

    ns=[]
    for _ in range(t):
        ns.append(int(input().strip()))

    for n in ns:
        start = timeit.default_timer() #DEBUG
        print(solution(n))
        stop = timeit.default_timer() #DEBUG
        print(n, "- runtime:", stop - start) #DEBUG