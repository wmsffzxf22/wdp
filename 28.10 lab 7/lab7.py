from random import randint
# for i in range(20):
#     print(randint(1,6), end=' ') #można brać też minusowe
#randint() - random int

#z.1
# mn=100
# mx=20
# for i in range(10):
#     r=randint(20,101)
#     print(r, end=' ')
#     if mx<r: mx=r
#     if mn>r: mn=r
# print(f'\nminimum= {mn}, maximum= {mx}')

#z.2
# l=[]
# for i in range(10):
#     r=randint(-5,5)
#     l.append(r)
#     #krócej -> l.append(randint(-5,5))
# print(l, sum(l))

#z.3
#while - powtarza dopóki nie osiągnie warunku
#for - powtarza określoną liczbe razy

# l=0
# while 1: #while True
#     l+=1
#     print('*',end=' ')
#     if l==100: break #break to wymuszone wyjście

# r=randint(1,1000)
# l=0
# print(r)
# while 1:
#     l+=1
#     n=int(input('Podaj liczbe:'))
#     if n>r: print('Liczba jest za duża.')
#     if n<r: print('Liczba jest za mała.')
#     if n==r: break
# print(f'Liczba się za zgadza. Za {l} razem.')

#z.4
# l=[]
# for i in range(10): l.append(0)
# l2=[0 for _ in range(10)] #podkreślnik oznacza że nie chcemy żadnej zmiennej
# print(l, l2)

# rzuty=[0 for i in range(13)]
# print(rzuty)
# for a in range(1000):
#     p=randint(1,6)
#     d=randint(1,6)
#     c=p+d
#     rzuty[c]+=1 #jeżeli suma oczek będzie równa 8 to w liście przy 8 będzie dodane, że udało się rzucić raz taką sume
# print(rzuty)
# for i in range(2,13):
#     print(i, rzuty[i])

#z.5
from random import uniform
# #uniform() - random float
# # for i in range(10):
# #     print(uniform(2.3,5.2))
#
# l=[uniform(0.01,1) for i in range(1000)]
# ilosc=[0 for i in range(10)]
# # print(ilosc, l)
# for a in l:
#     z=int(a*10) #0.574 -> 5.74
#     ilosc[z]+=1 #dodaje jeżeli jest 0,.... to do zerowego elementu, jeżeli z=1,.... to do pierwszego itp
# print(ilosc)
#
# l2=[]
# for a in l:
#     l2.append(1/a)
# print(l2)
#
# il2=[0 for i in range(10)]
# for a in l2:
#     z=int(a)//10
#     il2[z]+=1
# print(il2)
# #bo >0.1 -> <10

#z.6 #największy wspólny dzielnik aka NWD
from math import gcd
for i in range(10):
    a=randint(1,41)
    b=randint(1,41)
    print(a,b,gcd(a,b))