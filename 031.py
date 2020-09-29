
# Time to achieve the answer: 7.4600984s
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

def mount(p100=0, p50=0, p20=0, p10=0, p5=0, p2=0, p1=0):
    return str(p100)+","+str(p50)+","+str(p20)+","+str(p10)+","+str(p5)+","+str(p2)+","+str(p1)

def solution(n):
    di = {}
    for p100 in range(0,300,100):
        for p50 in range(0,250,50):
            for p20 in range(0, 220, 20):
                for p10 in range(0, 210, 10):
                    for p5 in range(0, 205, 5):
                        for p2 in range(0, 202, 2):
                            for p1 in range(0, 201, 1):
                                if (p100 + p50 + p20 + p10 + p5 + p2 + p1) == 200:
                                    di[mount(p100, p50, p20, p10, p5, p2, p1)] = 1

    return len(di)+1

if __name__ == "__main__":
    n=0
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG