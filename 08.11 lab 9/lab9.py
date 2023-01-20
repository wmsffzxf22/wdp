from random import randint

#z.1
# def loslis(a,b,n):
#     #rozw.1
#     # l=[]
#     # for i in range(n):
#     #     l.append(randint(a,b))
#     #rozw.2
#     l=[randint(a,b) for i in range(n)]
#     return l
#
# print(loslis(1,5,3))

#z.2
# def podwoj(lis):
#     for i in range(len(lis)):
#         lis[i]=2*lis[i]
#
# l=[-4,2,4]
# podwoj(l)
# print(l)

#z.3 #nie s=l.sum()
# def suma(l):
#     s=0
#     for i in l: #albo for i in range(len(l)): s=s+l[i]
#         s=s+i
#     return s
# l=[1,2,3,4,57,2]
# print(suma(l))

#z.4
# def suma(l):
#     s=0
#     for i in l:
#         s=s+i
#     return s
# l=['Ala', 'ma', 'kota'] #błąd bo s to int, a nie str
# print(suma(l))

# def suma(l):
#     s=''
#     for i in l:
#         s=s+i
#     return s
# l=['Ala', 'ma', 'kota']
# print(suma(l)) #kontkatencja

#type() rozpoznaje typ zmiennej, np. str, float, int, list
# i=0.12
# print(type(i))
# if type(i) is float: print('działa!')

def suma(l):
    if type(l[0]) is str: #sprawdza czy pierwszy element na liście jest
        # stringiem czy int'em i wybiera poprawną wersje s
        s=''
    else:
        s=0
    for i in l:
        s=s+i
    return s
l=['Ala', 'ma', 'kota']
# l=[1,52,53]
print(suma(l))

#z.5
# def element(lista, x):
#     #rozw.1
#     # if x in lista:
#     #     return 1
#     # else:
#     #     return 0
#     #rozw.2
#     for i in lista:
#         if i==x:
#             return 1
#     return 0
#
# # l=[1,6,3]
# # print(element(l,1))
# l=[randint(1,300) for i in range(101)]
# # print(l)
# for i in range(len(l)):
#     if i%25==0: print()
#     print(l[i], end=' ')
# print()

#z.6
# def dublowanie(l):
#     for i in range(len(l)):
#         for j in range(len(l)):
#             if i!=j and l[i]==l[j]:
#                 return 1
#     return 0
#
# # l=[1,2,3,4,5,3]
# # print(dublowanie(l))
# s=0
# il=10000
# for _ in range(il):
#     l=[randint(1,365) for i in range(25)]
#     # print(dublowanie(l), end=' ')
#     s=s+dublowanie(l)
# print(l)
# print(s)
# print(s/il)