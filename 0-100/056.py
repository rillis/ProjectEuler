
# Time to achieve the answer: 0.0555272s
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

def solution():
    m = 0
    for x in range(1, 100):
        for y in range(1, 100):
            z = x**y
            n = 0
            for k in str(z):
                n+=int(k)
            m = max(m, n)
    return m

if __name__ == "__main__":
    start_t = timeit.default_timer()  # DEBUG
    print(solution())
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG