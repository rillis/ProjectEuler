
# Time to achieve the answer: 4.155s
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

import itertools

def check(arr):
    used = []
    for i in range(len(arr)):

        if i == len(arr)-1:
            comp = arr[0][1]
        else:
            comp = arr[i + 1][1]

        if arr[i][2] != comp:
            return False

        if arr[i][0] in used or arr[i][1] in used:
            return False
        else:
            used.append(arr[i][0])
            used.append(arr[i][1])

    sm = [sum(x) for x in arr]
    if len(set(sm)) != 1:
        return False
    return True

def getValue(arr):
    lowest = [150, -1]
    for i in range(len(arr)):
        if arr[i][0] < lowest[0]: lowest = [arr[i][0], i]
    conc = ""
    arr = arr[lowest[1]:] + arr[:lowest[1]]
    for i in arr:
        conc += str(i[0])+str(i[1])+str(i[2])
    return int(conc)


def solution():
    biggest = 0

    perm = itertools.permutations(list(range(1, 11)))

    for p in perm:
        outer_ring = list(p[:5])
        if 10 in outer_ring and 6 in outer_ring:
            inner_ring = list(p[5:])

            arr = [[outer_ring[0], inner_ring[0], inner_ring[1]],
                    [outer_ring[1], inner_ring[1], inner_ring[2]],
                    [outer_ring[2], inner_ring[2], inner_ring[3]],
                    [outer_ring[3], inner_ring[3], inner_ring[4]],
                    [outer_ring[4], inner_ring[4], inner_ring[0]]]

            if check(arr):
                v = getValue(arr)
                biggest = max(biggest, v)
    return biggest

if __name__ == "__main__":
    n=0
    #f = open("text/XXX.txt", "r")
    #n = f.read().strip().split()
    start_t = timeit.default_timer()  # DEBUG
    print(solution())
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG
