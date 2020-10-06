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

def isPrime(n): #AKS
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    i = 5
    w = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6-w
    return True

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

def allSame(arr):
    return sum(arr)==arr[0]*len(arr)

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

ascii={'!': 33, '"': 34, '#': 35, '$': 36, '%': 37, '&': 38, "'": 39, '(': 40, ')': 41, '*': 42, '+': 43, ',': 44, '-': 45, '.': 46,
       '/': 47, '0': 48, '1': 49, '2': 50, '3': 51, '4': 52, '5': 53, '6': 54, '7': 55, '8': 56, '9': 57, ':': 58, ';': 59, '<': 60,
       '=': 61, '>': 62, '?': 63, '@': 64, 'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72, 'I': 73, 'J': 74,
       'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85, 'V': 86, 'W': 87, 'X': 88,
       'Y': 89, 'Z': 90, '[': 91, '\\': 92, ']': 93, '^': 94, '_': 95, '`': 96, 'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102,
       'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115,
       't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122, '{': 123, '|': 124, '}': 125, '~': 126}


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

def triangle(n):
    return n*(n+1)//2

def pentagonal(n):
    return n*(3*n-1)//2

def hexagonal(n):
    return n*(2*n-1)

