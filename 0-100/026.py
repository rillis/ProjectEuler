
# Time to achieve the answer: 0.0084469s
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

di = {}
def tamanhoRecorrencia(n):
    foundRemainders = [0]*(n+1)
    value = 1
    position = 0
    while foundRemainders[value]==0 and value!=0:
        foundRemainders[value] = position
        value *= 10
        value %= n
        position+=1
    return position-foundRemainders[value]

def solution(n):
    r=0
    for i in range(1, n+1):
        t = tamanhoRecorrencia(i)
        di[t] = i
        r=max(r, t)
    return di[r]

if __name__ == "__main__":
    n=1000
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG