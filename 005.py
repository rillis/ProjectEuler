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

def genPrimes(n):
    primes = []
    for possiblePrime in range(2, n+1):
        isPrime = True
        for num in range(2, possiblePrime):
            if possiblePrime % num == 0:
                isPrime = False
        if isPrime:
            primes.append(possiblePrime)
    return primes

def anyMultiply(arr, n):
    for x in arr:
        if x%n==0: return True
    return False

def smallest_multiply(n, primos):
    a = list(range(1,n+1))
    num = 1
    while sum(a)>len(a):
        for y in primos:
            while(anyMultiply(a, y)):
                for x in range(len(a)):
                    if a[x]%y==0: 
                        a[x]//=y
                num*=y
    return num


if __name__ == "__main__":
    t = int(input().strip())
    ns = []
    for _ in range(t):
        ns.append(int(input().strip()))

    primos = genPrimes(max(ns))
    for n in ns:
        print(smallest_multiply(n, primos))
    
