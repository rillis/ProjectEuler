
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

def solution(arrGrid):
    maximum = 0 

    adjacentNumbers = 4
    size = len(arrGrid)
    sizel = size-(adjacentNumbers-1)
    
    v = h = dl = dr = 0
    for r in range(size):
        for c in range(size):
            if c<=16: h = arrGrid[r][c]*arrGrid[r][c+1]*arrGrid[r][c+2]*arrGrid[r][c+3]
            if r<=16: v = arrGrid[r][c]*arrGrid[r+1][c]*arrGrid[r+2][c]*arrGrid[r+3][c]
            if c<=16 and r<=16: dr = arrGrid[r][c]*arrGrid[r+1][c+1]*arrGrid[r+2][c+2] *arrGrid[r+3][c+3]
            if c>=3 and r<=16: dl = arrGrid[r][c]*arrGrid[r+1][c-1]*arrGrid[r+2][c-2] *arrGrid[r+3][c-3]
            maximum = max(maximum,v,h,dl,dr)
    return maximum



if __name__ == "__main__":
    grid = []
    for grid_i in range(20):
        grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
        grid.append(grid_t)
    print(solution(grid))
