#z.1
# l=[3, 'alfa', 2.71, 'kot']
# print(l)
# print(l[1]) #drugi element listy
# print(l[1:3]) #podlista od elementu drugiego do czwartego (nie czyta 4)
# print(l[3:1:-1]) #podlista od czwartego elementu do drugiego (nie czyta 2)
# print(l[::-1]) #odwrotna lista
# print(l[-1]) #od końca pierwszy element [alfa,2,71,kot,3,alfa,2.71,kot] czyli 3 jako element zerowy
# print(l[-2]) #od końca drugi element
# print(l[-4]) #ostatni element w liście odwrotnej, przy -5 wyskakuje error
# l[0]=4 #zamienia element zerowy, czyli w tym przypadku 3 na 4
# l[-1]='pies' #minusowe przydają się wtedy kiedy lista jest długa
# print(l)

# l2=l #lista 2
# l2[2]=3.14
# l2[-4]=6
# print(l,l2)
#tutaj, ponieważ lista 2 jest równa liście 1 to każda zmiana drugiej powoduje także taką samą zmiane pierwszej listy

# l3=l.copy() #komenda na kopiowanie listy bez zmieniania oryginalnej

# print(l,l3)
# l3[0]=55
# print(l,l3)

#z.2
# l1=[1, 2]
# l2=['trzy', 4.1, 5.2]
# l=l1+l2 #dodawanie list
# print(l)
# l=l+['koniec'] #dodawanie pojedyńczych elementów
# print(l)

# l=[] #pusta lista
#tutaj kwadraty i parzystość muszą być włączone
#kwadraty od 1 do 10
# for i in range(1,11):
#     l=l+[i**2]
# print(l)

#znak elementów parzystych
#rozwiązanie 1
# for i in range(len(l)):
#     if i%2==0:
#         l[i+1]=-l[i+1] #tutaj musi być +1, ponieważ chcemy aby parzyste liczby miały zmieniony znak
# print(l)

#rozwiążanie 2 #znaki parzystości od razu
# for i in range(len(l)):
#     if i%2==1:
#         l[i]=-l[i]
# print(l)

#z.3
# n=int(input('Ilość liczb:'))
# l=[]
# for i in range(n):
#     a=int(input('Kolejna liczba:'))
#     l=l+[a]
#     #te dwie można skrócić do l=l+[int(input('Kolejna liczba:'))]
# print(l)
# print(max(l),min(l))
#
# #max i min wartość inaczej
# mx=l[0]
# mn=l[0]
# for i in range(1,len(l)): #przebiega od 1 do ilości elementów w liście
#     if mx<l[i]: mx=l[i]
#     if mn>l[i]: mn=l[i]
# print(f'minimum={mn}, maximum={mx}') #f oznacza, że w klamry możemy dać zmienne

#z.4
# from math import sin
# n=int(input('Ilość liczb:'))
# l=[]
# for i in range(1,n+1):
#     l=l+[sin(i)]
# print(l)
# mx=l[0]
# mn=l[0]
# for i in range(1,len(l)): #przebiega od 1 do ilości elementów w liście
#     if mx<l[i]: mx=l[i]
#     if mn>l[i]: mn=l[i]
# print(f'minimum={mn}, maximum={mx}')

#z.5
# l=[1, 'dwa', 3.01]
# print(l)
# del l[1]
# print(l)

# l=[]
# for i in range(100,151):
#     l=l+[i]
# print(l)
#rozw 1
# for i in range(5,41,4):
    # print(i, end='')
    # del l[i]
#rozw 2
# for i in range(45,4,-5):
#     del l[i]
#rozw 3
# for i in range(1, len(l)-11):
#     if l[i]%5==0: del l[i]
# print(l)
#rozw 4
# print(l[5:46:5])
# del l[5:46:5]
# print(l)

#z.6
l=[1,2,3,66,55,44,32,51,24,24,8]

# l2=l.copy() #początkowy element na koniec
# l2=l2+[l[0]] #dodaje element taki sam jak zerowy na sam koniec
# del l2[0] #usuwam element zerowy
# print(l2)

# l3=l.copy() #końcowy element na początek
# l3=[l[-1]]+l3 #kolejność ma znaczenie, dodaje na początek końcowy element
# del l3[-1] #usuwam końcowy element
# print(l3)

# l4=l.copy() #odwrócona lista l
# l4=l[::-1]
# print(l4)

# l5=[] #tylko parzyste listy l
# for i in range(len(l)): #ma przebiegać przez długość listy
#     if l[i]%2==0: l5=l5+[l[i]]  #jeżeli przy przebieganiu element będzie parzysty to do listy l5 ma dodać element [l[i]]
# print(l5)

# l6=[] #parzyste liczby o parzystych indeksach
# for i in range(len(l)):
#     if l[i]%2==1 and i%2==0: #indeks 0 -> 1
#         l6=l6+[l[i]]
# print(l6)