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

prime_occurences = [0,2,3]

def isPrime(num):
    i = 2
    while i <= math.ceil(math.sqrt(num)):
        if num % i == 0 and num != i: return False
        i += 1
    return True

t = int(input().strip())
for a0 in range(t):
    position = int(input().strip())
    try:
        if prime_occurences[position]:
            print(prime_occurences[position])
    except:
        ptr = len(prime_occurences)
        i = ptr - 1
        num = prime_occurences[i]+1
        while ptr <= position:
            if isPrime(num):
                prime_occurences.append(num)
                ptr += 1
            num += 1
        print(prime_occurences[position])
