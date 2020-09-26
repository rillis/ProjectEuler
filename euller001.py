import sys

def n_termos(an, ai, r):
    return ((an-ai)//r)+1

def an(t, r):
    return t-(t%r)

def spa(a1, an, n):
    return ((a1+an)*n)//2

def soma_pa(n, i):
    if n >= i: return spa(i, an(n, i), n_termos(an(n, i), i, i))
    elif n == i: return i
    else: return 0

def mult(n):
    spa3 = soma_pa(n, 3)
    spa5 = soma_pa(n, 5)
    spa15 = soma_pa(n, 15) if n+1>=15 else 0
    return spa3+spa5-spa15


t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(mult(n-1))
