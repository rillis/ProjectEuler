
# Points 100/100
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

def solution(ns):
    soma = 0
    for n in ns:
        soma+=n
    return str(soma)[0:10]

if __name__ == "__main__":
    t = int(input().strip())

    ns=[]
    for _ in range(t):
        ns.append(int(input().strip()))

    #start = timeit.default_timer() #DEBUG
    print(solution(ns))
    #stop = timeit.default_timer() #DEBUG
    #print("runtime:", stop - start) #DEBUG