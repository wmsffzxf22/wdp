import time, datetime

# z.1
# t=time.time()
# print(t)
#
# s=0
# for i in range(10**6):
#     s=s+i
# print(s)
# print(time.time())

# def czekaj(s):   #program nic nie robi przez s sekund
#     t1=time.time()
#     while True:
#         t2=time.time()
#         if t2-t1>=s:   #musi być większe równe bo nie osiągnie perfekcyjnej równości
#             break

# print('przed')
# czekaj(3)
# print('po')

# for i in range(10):
#     print(i, end=' ')
#     czekaj(0.5)

# time.sleep(2)  #komenda na funkcje czekaj(s)
# print('2 sekundy po')

#z.2
# dzis=datetime.date.today()
# # print(dzis) #wyświetla dzisiejszą date
# # print(dzis.timetuple()) #wyświetla dokładniejszą dzisiejszą date(bez godziny i minut i sekund)
# d=dzis.timetuple()
# print(d.tm_year) #wyświetla z (tupla dzis) rok
# print(d.tm_mon) #wyświetla z (tupla dzis) miesiąc

# innadata=datetime.date(2015,12,30) #przepisujemy zmiennej datetime konkretnego roku jaki chcemy
# print(innadata.timetuple()) #wyświetla szczególne informacje na temat podanej przez nas daty

# r=int(input('Podaj rok: '))
# m=int(input('Podaj miesiąc: '))
# d=int(input('Podaj dzień: '))
#
# data=datetime.date(r,m,d)
# # print(data.timetuple().tm_wday)
# #tm_wday to dni tygodnia, ale poniedziałek to 0 do 6 czyli niedzieli
# da=data.timetuple()
# # print(da.tm_wday)
# l=['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
# print(l[da.tm_wday])

#z.3
# dzis=datetime.date.today()
# wczoraj=datetime.date(2022,11,22)
# t=time.mktime(dzis.timetuple())
# tt=time.mktime(wczoraj.timetuple())
# print(t) #pokazuje sekundy dziś z północy
# print(tt) #pokazuje sekundy wczoraj z północy
# print(t-tt) #odejmuje sekundy dziś z wczoraj i wychodzi 86400 sekund czyli 24 godziny
# #czyli mktime ma obliczać konkretnie ile było sekund w północ danego dnia

#z.4
# dzis=datetime.date.today()
# wczoraj=datetime.date(2022,11,26)
# t=time.mktime(dzis.timetuple())
# tt=time.mktime(wczoraj.timetuple())
#
# t2=time.ctime(t) #wyświetla dzień, miesiąc, dzień, date oraz rok w lepszej wersji niż timetuple
# print(t2)

# t=time.time()
#
# for i in range(10):  #oblicza czas teraz, 10 sekund temu, 100 sekund temu itd.
#     j=10**i
#     t2=time.ctime(t-j)
#     #d=time.ctime(t-10**i) inaczej
#     print(i, t2)

# print(time.ctime(0)) #wyświetla unix time

#z.5
from random import randint
# los=randint(1,10)
# print(f'Wciśnij enter, odczekaj {los} sekund i wciśnij ponownie enter')
#
# input()
# t1=time.time()
# input()
# t2=time.time()
# rt=t2-t1
# if rt>los:
#     print(f'Za długo o {rt-los} sek.')
# else:
#     print(f'Za szybko o {los-rt} sek.')

#z.6
dzis=datetime.date.today()
dzis2=datetime.date.today()
dl=datetime.timedelta(days=1) #dodaje do daty dni, godziny (trzeba ustawić) itp
d=dzis.timetuple()
# print(dzis+dl)
# print(dzis-dl)
# print(dzis+5*dl)
# print(dzis-50*dl)

bm=dzis.timetuple().tm_mon #bm - bieżący miesiąc
print(bm)
while 1:
    dzis=dzis+dl
    m=dzis.timetuple().tm_mon
    if bm!=m: break  # != to przeczenie

while 1:
    dzis=dzis-dl
    dt=dzis.timetuple().tm_mon
    if dt==6: break

print(dzis-dzis2)
