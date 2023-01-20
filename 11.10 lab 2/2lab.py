#z.1
# for i in range(5): print(i) #jeżeli nie ma przedziału to liczy od 0
# for i in range(4,8): print(i) #przedstawia przedział bez ostatniej liczby
# for i in range(1,20,3): print(i) #od 1 do 20(nie liczy 20) z różnicą 3 pomiędzy liczbami
# for i in range(4,8): print(i,end=' ') #end='' daje liczby w jednym rzędzie, jeżeli po znaku = cudzysłów będzie bez spacji to liczby będą obok siebie

#z.2
# for i in range(2,21,2): print(i,end=' ') #parzyste liczby w jednym rzędzie od 2 do 20 z różnicą dwa pomiędzy
# for i in range(19,0,-2): print(i,end=' ') #nieparzyste od 19 do 1 z różnicą -2 aby było w dół i aby były nieparzyste
# for i in range(1,11):print(i**2,end=' ') #kwadraty od 1 do 10
#aby było wydrukowane wszystko to pomiędzy nimi trzeba dać print()

#z.3
# n=int(input('podaj n:'))
# m=int(input('podaj m:'))
# if n<=m:
#     for i in range(n,m+1): print(i,end=' ')
# else:
#     for i in range(n, m-1,-1): print(i,end=' ')

#podaje dwie liczby n i m, gdy n będzie mniejsze lub równe od m to program
#pokaże przedział od n do m+1, jednakże gdy n będzie większe od m to program
#pokaże przedział od n do m-1 z różnicą -1 w dół np. od 7 do 3

#z.4
# s=0 #suma
# for i in range(1,101):
#     s=s+i  #1+2+3+4+...+100 czyli taki jaki jest range zmiennej i
# print(s)
#tu program liczy sume 1+2+3+..+100

# s=0
# n=int(input('podaj n:'))
# for i in range(1,n+1):
#     s=s+i
# print(s)
#w tym wypadku program będzie liczyć sume 1+2+3+...+n gdy poda mu się zmienną n

#PĘTLA WHILE!!!
# while WARUNEK:
#     I1
#     I2
# I3 #będzie czytał to dopiero wtedy gdy i1 i i2 będą nie prawdziwe

#z.5
# i=1 #liczba 1, która będzie dodawana(jest pierwszą liczbą w sumie)
# s=0 #suma
# while s<=10**6: #tworze pętle która będzie się powtarzała do momentu kiedy s osiągnie, że jest większe lub równe milion
#     s=s+i #suma 1+2+3+....
#     i=i+1 #zmienna i która przy każdej dodanej liczbie będzie zwiększała się o 1 np. jeżeli s=1 nie osiągnie miliona to s=s+i i później i=i+1 czyli dodaje do siebie 1 czyli mamy sume 1+2 i tak dalej
# print(i-1) #ma wyświetlać najmniejsze i, bo przy osiągnięciu miliona(gdyby było wynikiem było 1415 to byłoby nieprawdziwe, bo 1414 jest najmniejsze)

#z.6
# i=1
# s=0
# while s<=10:
#     s=s+1/i
#     i=i+1
# print(i-1)
# #to samo co zadanie 5, ale tutaj szukamy najmniejszego n i dodajemy ułamki

#z.7
#gdy n=15 to program sprawdza czy n można zapisać za pomocą kwadratu np. 0*0,1*1,2*2,3*3,4*4>15 dla n=15 NIE
#n=16 -''- 4*4==16 TAK

# n=int(input('podaj n:'))
# i=0
# while i*i<n: #np. 1*1,2*2
#     i=i+1 #jeżeli n będzie większe to i będzie się dodawało 1 do siebie
# if i*i==n: #tutaj program sprawdza czy podane n zgadza się z formułą i*i
#     print("tak")
# else:
#     print('nie')

#z.8 (silnia)
# s=1 #zaczynamy sume od 1
# n=int(input('podaj n:'))
# for i in range(1,n+1): #jaki będzie przedział i jest zależne od podanego n
#     s=s*i #suma mnoży się przez przedział i, jeżeli przedział będzie (1,2) to suma najpierw się pomnoży razy 1 a potem dwa tworząc silnie
# print(s)

#z.9 (potęgowanie bez ujemnych jednostek i bez używania potęgowania) ??????????
# s=1 #suma=1
# n=int(input('podaj n:'))
# m=int(input('podaj m:'))
# for i in range(m): #powtarza tyle ile razy jest m np. n=2, m=3 to s=1*2=2, s=2*2=4, s=4*2=8
#     s=s*n
# print(s)
# print(n**m)

#z.10 (ma wyświetlać ile dzielników ma liczba n)
# n=int(input('podaj n:'))
# l=0 #l-liczba liczników na początku
# for i in range (1, n+1): #i jako potencjalny dzielnik
#     if n%i==0: l=l+1
#     # print(i, end=' ') #wyświtla przez co dzieli aby sprawdzać
# print(l)

#w pętli, ale inaczej
# for n in range (1,21): #tutaj komenda pokazuje n od 1 do 20 i ich dzielniki
#     l=0 #dzielnik
#     for i in range (1, n+1): #szukamy dzielników w przedziale
#         if n%i==0:
#             l=l+1
#     print(n,l) #wyświetla liczbe oraz liczbe jej dzielników