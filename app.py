#Multiplicação de dois números naturais, através de somas sucessivas (Ex.: 6 ∗ 4 = 4 + 4 + 4 + 4 + 4 + 4).

from ast import If


def multi(a, b):
    if (b>1): 
        return a + multi(a, b-1) 
    else: 
        return a

def sum(a, b):
    if(a > 0):
        return 1+ sum(a -1, b)
    elif (b > 0):
        return 1+ sum(a, b -1)
    else:
        return 0

# Calculo de 1 + 1/2 + 1/3 + 1/4 + ... + 1/N.
def calcFrac(n):
    if(n > 1):
        return 1/n + calcFrac(n-1)
    return 1

# Inversão de uma string
def revertString(s): 
    if(len(s) > 0):
        return s[-1] + revertString(s[ : -1]) 
    return ""

#F(1) = 1
#F(2) = 2
#F(n) = 2 ∗ F(n − 1) + 3 ∗ F(n − 2).
def f(n):
    if (n == 1):
        return 1
    if (n == 2):
        return 2
    return 2 * f(n-1) + 3 * f(n-2)

#Gerador de Sequencia de Ackerman:
#A(m, n) = n + 1, se m = 0
#A(m, n) = A(m − 1, 1), se m != 0 e n = 0
#A(m, n) = A(m − 1, A(m, n − 1)), se m != 0 e n != 0.

def ackSeq(m, n):
    if(m == 0):
        return n+1
    if(m!=0 and n == 0):
        return ackSeq(m-1, 1)
    return ackSeq(m - 1, ackSeq(m, n - 1))

#A partir de um vetor de numeros inteiros, calcule a soma e o produto dos elementos do vetor.

def somProd(vet):
    return

print(ackSeq(1,2))
