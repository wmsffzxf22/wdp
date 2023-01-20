#z.1
l=[1,2,3,4,5,6,7,8]
a=l.pop(0) #wyjmuje z listy element (poźniej się nie wyswietla na liście)
print(a)
print(l)
l.pop(2)
print(l)
l.pop(0)
print(l)

#z.2
# l=[1,2,3,4,5,6,7,8,9,10]
# # print(l[0:3])
# # print(l[2:5])
# dl=len(l)
# l1=l[:dl//2]
# l2=l[dl//2:]
# print(l1,l2)

# l=[1,2,3,4,5,6,7,8,9,10,11] #nieparzysta
# # print(l[0:3])
# # print(l[2:5])
# dl=len(l)
# l1=l[:dl//2]
# l2=l[dl//2:]
# print(l1,l2)

#z.3
def scal(l1,l2):
    l=[]
    while True:
        if len(l1)==0:
            l=l+l2
            return l
        if len(l2)==0:
            l=l+l1
            return l
        if l1[0]<l2[0]:
            l.append(l1[0])
            l1.pop(0)
        else:
            l.append(l2[0])
            l2.pop(0)
            #l.append(l2.pop(0))

# l1=[1,3,7]
# l2=[2,4,6,8,9,11]
# print(scal(l1,l2))

#z.4
def sortscal(l): #sortowanie przez scalanie
    if len(l)<=1: return l
    if len(l)==2:
        if l[0]>l[1]:
            c=l[0];l[0]=l[1];l[1]=c
        return l
    l1=l[:len(l)//2]
    l2=l[len(l)//2:]
    l1=sortscal(l1)
    l2=sortscal(l2)
    l=scal(l1,l2)
    return l

# print(sortscal([5,2,22,14,90,3,4,7,1]))

#z.5 i z.6
def sortuj(l): #(bąbelkowe sortowanie)
    for j in range(len(l)-1):
        for i in range(len(l)-1):
            if l[i]>l[i+1]:
                c=l[i];l[i]=l[i+1];l[i+1]=c
    return l

from random import randint
from time import time
# l=[randint(1,1000) for i in range(10**7)]
# print(l)
# t1=time()
# # sortuj(l) #N*N
# # sortscal(l) #N*log(N)
# l.sort()
# t2=time()
# print(t2-t1)

#z.7
def sortmax(l): #max(l)
    for j in range(len(l)-1,1,-1):
        m=max(l[:j+1])
        pm=l.index(m) #pm - pozycja max'a
        c=l[pm]
        l[pm]=l[j]
        l[j]=c

# l=[1,2,4,6,2,22,9,3]
# sortmax(l)
# l=[randint(1,1000) for i in range(1000)]
# print(l)
# t1=time()
# sortuj(l) #N*N
# sortscal(l) #N*log(N)
# sortmax(l)
# l.sort()
# t2=time()
# print(t2-t1)
 #bąbelkowe<max<sortscal<sort