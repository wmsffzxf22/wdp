from graphics import *
from random import randint
from time import sleep
win = GraphWin('NazwaOkienka',500,500)
win.setBackground('white')

#z.2
#jeden punkt
# pt=Point(250,250)
# pt.draw(win)
# pt.setOutline('red')

# 3 punkty
# pt=Point(250,250)
# pt.draw(win)
# pt2=Point(300,400)
# pt3=Point(100,230)
# pt2.draw(win)
# pt3.draw(win)

# l = ['red', 'blue', 'yellow']
# #losowe punkty
# for i in range(1,25000):
#     pt=Point(randint(0,499),randint(0,499))
#     # pt.setOutline('red')
#     pt.setOutline(l[randint(0,2)])
#     #2 rozw
#     # x=randint(1,500)
#     # y=randint(1,500)
#     # pt=Point(x,y)
#     pt.draw(win)

#z.3 okręgi centrum to point, radius
# c=Circle(Point(250,250),50)
# c.setOutline('red')
# c.setFill('blue') #wypełnia okrąg
# c.setWidth(5) #grubość
# c.draw(win)

#trzy okręgi
# kol=['red','green','blue']
# for i in range(3):
#     c=Circle(Point(randint(0,500),randint(0,500)),randint(10,50))
#     c.setFill(kol[i])
#     c.draw(win)

#losowe koła
# for i in range(1000):
#     c=Circle(Point(randint(0,500),randint(0,500)),randint(10,50))
#     c.setFill(kol[randint(0,2)])
#     c.draw(win)
#     sleep(0.2)

#z.4
# ov=Oval(Point(100,100),Point(300,200))
# ov.setFill('red')
# ov.draw(win)
#
# rt=Rectangle(Point(300,100),Point(400,180))
# rt.setFill('green')
# rt.draw(win)

#z.5
# l1=Line(Point(100,200),Point(200,200))
# l2=Line(Point(100,100),Point(100,200))
# l3=Line(Point(200,200),Point(100,100))
# l1.draw(win)
# l2.draw(win)
# l3.draw(win)

# l=[]
##n=4
# for i in range(10):  #range(n)
#     l.append(Point(randint(0,499),randint(0,499)))
#
# # for i in range(9):
# #     line=Line(l[i],l[i+1])
# #     line.setWidth(5)
# #     line.draw(win)
# #
# # lo=Line(l[0],l[-1])
# #inaczej ostatnia pętla (bez osobnego line)
# for i in range(10):   #range(n)
#     line=Line(l[i],l[(i+1)%10])    #%n
#     line.setWidth(5)
#     line.draw(win)

#z.6
# n=int(input('Podaj liczbe boków'))
n=5
from math import pi, sin, cos
alfa=2*pi/n
lp=[]
for i in range(n):
    x=250+250*cos(alfa*i)
    y=250+250*sin(alfa*i)
    lp.append(Point(x,y))

for i in range(n):
    li=Line(lp[i],lp[(i+1)%n])
    li.draw(win)


win.getMouse()
win.close()
