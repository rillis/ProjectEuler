
# Time to achieve the answer: 0.0002762s
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

def solution(ns):
    for x in range(len(ns)-1, 0, -1):
        i=0
        for y in range(x):
            ns[x-1][i] = ns[x-1][i]+max(ns[x][y],ns[x][y+1])
            i += 1
    return ns[0][0]

if __name__ == "__main__":
    ns = []
    while True:
        i = input()
        if i.lower()=="": break
        ns.append([int(i) for i in i.strip().split()])

    start_t = timeit.default_timer()  # DEBUG
    print(solution(ns))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG