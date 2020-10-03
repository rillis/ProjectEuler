
# Time to achieve the answer: 26.8108474s
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

def primos(nth): #INT [bool] (true=primo) 0 até nth
    a = [True] * (nth+1)
    a[0] = a[1] = False
    for i,isPrime in enumerate(a):
        if isPrime:
            for n in range(i*i, nth+1, i):
                a[n] = False
    return a

def isSequencial(a,b):
    r=[]

    sta = str(a)
    stb = str(b)
    if len(sta)!=len(stb): return ""


    di = {}
    for x in range(len(sta)):
        if sta[x] != stb[x]:
            di [stb[x]]=1
            r.append(x)


    if len(di)!=1: return ""

    s = [i for i in sta]
    for x in r:
        s[x] = "*"
    return ''.join(s)




def solution():

    ar = {}

    for x in range(100000, 230000):
        if primo[x]:
            for y in range(x+1, 230000):
                if primo[y]:
                    s = isSequencial(x,y)
                    if s!="":
                        ar[s] = 0

    di = {}
    for x in ar:
        for y in range(0,10):
            n = int(x.replace("*", str(y)))
            print(x, n)
            if primo[n]:
                if not x in di: di[x] = 0
                di[x]+=1

    for x in di:
        if di[x]>=8: print (x, di[x])




if __name__ == "__main__":
    start_t = timeit.default_timer()  # DEBUG
    primo = primos(1000000)
    print(solution())
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG