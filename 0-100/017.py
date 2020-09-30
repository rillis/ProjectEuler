
# Time to achieve the answer: 0.0012502s
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
di = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8:"eight", 9:"nine", 10:"ten",
      11: "eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen",
      19: "nineteen", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety",
      1000: "onethousand"}

def complete():
    for n in range(21, 1000):
        if not(n%10==0 and n<=90):
           if n<100:
               di[n] = di[n-(n%10)]+di[n%10]
           elif n%100==0:
               di[n] = di[n//100]+"hundred"
           else:
               di[n] = di[n-(n%100)]+"and"+di[n%100]

def solution(n, i=1, s=0):
    if i>n: return s
    return solution(n, i+1, s+len(di[i]))

if __name__ == "__main__":
    complete()
    n = 1000
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG