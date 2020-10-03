
# Time to achieve the answer: 0.0831678s
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

def isPalindrome(n):
    s=str(n)
    return int(s[::-1]) == int(s)

def solution():
    p = 0
    for x in range(1,10000):
        n=x
        d = False
        for y in range(49):
            n=n+int(str(n)[::-1])
            if isPalindrome(n):
                d=True
                break
        if not d: p+=1

    return p

if __name__ == "__main__":
    start_t = timeit.default_timer()  # DEBUG
    print(solution())
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG