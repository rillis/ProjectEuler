
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

def gen_fibo(n):
    k = 8
    fibo = [1,2,3,5]
    while(k<n):
        fibo.append(k)
        k+=fibo[-2]
    return fibo

def even_fibonacci(n):
    fibo = gen_fibo(n)
    soma = sum([i if i%2==0 else 0 for i in fibo])
    return soma


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        print(even_fibonacci(n))