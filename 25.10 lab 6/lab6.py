#z.1
# s='Ala ma kota'
# lz=list(s) #robi liste z zmiennej s
# print(lz)
# # print(len(s), len(lz)) #lista lz ma tyle samo znaków co string s
# for i in range(len(lz)): #przebiega przez długość lz
#     print(lz[i], end='*') #drukuje elementy listy lz i pomiędzy nimi daje gwiazdki
# print()
# #inaczej
# for i in lz: #tutaj i przebiega przez lz, bo wiadomo że jest to lista ze stringa s
#     print(i, end='*')

#z.2
# s='Ala ma kota'
# lz=list(s)
# ile=lz.count('a') #liczy ile jest a w stringu
# można zapisać też przez ile=s.count('a')
# print(ile)

# s=input('Podaj zdanie:')
# lz=list(s)
# ile=lz.count('a')
# print(f'Ilość a = {ile}.')

#z.3
# i=321
# lz=list(i) #nie może z tego stworzyć listy ponieważ nie jest to string
# print(i)

# i=321
# s=str(i)
# lz=list(s)
# print(lz)

from math import factorial
# print(factorial(4))
# print(factorial(5))
# print(factorial(6))

# n=factorial(1000)
# s=str(n)
# lz=list(s)
# # ile=lz.count('9')
# # print(f'Ilość dziewiątek: {ile}.')
# # print(lz.count('9')) #skrócona wersja
#
# for i in range(10):
#     z=str(i)
#     print(i, lz.count(z)) #drukuje najpierw i od 0 do 10-ątki otwartej i potem
#     #liczy i drukuje z lz zmienne 'z' które są stringiem i (ponieważ lista jest
#     #stworzona ze stringów)

#z.4
# lz=list('Alamakota')
# print(lz)
# print(lz.index('a')) #pokazuje pierwszy najmniejszy indeks
# print(lz.index('m'))
# print(lz.index('k'))
# print(lz.index('s')) #tu error ponieważ w liście stworzenej ze stringa nie ma elementów 's'

#aby skrócić dodawanie elementów do listy używamy l.append()
#l=l+[123] <==> l.append(123)

# l=[]
# for n in range(31):
#     l.append((3**n)-2**n)
# print(l)
# print(l.index(1161737179)) #patrzymy który ma indeks
#
# print(3**19-2**19)

#z.5
# l=[1,'dwa',3.01]
# print(2 in l) #sprawdza czy element jest w liście i daje albo False albo True

# l=[]
# for n in range(31):
#     l.append((3**n)-2**n)
# print(l)
#
# l2=[]
# #rozw1
# # for i in range(len(l)): #i przebiega przez ilość elementów na liście
# #     l2.append(l[i]%19) #kiedy i przebiega przez liste l to dodaje reszte
# #     # z dzielenia przez 19 przez każdą liczbe
#
# #rozw2
# for a in l: #łatwiejszy zapis, a przebiega przez liste l
#     l2.append(a%19) #jeżeli a trafi na element to go dzieli go przez 19 i dodaje do l2
# print(l2)
# # print(10 in l2)
# # print(11 in l2)
#
# x=int(input('Podaj liczbe od 0 do 18:'))
# if x in l2:
#     print(f'{x} występuje w l2 {l2.count(x)} razy.')
#     # drukuje podane x i oblicza ile jego jest w l2
# else:
#     print(f'{x} nie występuje w l2.')

#z.6
# l=[]
# for i in range(1,101):
#     l.append(1/i)
# print(l)
# print(sum(l), min(l), max(l))
# #sum - suma wszystkich elementów l,
# #min - najmniejszy element,
# #max - największy element
# print(sum([1,2,3,3,5,0,4])) #możemy wpisać w sume od razu liste

# n=factorial(1000)
# s=str(n)
# lz=list(s)
# print(lz)
#
# l2=[]
# for a in lz:
#     l2.append(int(a)) #a przebiega przez liste lz i zamienia z niej
      # stringi liczbowe na normalne liczby
# print(l2)
# print(sum(l2))

#z.7
# n=factorial(1000)
# s=str(n)
# lz=list(s)
# print(lz)
#
# lp=[] #lista pomocnicza
# for i in range(len(lz)-1): #aby liczba miała pary
#     lp.append(lz[i]+lz[i+1]) #konkatencja dwóch elementów obok siebie aby tworzyły pare
# print(lp)
# for i in range(100): #teraz chcemy aby przed liczbą par się wyświetlało o jakie pary nam chodzi
#     if i<10:
#         z='0'+str(i) #jeżeli mamy 1, 2, 3, itd do 9 to chcemy uzyskać 01,02, więc
#         #dodajemy string '0' + zamieniamy i na string
#     else: z=str(i) #inne liczby drukują się normalnie
#     print(z, ':', lp.count(z)) #najpierw o jakie pary nam chodzi, a później
#     #wybiera z listy pomocniczej te pary które odpowiadają z'towi