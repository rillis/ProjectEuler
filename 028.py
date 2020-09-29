
# Time to achieve the answer: 0.0043669s
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
    s = atual = 1
    times = (n-1)//2
    e = 2
    for x in range(times):
        for _ in range(4):
            atual += e
            s += atual
        e+=2
    print(s)

if __name__ == "__main__":
    n=1001
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG