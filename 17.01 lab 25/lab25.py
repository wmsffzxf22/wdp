from math import *

class Zespolona:
    def __init__(self, re, im=0):
        self.re = re
        self.im = im

    def __repr__(self):
        if self.im == 0:
            return f'{self.re}'
        if self.re == 0:
            if self.im == 1: return 'i'
            elif self.im == -1: return '-i'
            else: return f'{self.im}i'
        if self.im == 1: return f'{self.re}+i'
        if self.im == -1: return f'{self.re}-i'
        if self.im > 0:
            return f'{self.re}+{self.im}i'
        else: str(self.re) + str(self.im) + 'i'

    def abs(self):
        return sqrt(self.re**2 + self.im**2)

    def arg(self):
        if self.re == 0:
            if self.im  > 0: return pi/2
            else: return -pi/2
        if self.re<0:
            return pi+atan(self.im/self.re)
        return atan(self.im/self.re)

    def __add__(self, other):
        return Zespolona(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return Zespolona(self.re*other.re - self.im*other.im, self.re*other.im + self.im*other.re)

    def __eq__(self, other):
        if self.re == other.re and self.im == other.im: return True
        else: return False

# z1 = Zespolona(1,1)
# z2 = Zespolona(-1,0)
# z3 = Zespolona(1,1)
# # # print(z1,z2,z3)
# #
# # print(z1.abs(), z2.abs(), z3.abs())
# # print(z1.arg()*180/pi, z2.arg()*180/pi, z3.arg()*180/pi)
#
# z4 = z1 + z3
# print(z4)
# z5 = z1 * z3
# print(z5)
# print(z1*z1)
# print(z1==z2)
# print(z1==z3)

class Wielomian:
    def __init__(self, lw):
        self.lw = lw
    def __repr__(self):
        s=''
        l=len(self.lw)
        for w in self.lw:
            if w==0:
                l=l-1
                continue #torche jak break tylko jest dalej w pętli, pomija krok w pętli
            if l-1==0:
                s=s+str(w)
            elif l-1==1:
                s=s+str(w)+'x'
            else:
                s=s+str(w)+'x^'+str(l-1)
            if l-1==0: break
            s=s+' + '
            l=l-1
        return s

    def stp(self):
        return len(self.lw)-1

    def __add__(self, other):
        roz_stp = other.stp()-self.stp()
        l1 = self.lw.copy()
        l2 = other.lw.copy()
        if roz_stp > 0:
            lz = [0 for i in range(roz_stp)]
            l1 = lz + l1
        if roz_stp < 0:
            lz = [0 for i in range(-roz_stp)]
            l2 = lz + l2
        for i in range(len(l1)):
            l1[i] = l1[i] +l2[i]
        return Wielomian(l1)

    def __mul__(self, other):
        l1 = self.lw[::-1]
        l2 = other.lw[::-1]
        l3 = [0 for i in range(self.stp() + other.stp()+1)]
        for i in range(len(l3)):  #i=2 l1[0]*l2[2]+l1[1]*l2[1]
            w = 0
            for j in range(i+1):
                if j < len(l1) and i-j < len(l2):
                    w = w + l1[j] * l2[i-j]
            l3[i] = w
        return Wielomian(l3[::-1])


w1 = Wielomian([1,0,2,1])
w2 = Wielomian([-5,1,0])

# print(w1)
# print(w2)
# print(w1.stp(),w2.stp())
# print(w1 + w2)
print(w1 * w2)