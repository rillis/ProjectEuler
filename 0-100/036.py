
# Time to achieve the answer: 0.4755789s
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

def solution(n):
    s = 0
    for i in range(1, 1000000):
        bi = str(bin(i))[2:]
        if isPalindrome(i) and isPalindrome(bi):
            s+= i
    return s

if __name__ == "__main__":
    n=0
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG