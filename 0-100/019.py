
# Time to achieve the answer: 0.3479372s
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
from datetime import datetime
import timeit


def solution(day,year_limit,cont=0,y=1901,m=1):
    if datetime.strptime("1 "+str(m)+" "+str(y), "%d %m %Y").weekday() == day: cont+=1
    if y==year_limit and m==12: return cont
    if m==12: return solution(day, year_limit, cont, y+1, 1)
    return solution(day, year_limit, cont, y, m+1)

if __name__ == "__main__":
    day = 6
    year_limit = 2000

    start_t = timeit.default_timer()  # DEBUG
    print(solution(day,year_limit))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG