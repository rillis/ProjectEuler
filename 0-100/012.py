
# Points 100/100
# Notes: Running in PyPy3

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
import copy

factors_memory = {}
divisors_memory = {}
mintri_memory = {}

def triangular(n):
    return n * (n + 1) // 2

def factors(nr):
    if nr in factors_memory: return factors_memory[nr]
    i = 2
    fac = {}
    d = 1
    while i <= nr:
        if i%2==1: d=2
        for i in range(i, nr+1, d):
            if (nr % i) == 0:
                if not i in fac: fac[i] = 0
                fac[i] += 1
                nr //= i
                break
    factors_memory[nr]=fac
    return fac


def divisors(n):
    if n in divisors_memory: return divisors_memory[n]
    divi = 1

    f = factors(n).values()

    for x in f:
        divi *= (x + 1)

    divisors_memory[n] = divi
    return divi


def minTriangularDiv(n):
    if n in mintri_memory: return mintri_memory[n]
    if n == 1: return 3
    i = d = 1
    while d <= n:
        i += 1
        num = triangular(i)
        d = divisors(num)

    mintri_memory[n] = num
    return num


def solution(ns):
    for n in ns:
        print(minTriangularDiv(n))


if __name__ == "__main__":
    t = int(input().strip())
    ns = []
    for _ in range(t):
        ns.append(int(input().strip()))
    solution(ns)