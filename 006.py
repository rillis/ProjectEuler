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

def somaGauss(n):
    return int((n+1)*(n/2))

def somaQuadrados(n):
    return int((n*(n+1)*(2*n+1))/6)

def absDiffSquares(n):
    a = somaGauss(n)**2
    b = somaQuadrados(n)
    return abs(a-b)

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(absDiffSquares(n))