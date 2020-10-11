
# Time to achieve the answer: 0.087562s
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

numbers={}
def pregen(n=141):
    for x in range(1,n+1):
        ngen = x * (x + 1) // 2
        if 1000 <= ngen <= 9999:
            if not ngen in numbers: numbers[ngen] = []
            numbers[ngen].append(3)
        ngen = x ** 2
        if 1000 <= ngen <= 9999:
            if not ngen in numbers: numbers[ngen] = []
            numbers[ngen].append(4)
        ngen = x*(3*x-1)//2
        if 1000 <= ngen <= 9999:
            if not ngen in numbers: numbers[ngen] = []
            numbers[ngen].append(5)
        ngen = x*(2*x-1)
        if 1000 <= ngen <= 9999:
            if not ngen in numbers: numbers[ngen] = []
            numbers[ngen].append(6)
        ngen = x*(5*x-3)//2
        if 1000 <= ngen <= 9999:
            if not ngen in numbers: numbers[ngen] = []
            numbers[ngen].append(7)
        ngen = x*(3*x-2)
        if 1000 <= ngen <= 9999:
            if not ngen in numbers: numbers[ngen] = []
            numbers[ngen].append(8)

def ciclic(a,b):
    st = [str(a), str(b)]
    return st[0][2:4] == st[1][0:2]

def diff(ar):
    return len(ar) == len(set(ar))

def perfect(ar):
    t = {3:0,4:0,5:0,6:0,7:0,8:0}

    for x in ar:
        for y in numbers[x]:
            if t[y]==0:t[y] = x
    return list(t.values()).count(0)==0

def solution(n):
    pregen()

    for xa in numbers:
        if len(numbers[xa])>0:
            for xb in numbers:
                if len(numbers[xb])>0 and diff([xa,xb]) and ciclic(xa,xb):
                    for xc in numbers:
                        if len(numbers[xc]) > 0 and diff([xa,xb,xc]) and ciclic(xb, xc):
                            for xd in numbers:
                                if len(numbers[xd]) > 0 and diff([xa, xb, xc, xd]) and ciclic(xc, xd):
                                    for xe in numbers:
                                        if len(numbers[xe]) > 0 and diff([xa, xb, xc, xd, xe]) and ciclic(xd, xe):
                                            for xf in numbers:
                                                if len(numbers[xf]) > 0 and diff([xa, xb, xc, xd, xe, xf]) and ciclic(xe, xf) and ciclic(xf,xa):
                                                    if perfect([xa,xb,xc,xd,xe,xf]): return xa+xb+xc+xd+xe+xf
    return 0




if __name__ == "__main__":
    n=0
    #f = open("text/XXX.txt", "r")
    #n = f.read().strip().split()
    start_t = timeit.default_timer()  # DEBUG
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG