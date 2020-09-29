
# Time to achieve the answer: 0.1135202s
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
    s=0
    for x in range(2, n):
        i = 0
        for y in str(x):
            i+=int(y)**5
        if i==x: s+=x
    return s

if __name__ == "__main__":
    n=1000000
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG