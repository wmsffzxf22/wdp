# def wyswietl(a):
#     print('Wyświetlam', a)

# wyswietl(2400)

# def dodaj(a,b):
#     c=a+b
#     print(c)

# wyswietl(2100)
# dodaj(3,9)

# def dodaj(a,b):
#     c=a+b
#     return c #zwracanie, podsumowuje zmienną i zapisuje ją
#
# print(dodaj(4,7))
# d=dodaj(100,400)
# print(d)
# e=dodaj(3,7)+19
# print(e)

#z.1
# def trojka(n):
#     print(n, n**2, n**3)
#
# for i in range(1,11):
#     trojka(i)

#z.2
# def min(a,b):
#     if a>b: return b
#     else: return a
# print(min(2,4))
#
# def max(a,b):
#     if a>b: return a
#     else: return b
# print(max(4,2))
#
# a=int(input('1:'))
# b=int(input('2:'))
# print(min(a,b), max(a,b))

# def min(a,*l): #l jako stała lista
#     mn=a
#     for i in range(len(l)):
#         # print(l[i])
#         if mn>l[i]: mn=l[i]
#     return mn
# print(min(10,22,4,55)) #dowolna liczba parametrów
#
# def max(a,*l):
#     mx=a
#     for a in l:
#         if mx<a: mx=a
#     return mx
# print(max(10,22,4,55))

#z.3
# def potega(a,b):
#     #c=a**b
#     s=1
#     for i in range(b):
#         s=s*a
#     return s #c
# #return powoduje też opuszczenie funkcji
# # print(potega(2,3))
#
# for i in range(1,11):
#     print(potega(2,i), end=' ')
# print()
# for i in range(1,11):
#     print(potega(3,i), end=' ')

#z.4
# def silnia(n):
#     s=1
#     for i in range(1, n+1):
#         s=s*i
#     return s
# # print(silnia(4))
#
# for n in range(1,11):
#     print(2**n*silnia(n)/n**n)
# print()
# for n in range(1,11):
#     print(3**n*silnia(n)/n**n)

#z.5
# def rk(a):   #wzór rekurencyjny
#     if a==1: return 1
#     return rk(a-1)+2
# print(rk(3)) # rk(2)=rk(1)+2    rk(3)=rk(2)+2
#
# def silnia(n):
#     if n==1: return 1
#     return n*silnia(n-1)
# print(silnia(5))

#z.6
#a1=1, a2=1, a3=2, an=a(n-1)+a(n-2)
#1,1,2,3,5,8,21,34

# def fibb(n):
#     #1 rozw.
#     # if n==1: return 1
#     # if n==2: return 1
#     #2 rozw.
#     if n<=2: return 1
#     return fibb(n-1)+fibb(n-2)
#
# # print(fibb(3))
# # for i in range(1,21):
# #     print(i, fibb(i))
#
# for i in range(20,31):
#     a=(5**0.5*fibb(i))**(1/i)
#     print(i,a)
# print((2*a-1)**2)
# #a=(1+sqrt(5))/2

#z.7
def scyfry(n):
    s=0
    while n>0:
        c=n%10 #jeżeli n=123 to reszta będzie 3 itd.
        n=n//10
        s=s+c
    return s
print(scyfry(1111))