
# Time to achieve the answer: 0.0360085s
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

listLetters = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
     'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
def wordValue(word, i=0):
    if i == 0: word = word.upper()
    if len(word)==1: return i+listLetters[word]
    return wordValue(word[1:], i+listLetters[word[0]])

def nthTriangle(nth):
    return int(0.5*nth*(nth+1))

def solution(n):
    i = 0
    for word in n:
        word_value = wordValue(word)
        if word_value in triangleNumber: i+=1
    return i


def preGen(limit):
    t = {}
    for x in range(1,limit+1):
        t[nthTriangle(x)] = x
    return t


if __name__ == "__main__":
    n = input().replace("\"", "").split(",")
    start_t = timeit.default_timer()  # DEBUG
    triangleNumber = preGen(500)
    print(solution(n))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG