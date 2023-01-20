#z.1
# n=int(input('podaj n:'))
# p=1 #zakładamy że liczba jest pierwsza
# for i in range(2,n): #pętla w której i jest wybierane w przedziale od 2 do n
#     if n%i==0: p=0 #jeśli n będzie podzielne przez i (w przedziale) i nie będzie się przez nic dzieliło, czyli p będzie się równało 0 to pętla się kończy
# if p==0: print('złożona') #sprawdza czy p=0
# else: print('pierwsza')

#z.2
# for n in range(1,201): #sprawdza n od 1 do 200
#     p=1 #liczba pierwsza
#     for i in range(2,n): #sprawdza przedział dzielników od 2 do n
#         if n%i==0: p=0 #sprawdza dzielniki
#     if p==1: print(n, end=' ') #jeżeli p=1 to wyświetli (czyli tylko liczby pierwsze)

#z.3 (kwadrat 10x10)
# for j in range(1,11):
#     for i in range(1,11):
#         print('*', end=' ')
#     print() #przeskok do następnej linijki

#z.4 (brzeg kwadratu)
for j in range(1,11):
    for i in range(1,11):
        if j==1 or j==10 or i==1 or i==10: #sprawdza tylko 1,10 pionowo i poziomo
            print('*', end=' ') #jeżeli i,j równają sie tyle to ma wyświetlać gwiazdki
        else: print(' ', end=' ') #jeżeli i,j nie równają się 10 lub 1 to ma być puste
    print()

#z.5
# for j in range(1,11):
#     for i in range(1,11):
#         if i+j==11 or i==j or i==1 or i==10 or j==10 or j==1: #i==j daje przekątną z lewej do prawej, a i+j==11 daje z prawej do lewej
#             print('*', end=' ')
#         else: print(' ', end=' ')
#     print()

#z.6 (szachownica)
# for j in range (1,11):
#     for i in range(1,11):
#         if (i%2==1 and j%2==1) or (i%2==0 and j%2==0): #or'y dodają, and'y odejmują gwiazdki
#             print('*', end=' ')
#         else: print(' ', end=' ')
#     print()

#inaczej
# for j in range(1,11):
#     for i in range(1,11):
#         if i%2==j%2:
#             print('*', end=' ')
#         else: print(' ',end=' ')
#     print()

#z.8 (kontynnuacja 3)
# for j in range(1,11):
#     for i in range(1,11):
#         if i>=j: #or i<=j or i+j<=11 or i+j>=11
#             print('*', end=' ')
#         else: print(' ', end=' ')
#     print()

#z.7 (tabliczka mnożenia)
# print('    ', end='')
# for i in range(1,11):
#     print(i, end='  ')
# print()
# for j in range(1,11):
#     print(j,':', end=' ')
#     for i in range(1,11):
#         print(i*j, end=' ')
#         if i*j<10: print(' ', end='') #tylko aby wyrównać liczby
#     print()

#prościej
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j, end=' ')
#     print()

#z.10 koło
# for j in range(1,11):
#     for i in range(1,11):
#         if ((i-5.5)**2+(j-5.5)**2<=4.5**2): #równanie koła
#             print('*', end='  ')
#         else: print(' ', end='  ')
#     print()
# 
# #okrąg
# for j in range(1,11):
#     for i in range(1,11):
#         if (4**2-4<=(i-5.5)**2+(j-5.5)**2+1<=4**2+4):
#             print('*', end='  ')
#         else: print(' ', end='  ')
#     print()