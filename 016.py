
# Time to achieve the answer: 0.0006686s
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
def solution(n, i=0):
    if len(n) == 1: return i+int(n)
    i+=int(n[0])
    return solution(n[1:], i)

if __name__ == "__main__":
    n=str(2**1000)
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG