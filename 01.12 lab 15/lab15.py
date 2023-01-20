from random import randint

#z.1
# fo = open('liczby.txt', 'w')

# for n in range(20):
#     n=randint(1,100)
#     #rozw 1
#     s=str(n)
#     fo.write(s)
#     fo.write(' ')
#
#     #rozw 2
#     # fo.write(str(n)+' ')
#
# fo.close()

#z.2
# fo = open('liczby.txt', 'r')
# l=[]
# bl=''
# while 1:
#     zn=fo.read(1)
#     if zn=='':
#         break
#     if zn!=' ':
#         bl=bl+zn
#     else:
#         l.append(int(bl))
#         bl=''
#
# print(l)
# fo.close()

#z.3
# fo = open('gwiazdki.txt', 'w')

# for j in range(1,51):
#      for i in range(1,51):
#         fo.write('* ')
#      fo.write('\n')

# for j in range(1,51):
#     for i in range(1,51):
#         a=randint(1,5)
#         if a==1:    #można if randint(1,5)==1
#             fo.write('*')
#         else:
#             fo.write(' ')
#     fo.write('\n')
#
# fo.close()

#z.4
def pierwsza(n):
    for k in range(2, int(n**0.5)+1):
        if n%k==0:
            return 0 #złożona
    return 1 #pierwsza

# fo = open('pierwsze.txt', 'w')
#
# for i in range(1,101):
#     if pierwsza(i)==1:
#         fo.write(str(i)+' ')
#
# fo.close()

#z.5
# fo = open('pierwsze.txt', 'r')
# l=[]
# bl=''
# while 1:
#     zn=fo.read(1)
#     if zn=='':
#         break
#     if zn!=' ':
#         bl=bl+zn
#     else:
#         l.append(int(bl))
#         bl=''
#
# print(l[-1])
# fo.close()

# bl=''
# while 1:
#     zn=fo.read(1)
#     if zn=='':
#         break
#     if zn!=' ':
#         bl=bl+zn
#     else:
#         pbl=bl #poprzedni bl
#         bl=''
#
# ost=int(pbl)
# ost=(ost//100+1)*100     #aby nie było przesunięcia, największa liczba podzielna przez 100
# print(ost)
# fo.close()
#
# fo = open('pierwsze.txt', 'a')
#
# for i in range(ost+1,ost+101):
#     if pierwsza(i) == 1:
#          fo.write(str(i)+' ')
#
# fo.close()

#z.6
fo = open('gwiazdki2.txt', 'w')

x1=randint(1,49)
x2=randint(1,49)
y1=randint(1,49)
y2=randint(1,49)

for j in range(1,51):
     for i in range(1,51):
         if (x1==i and y1==j) or (x2==i and y2==j):   #or zachowuje się jak plus a and jako mnożenie więc dlatego nie dajemy nawaisów
             fo.write('*')
     else:
         fo.write(' ')
     fo.write('\n')

fo.close()