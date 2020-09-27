
# Points 100/100
# Notes: -

# 
# ProjectEuler - HackerRank
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

def produto(num):
    if num.count("0")>0: return 0
    m = 1
    for x in num:
        m*=int(x)
    return m

def solution(num, k):
    a = [num[i:i+k] for i in range(len(num)-k+1)]
    b = [produto(i) for i in a]
    return max(b)

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n,k = input().strip().split(' ')
        n,k = [int(n),int(k)]
        num = input().strip()
        print(solution(num, k))