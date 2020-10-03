
# Time to achieve the answer: 0.5719294s
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

def sameNumbers(a,b):
    return sorted(str(a))==sorted(str(b))

def solution():
    for i in range(1, 1000000):
        certo = True
        for x in range(2, 7):
            if not sameNumbers(i, i*x):
                certo = False
                break
        if certo: return i

if __name__ == "__main__":
    start_t = timeit.default_timer()  # DEBUG
    print(solution())
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG