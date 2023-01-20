# class Zwierze:
#     def __init__(self, gatunek, imie, wiek):
#         self.gatunek = gatunek
#         self.imie = imie
#         self.wiek = wiek
#
#     def wyswietl(self):
#         print(f'{self.gatunek} nazywa się {self.imie}')
#
#     def __repr__(self):
#         return self.gatunek + ' ' + self.imie
#
#     def __eq__(self, other):    # odpowiada znakowi ==
#         if self.wiek == other.wiek: return True
#         else: return False
#
# z1=Zwierze('Słoń', 'Jambo', 30)
# z2=Zwierze('Papuga', 'Polly', 40)
# z3=Zwierze('Hippopotam', 'Potam', 30)

# if z1==z3: print(f'{z1.imie} ma taki sam wiek jak {z3.imie}')

#kiedy eq nie ma podkreśleń
# if z1.__eq__(z3): print(f'{z1.imie} ma taki sam wiek jak {z3.imie}')

# print(z1)
# print(z1.imie)

# z1.wyswietl()
# z2.wyswietl()


#z.1
class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def wyswietl(self):
        print(f'{self.imie} {self.nazwisko} ma {self.wiek}')

    def inicjaly(self):
        return self.imie[0]+self.nazwisko[0]

    # def starszy(self, other):
    #     if self.wiek >= other.wiek: return True
    #     else: return False

    def __ge__(self, other):
        if self.wiek >= other.wiek: return True
        else: return False

    def __repr__(self):
        return self.imie + ' ' + self.nazwisko
#
# o1=Osoba('Anna', 'Kowal', 30)
# o2=Osoba('Jan', 'Kowal', 40)
# o3=Osoba('Maciej', 'Przerwacki', 30)
#
# o1.wyswietl()
# print(o1.inicjaly()) #trzeba użyć printa bo metoda zwraca
# # print(o2.starszy(o3))
# print(o3 >= o2)

#z.2
class Student(Osoba):
    def __init__(self, imie, nazwisko, wiek, nrindeksu, rok):
        super().__init__(imie, nazwisko, wiek)  #super bierze z klasy Osoba trzy pierwsze elementy z konstruktora
        self.nrindeksu = nrindeksu
        self.rok = rok

    def licmag(self):
        if self.rok > 3: return 'magisterskie'
        else: return 'licencjackie'


# s1=Student('Anna', 'Kowal', 20, 202141, 1)
# s2=Student('Jan', 'Kowalski', 22, 214532, 3)
# s3=Student('Adam', 'Kowalik', 25, 421454, 5)
# s4=Student('Joanna', 'Kowalska', 32, 942142,4)
# print(s1.nrindeksu)
# print(s4.licmag())
# print(f'{s3} uczęszcza na studia {s3.licmag()}')
#
# if s1<=s2: print(f'{s1} jest młodszy/a od {s2}')
# else: print(f'{s1} jest starszy/a od {s2}')

#z.3
class Przedmiot:
    def __init__(self, nazwa, cena, stan):
        self.nazwa = nazwa
        self.cena = cena
        self.stan = stan
        self.czyj = 0 #0 oznacza niczyi

    def __repr__(self):
        return (f'{self.nazwa}, {self.cena}, {self.stan}')

p1=Przedmiot('Blender', 200, 'dobry')
p2=Przedmiot('Latarka', 15, 'używany')
# print(p1)
# print(p2)

class Klient(Osoba):
    def __init__(self, imie, nazwisko, wiek=0):
        super().__init__(imie, nazwisko, wiek)
        self.stankonta = 0
        self.lp = []

    def zasilkonto(self, ile):
        self.stankonta+=ile

    def kup(self, co):
        if co.czyj==0:
            self.lp.append(co)
            self.stankonta-=co.cena
            co.czyj=self
        else:
            print('Przedmiot już został kupiony')

    def kupuj(self, other, co): #self kupuje od other
        if co in other.lp:
            c=co.cena
            self.stankonta-=c
            other.stankonta+=c
            self.lp.append(co)
            for i in range(len(other.lp)):
                if other.lp[i]==co: del other.lp[i]
        else:
            print(f'{other} nie ma przedmiotu {co}')

    def przedmioty(self):
        for p in self.lp:
            print(p.nazwa,end=' ')
        print()


k1=Klient('Anna', 'Nowak')
k2=Klient('Adam', 'Adamowski')
# print(k1,k2)
k1.zasilkonto(2000); k2.zasilkonto(50); k2.zasilkonto(20)
print(k1.stankonta, k2.stankonta)
k1.kup(p2)
k1.kup(p1)
print(p1.czyj)
print(k1.stankonta, k2.stankonta)
k2.kupuj(k1,p1)
print(k1.stankonta, k2.stankonta)
k1.przedmioty()
# print(k1.stankonta, k2.stankonta)
# print(k1.lp)
# for i in k1.lp:
#     print(i.nazwa)