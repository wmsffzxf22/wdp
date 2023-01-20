#z.1
# for i in 'To jest zdanie': print(i, end='*') #i przebiega przez całe wyrażenie (razem ze spacjami) i wstawia pomiędzy literami i spacjami gwiazdki

# zd=input('Podaj zdanie:') #podaje zdanie
# l=0 #licznik liter równy na początku 0
# for i in zd: #pętla w której i przebiega przez cały wyraz
#     print(i, end=' ') #drukuje litere i następnie daje spacje
#     l=l+1 #licznik liczy litery ORAZ SPACJE
# print(f'Ilość liter={l}') #tu wstawiamy przed stringiem f przez co możemy dać nawias, w którym zmienna będzie się sama uzupełniała

#z.2
# zd=input('Podaj zdanie:')
# l=0
# for i in zd:
#     if i=='a': l=l+1 #tutaj if sprawdza czy i przebiegające przez zd będzie miało w sobie a, jeżeli będzie to licznik będzie się zwiększał, 'a' - literka, a - zmienna a
# print(f'Ilość liter a = {l}')

#z.3
# zd=input('Podaj zdanie:')
# l=0
# for i in zd:
#     if i==' ': #jeśli spacja to przeskok do następnej linijki
#         print()
#         l=l+1 #teraz liczymy słowa po spacji
#     else:
#         print(i, end='')
# print(f'\nIlość zdań={l+1}') #musi być l+1 ponieważ przy ostatnim zdaniu nie ma spacji
#\n to przeskok do następnej linijki

#z.4 (logarytm)
# znak=1
# s=0
# for i in range(1,1000001):
    #rozwiązanie nr 1 (parzystość)
    # if i%2==0:
    #     s=s-1/i
    # else: s=s+1/i

    #rozwiązanie nr.2 (wzór)
    # s=s-(-1)**i*1/i #np. s-(-1)**5*1/5

    #rozwiązanie nr.3 (znak)(najłatwiejsze)
    #trzeba znak na samym początku napisać!!!!
    # s=s+znak*1/i
    # znak=-znak
# print(s)

#z.4 dalej (liczba pi)
# znak=1
# s=0
# for i in range(1,10001,2):
    #rozwiązanie nr.1 (znak)
    # s=s+znak*1/i
    # znak=-znak

    #rozwiązanie nr.2 (podzielność przez 4)
    # if i%4==1: #podzielna liczba przez 4 z resztą 1 np. 5,9,13 itp.
    #     s=s+1/i
    # else: s=s-1/i #reszta liczb np. 3,7,11...
    #musi być podzielna przez 4 z resztą bo te bliskie 4 muszą być dodatnie, poza tym w range'u liczby skippują liczby parzyste

    #rozwiązanie nr.3 (wzór) (range musi być(1,10001) bez skipowania liczb parzystych)
#     s=s-(-1)**i*1/(2*i-1) #2*i-1: 1->1, 2->3, 3->5 itd.
# print(4*s)

#z.5
# n=int(input('Podaj ilość osób'))
# s=0 #suma=0
# for i in range(n): #i będzie przebiegało przez polecenia n razy
#     st=int(input('Kolejna liczba:')) #tu podaje liczby, które chcę później wykorzystać do średniej
#     s=s+st #tutaj program sumuje wszystkie podane liczby
# print(f'Średnia równa się {s/n}') #s/n, bo wszystkie liczby przez ilość n

#z.6
from math import sqrt, cos, sin
# print(sqrt(2))
# print(cos(0))

# for i in range(1,21):
#     print(f'{i}: {sqrt(i)}')

# for i in range(1,21):
#     print(f' {i}: {sin(i)}')

#z.7
# s=0
# for i in range(1,1001):
#     s=s+(1/i)**2
# print(s)
# print(sqrt(6*s))  #sqrt(6s)=6s 6s=pi^2 s=pi^2/6

#z.8
# t='Ala ma kota'
# print(t[2]) #liczba z kolei od 0, czyli A-0 , l-1 i a-2
# print(t[1])
# print(t[2:8]) #przedział od 2 elementu do 8 elementu (8 nie pokazuje)
# print(t[:5]) #tutaj jest przedział od początku do 5 elementu
# print(len(t)) #ilość znaków + spacje

# t=input('zdanie:')
#rozwiązanie 1
# for i in range(len(t)-1,-1,-1):
#     print(t[i], end='')

#rozwiązanie 2
# for i in range(len(t)): #0 -> l-1, 1->l-2
#     print(t[len(t)-1-i], end='')

#rozwiązanie 3 (najprostsze)
# print(t[5:2:-1]) #od 6 do 3 literki, -1 powoduje, że odwraca się zdanie
# print(t[::-1]) #odwrotne zdanie