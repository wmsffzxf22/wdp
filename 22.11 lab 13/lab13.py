from random import randint
from time import time
from math import gcd
#z.1
def pnwd(a,b):
    n=1
    for k in range(2,min(a,b)+1): #+1 bo może nie osiągnąć min
        if a%k == 0 and b%k == 0:
            n=k
    return n

# print(pwnd(15,21), pwnd(91,39), pwnd(10,13), pwnd(10,20)

#z.2
def nwd(a,b):
    if b == 0:
        return a
    # if b>a:  #zamiana b z a,    można zostawić if'a
    #     return nwd(b,a)
    #tutaj na pewno a>=b>0
    # print(b, a%b)  tutaj do przykładu, nie jest potrzebna w funkcji
    return nwd(b, a%b) #gdy a<b, b,a%b = b,a

# print(nwd(15, 21), nwd(91, 39), nwd(10, 13), nwd(10,20))
# print(nwd(10**6+1,10**9+1))
# print(nwd(10**6+101,10**9+20))

#z.3
# t1=time() #pnwd - 4 sekundy
# for i in range(10**10):
#     a=randint(1,10**6+1)
#     b=randint(1,10**6+1)
#     # n=pnwd(a,b)
#     # n=nwd(a,b)
#     n=gcd(a,b)
# t2=time()
# print(t2-t1)

#z.4
def jest(l,x): #zwraca 1 jeśli x jest w liście l
    for a in l:
        if a == x: return 1
    return 0

# l=[1,3,5,6]
# print(jest(l,2))

def jestsort(l,x): #l ma być posortowana
    s=len(l)//2 #1 el -> 0,  2el -> 1
    # print(l); input()
    if x==l[s]: return 1
    if len(l)==1: return 0
    if x<l[s]: return jestsort(l[:s], x)
    if x>l[s]: return jestsort(l[s:], x)

# l=[1,2,5,7,12,76,214]
# print(jestsort(l,2))

#z.5
# l=[randint(1,10**6) for i in range(1000)]
# l.sort()
# t1=time()
# for i in range(10**4):
#     x=randint(1,10**6)
#     jest(l,x)
# t2=time()
# print(t2-t1)

#z.6
def pierwsza(n):
    for k in range(2, n):
        if n%k==0:
            return 0 #liczba jest złożona
    return 1 #pierwsza

# for i in range(2,101):
#     if pierwsza(i)==1: print(i, end=' ')
#sprawdzic ktore liczby sa piewrsze w zakresie 10**6+1 do 10**6+100
#potem to samo z 10m, 100m, miliard itd

# for i in range(10**9+1,10**9+100):
#     if pierwsza(i)==1: print(i)
#     # print(i, pierwsza(i))
# print()
# print('KONIEC')

def pierwszalep(n):
    for k in range(2, int(n**0.5)+1):
        if n%k==0:
            return 0 #liczba jest złożona
    return 1 #pierwsza

for i in range(10**15+1,10**15+100):
    if pierwszalep(i)==1: print(i)
    # print(i, pierwsza(i))
print()
print('KONIEC')