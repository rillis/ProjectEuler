
# Time to achieve the answer: 1.5049629s
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

def isPrime(n):
    for x in range(3,int(n**0.5)+1,2):
        if n%x==0: return False
    return True

def solution(n):
    diagonais = [1]
    pri = []
    intervalo = 1
    atual = 1
    ratio = 1


    while ratio > 0.1:
        for x in range(4):
            atual+=intervalo+1
            diagonais.append(atual)
            if isPrime(atual): pri.append(atual)
        ratio = len(pri)/len(diagonais)
        intervalo+=2

    return int(atual**0.5)

if __name__ == "__main__":
    n=0
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG