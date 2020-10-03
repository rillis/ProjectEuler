# Time to achieve the answer: 0.1331012s
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

naipes = {"C": 1, "D": 2, "H": 3, "S": 4}
cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
sequence = {2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:10,10:11,11:12,12:13,13:14,14:2}
cards_r = {value : key for (key, value) in cards.items()}
naipes_r = {value : key for (key, value) in naipes.items()}

def genCards(s):
    c = []
    for x in s:
        c.append([cards[x[0]], naipes[x[1]]])
    return c

def allSame(arr):
    return sum(arr)==arr[0]*len(arr)

def consecutive(arr):
    for card in arr:
        achou = True
        c = card
        for _ in range(4):
            if arr.count(sequence[c])==0:
                achou=False
                break
            c=sequence[c]
        if achou:
            return True
    return False

def qtdCards(arr):
    di = {}
    for x in arr:
        if not x in di: di[x]=0
        di[x]+=1
    return di

def highcard(hand, n):
    c = sorted([i[0] for i in hand], reverse=True)
    return c[n]

def bestGame(hand):
    n = sorted([i[1] for i in hand])
    c = sorted([i[0] for i in hand])

    # Royal Flush
    if c==[10,11,12,13,14] and allSame(n): return [1000, 1]

    # Straight Flush
    if consecutive(c) and allSame(n): return [999, sum(c)]

    qtd = qtdCards(c)

    # Four of a Kind
    if 4 in qtd.values():
        for x, y in zip(qtd, qtd.values()):
            if y==4: return [998, 4*x]

    # Full House
    if 3 in qtd.values() and 2 in qtd.values():
        return [997,sum(c)]

    # Flush
    if allSame(n): return [996, sum(c)]

    # Straight
    if consecutive(c): return [995, sum(c)]

    # Three of a kind
    if 3 in qtd.values():
        for x, y in zip(qtd, qtd.values()):
            if y==3: return [994, 3*x]

    # Two pairs and One Pair
    if 2 in qtd.values():
        p = 0
        c = 0
        for x, y in zip(qtd, qtd.values()):
            if y == 2:
                p+=1
                c+=x*2
        if p==2: return [993, c] #2
        return [992, c] #1

    return [991, max(c)]

def winner(hand1, hand2):
    b = [bestGame(hand1), bestGame(hand2)]
    if b[0][0] > b[1][0]: return 1
    if b[0][0] < b[1][0]: return 2

    if b[0][1] > b[1][1]: return 1
    if b[0][1] < b[1][1]: return 2

    for i in range(5):
        hc1 = highcard(hand1, i)
        hc2 = highcard(hand2, i)
        if hc1>hc2: return 1
        if hc2>hc1: return 2

def solution(ns):
    di = {1:0, 2:0}
    for x in ns:
        h1 = genCards(x[0:5])
        h2 = genCards(x[5:])
        di[winner(h1,h2)]+=1
    return di


if __name__ == "__main__":

    ns = []
    while True:
        a = input()
        if a != "": ns.append(a.strip().split())
        else: break
    start_t = timeit.default_timer()  # DEBUG
    print(solution(ns))
    stop_t = timeit.default_timer()  # DEBUG
    print("TOTAL RUNTIME:", stop_t - start_t)  # DEBUG
