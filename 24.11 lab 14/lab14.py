#z.1
# fo = open('plik.txt','w')  #jeżeli plik istnieje to to niszczy
# #w - write,  r - read,  a - append
# fo.write('Pierwsza linijka\n') #bez \n teksty się łączą
# fo.write('Druga linijka\n')
# fo.write('Linijka 3')

# fo.close()

#z.2
# fo = open('plik.txt','r')
# s=fo.read(5); print(s) #odczytuje z pliku 5 pierwszych liter i drukuje
# s=fo.read(3); print(s)

# s=fo.read(5); print(s)
# s=fo.read(3); print(s)
#tutaj drukuje pieć pierwszych a potem 3 następne

# s=fo.read(); print(s) #bez żadnego inta drukuje wsyzstko co jest w pliku

# s=fo.read(5); print(s)
# s=fo.read(3); print(s)
# s=fo.read(); print(s)
#tu drukuje najpierw 5 liter, potem 3, potem reszte

# while 1:
#     s=fo.read(3)
#     print(s)
#     if s == '':
#         break

# fo.close()

#z.3
# fo = open('plik.txt','a')
# #dorzucamy 2 liniki do pliku, dwoma inputami
# l1=input('1:')
# l2=input('2:')
# fo.write(l1+ '\n') #trzeba dodać przerwe pomiędzy + a stirngiem
# fo.write(l2+ '\n')
# fo.close()

#z.4
# fo = open('plik.txt','r')
# l=0
# while 1:
#     s=fo.read(1)
#     if s =='':
#         break
#     if s == 'a':
#         l=l+1
#
# print(l)
# print(f'Ilość a = {l}')
#
# fo.close()

#z.5
# s='Ala ma kota'
# print('a m' in s)
#s=fo.readline()

# fo = open('plik.txt','r')
#
# s=input('Podaj słowo: ')
# while 1:
#     lin=fo.readline()
#     if lin == '':
#         break
#     if s in lin: print(lin, end='') #end kasuje print()
#
# fo.close()

# fo = open('pan-tadeusz.txt','r', encoding='utf-8') #encoding polskie znaki
#
# s=input('Podaj słowo: ')
# while 1:
#     lin=fo.readline()
#     if lin == '':
#         break
#     if s in lin: print(lin, end='')
#
# fo.close()

#z.6
# fo=open('plik.txt','r')
# fo2=open('plik2.txt', 'w')
# while 1:
#     z=fo.read(1)
#     if z =='': break
#     if z ==' ': z='*'
#     fo2.write(z)
#
# fo2.close()
# fo.close()

#z.7
fo=open('plik.txt','r')
fo3=open('plik3.txt', 'w')
while 1:
    z=fo.read(1)
    if z =='': break
    fo3.write(z.upper()) #analogicznie można lower

fo3.close()
fo.close()

# s='przykładowe zdanie'
# print(s.upper())