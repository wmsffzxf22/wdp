#z.1
# a=10
# b=12
# print(a,b)
# c=a #c przejmuje wartość a
# a=b #a przejmuje wartość b
# b=c #b przejmuje wartość c, czyli kiedy a=10 i b=12 to teraz a=12 i b=10
# print(a,b)

#z.2
# def zmien(a,b):
#     c=a
#     a=b
#     b=c
#     print(a,b)
#
# a=3
# b=5
# print(a,b) #nie przeszło bo a i b są oznaczone zmiennymi poza funckją, poza tym w funckji już jest print
# zmien(3,5) #tu przeszło bo podaliśmy w funkcji zmienne a i b

#z.3
# def zamien(l):
#     c=l[0]
#     l[0]=l[1]
#     l[1]=c
#
# l=[10,1000]
# print(l)
# zamien(l) #dla list nie trzeba umieszczać w funkcji print ani return
# print(l)

#z.4
# def odwroc(l):
#     #l[0]<>l[len(l)-1]
#     #l[1]<>l[len(l)-2]
#     #l[i]<>l[len(l)-i-1]
#     #rozw 1
#     # for i in range(len(l)//2):
#     #     c=l[i]
#     #     l[i]=l[-i-1]
#     #     l[-i-1]=c
#     #rozw 2
#     l2=l[::-1] #tworze liste 2 która jest odwrotna
#     for i in range(len(l2)):
#         l[i]=l2[i]
#
# l=[1,2,4,12,10]
# odwroc(l)
# print(l)
#można też użyć l.reverse() bez robienia funkcji

#z.5
#(sortowanie bąbelkowe)
#jedno z rozwiązań, nie najszybsze, ale najprostsze
#10,15,3,18,7,20,12   7 elementów
#10,3,15,7,18,12,20    6 przebiegów, bo później 7 element nie będzie miał innego wyjścia
#3,10,7,15,12,18,20
#3,7,10,12,15,18,20   [3 przebiegi wystarczą dla tej listy]
#czyli dla n-elementowej listy potrzebujemy n-1 przebiegów

# def sortuj(l):
#     #jeden przebieg
#     # for i in range(len(l)):
#     #     if l[i]>l[i+1]:
#     #         c=l[i]
#     #         l[i]=l[i+1]
#     #         l[i+1]=c
#
#     #wiele przebiegów
#     for j in range(len(l)-1):
#         for i in range(len(l)-1):  #można -j w range'u????
#             if l[i] > l[i + 1]:
#                   c=l[i]
#                   l[i]=l[i+1]
#                   l[i+1]=c

# l=[10,15,3,18,7,20,12]
# sortuj(l)
# print(l)

# l=['kot', 'pies', 'Ala', 'Zenon']
# sortuj(l) #sortuje najpierw duże litery alfabetycznie a potem małe alfabetycznie
# print(l)


#z.6
def sortuj(l):
    for j in range(len(l)-1):
        for i in range(len(l)-1):
            if l[i] > l[i + 1]:
                  c=l[i]
                  l[i]=l[i+1]
                  l[i+1]=c

# zd=input('Wpisz zdanie: ')
# #cel: ['Ala', 'ma', 'kota']
# sl=''
# ls=[]
# for z in zd:
#     if z == ' ':
#         ls.append(sl)
#         sl=''
#     else:
#         sl=sl+z
#
# ls.append(sl) #dodaje ostatni wyraz
# print(ls)

#inaczej
# ls=zd.split(' ') #specjalna komenda aby rozdzielać słowa\
# # sortuj(ls)
# print(ls)
# for a in ls:
#     print(a, end=' ')

#sortowanie po krótkich zdaniach

def sortuj2(l):
    for j in range(len(l) - 1):
        for i in range(len(l) - 1):
            if len(l[i]) > len(l[i + 1]):
                c = l[i]
                l[i] = l[i + 1]
                l[i + 1] = c

def sortuj3(l, typ): #??????????
    for j in range(len(l) - 1):
        for i in range(len(l) - 1):
            if typ==0:
                if l[i] > l[i + 1]:
                    c = l[i]
                    l[i] = l[i + 1]
                    l[i + 1] = c
            else:
                if len(l[i]) > len(l[i + 1]):
                    c = l[i]
                    l[i] = l[i + 1]
                    l[i + 1] = c

ls=['Ala', 'kot', 'pies', 'Zenon']
# ls=[65,21,64,1]
sortuj(ls)
print(ls)
