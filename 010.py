
# Points X/100
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

'''
def sieveEratosthenes(n):
    primes = [2]
    primes.extend(list(range(3, n+1, 2)))
    for possiblePrime in primes:
        #print(possiblePrime)
        for x in primes[1:]:
            if x%possiblePrime==0 and possiblePrime!=x:
                primes.remove(x)
    return primes
'''

def sieveEratosthenes(n):
    primes = [False, False, True]
    primes.extend([True]*(n-2))

    for num in range(3, n+1):
        if num%2==1:
            for n in range(3, len(primes), 2):
                if num%n==0: 
                    primes[num]=False
                    break
        else: primes[num]=False

    print(len(primes))

def solution(n, primes):
    if len(primes)<1 or n<2: return 0
    s = 0

    #print(primes)

    '''
    if n>=(primes[-1]//2):
        for x in range(len(primes)-1,-1,-1):
            if primes[x]<=n:
                return sum(primes[:x+1])
    else:
        for y in range(len(primes)):
            if primes[y]>n:
                return sum(primes[:y])
    '''

if __name__ == "__main__":
    t = int(input().strip())

    ns=[]
    for _ in range(t):
        ns.append(int(input().strip()))
    
    primes = sieveEratosthenes(max(ns))

    for n in ns:
        print(solution(n,primes))
