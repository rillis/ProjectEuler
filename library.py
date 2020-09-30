#LISTA DE METODOS UTEIS
import math
import itertools

#--------------------------------- Primos
def primos(nth): #INT [bool] (true=primo) 0 até nth
    a = [True] * (nth+1)
    a[0] = a[1] = False
    for i,isPrime in enumerate(a):
        if isPrime:
            for n in range(i*i, nth+1, i):
                a[n] = False
    return a

#--------------------------------- Progressão aritmética
def numeroTermos(an, a1, r): #INT
    return ((an-a1)//r)+1

def an(a1, n, r): #INT
    return a1+(n-1)*r

#tendo AR
def somaPA(a1, an, n): #INT
    return ((a1+an)*n)//2

#tendo R
def somaPA(a1, r, n): #INT
    return ((a1+an(a1,n,r))*n)//2

#--------------------------------- Fatoração e Divisores
def maiorFator(n): #INT
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

factors_memory = {}
def fatores(n): #INT
    if n in factors_memory: return factors_memory[n]
    i = 2
    fac = {}
    d = 1
    while i <= n:
        if i%2==1: d=2
        for i in range(i, n+1, d):
            if (n % i) == 0:
                if not i in fac: fac[i] = 0
                fac[i] += 1
                n //= i
                break
    factors_memory[n]=fac
    return fac

divisores_memory = {}
def somaDivisores(n):
    if n in divisores_memory: return divisores_memory[n]
    if n == 1: return 1
    s=1
    i=2 if n%2==0 else 3
    d=1 if n%2==0 else 2
    for x in range(i,n,d):
        s += x if n%x==0 else 0
    divisores_memory[n] = s
    return s

#--------------------------------- Gauss (soma de 1-n)
def somaGauss(n): #INT
    return int((n+1)*(n/2))

#--------------------------------- Operações array
def prod(arr): #ARR
    n = arr[0]
    for x in arr[1:]:
        n*=x
    return n

def div(arr): #ARR
    n = arr[0]
    for x in arr[1:]:
        n/=x
    return n

def removeDup(arr): #ARR
    return list(dict.fromkeys(arr))

#--------------------------------- Collatz
def collatz(n): #INT
    return n//2 if n%2==0 else 3*n+1

#--------------------------------- Fatorial
def fatorial(n): #INT
    if n<=1:
        return 1
    else:
        return n*fatorial(n-1)

#--------------------------------- Dictionaries
speechNumbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8:"eight", 9:"nine", 10:"ten",
      11: "eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen",
      19: "nineteen", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety",
      1000: "onethousand"}

letras = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
     'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
def valorPalavra(word, i=0): #String len <= 1000
    if i == 0: word = word.upper()
    if len(word)==1: return i+letras[word]
    return valorPalavra(word[1:], i+letras[word[0]])

#--------------------------------- Fibonacci
def genFibonacci(nth, i=2): #INT até a posição nth
    fibonacci = [0]*(nth+1)
    fibonacci[1] = 1
    if nth <= 1: return fibonacci
    while i<nth+1:
        fibonacci[i]=(fibonacci[i-2] + fibonacci[i-1])
        i+=1
    return fibonacci

def genFibonacciUntil(n): #INT até n
    fibonacci = [0,1]
    while fibonacci[-1] < n:
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
    return fibonacci

#--------------------------------- Outros
def allCircular(word):
    t = [""]*len(word)
    t[0] = word[1:]+word[0]
    for i in range(1,len(word)):
        t[i]=t[i-1][1:]+t[i-1][0]
    return t

def isPalindrome(n): #INT ou STR
    s=str(n)
    return int(s[::-1]) == int(s)

def genTriangles(perimeter): #INT
    t = []
    for a in range(1,perimeter-1):
        for b in range(a+1, perimeter-1):
            c = math.sqrt(a**2+b**2)
            if c.is_integer() and a+b+c == perimeter: t.append([a,b,c])
    return t

def nthTriangle(nth):
    return int(0.5*nth*(nth+1))

def panDigital(n): #INT retorna quantida pandigital, 0: não é
    st = sorted(str(n))
    i=0
    for x in st:
        i += 1
        if int(x)!=i: return 0
    return i

def genAllPanDigitals(a=0,b=9):
    s = "0123456789"
    t = []
    for x in list(itertools.permutations(s[a:b+1],r=len(s[a:b+1]))):
        s = int(''.join(x))
        t.append(s)
    return t

