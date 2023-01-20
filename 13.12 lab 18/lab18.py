from graphics import *
from time import sleep
from random import randint,uniform
from math import pi, cos, sin
win = GraphWin('Window',800,800)
win.setBackground('white')

#z.1
# c=Circle(Point(250,250),50)
# c.setOutline('red')
# c.setFill('red')
# c.draw(win)
# c.move(10,-60) #10 w prawo, -60 w góre

# ov=Oval(Point(350,350),Point(450,400))
# ov.setFill('red')
# ov.draw(win)
#
# c=Circle(Point(100,100),80)
# c.setFill('blue')
# c.draw(win)
#
# rt=Rectangle(Point(500,500),Point(700,600))
# rt.setFill('green')
# rt.draw(win)
#
# kier=1
# li=0
# while 1:
#     if kier==1:
#         c.move(1,1)
#     else:
#         c.move(-1,-1)
#     li=li+1
#     sleep(0.005)
#     if li==650:
#         kier=-kier
#         li=0
# #kolejność jest ważna, druga będzie nad pierwszą, a druga pod trzecią

#z.2
# k=win.getKey()   #wstrzymuje działanie
# if k=='a': cośtam

# c=Circle(Point(100,100),80)
# c.setFill('blue')
# c.draw(win)
#
# while 1:
#     k=win.getKey()
#     if k=='a': c.move(-10,0)
#     if k=='w': c.move(0,-10)
#     if k=='d': c.move(10,0)
#     if k=='s': c.move(0,10)
#     if k=='q': break

#z.3
# x=400
# y=400
# pt=Point(x,y)
# pt.draw(win)
# while 1:
#     k=randint(1,4)
#     if k==1:
#         x=x-1
#     if k==2:
#         x=x+1
#     if k==3:
#         y=y-1
#     if k==4:
#         y=y+1
#     pt=Point(x,y)
#     pt.draw(win)

# k=1
# while 1:
#     if randint(1,20)==1:
#         k=randint(1,4)
#     if k==1:
#         x=x-1
#     if k==2:
#         x=x+1
#     if k==3:
#         y=y-1
#     if k==4:
#         y=y+1
#     pt=Point(x,y)
#     pt.draw(win)

#z.4
# x=400
# y=400
# pt=Point(x,y)
# pt.draw(win)
# alfa=0
# while 1:
#     alfa=alfa+randint(-2,2)/10
#     x=x+cos(alfa)
#     y=y+sin(alfa)
#     pt=Point(x,y)
#     pt.draw(win)

#z.5
# x=400
# y=400
# pt=Point(x,y)
# pt.draw(win)
# alfa=0
# while 1:
#     # if randint(1,20)==1:
#     alfa=alfa+randint(-4,4)/10  #można zmieniać randint i bedą spirale
#     x=x+cos(alfa)
#     y=y+sin(alfa)
#     pt=Point(x,y)
#     pt.draw(win)
#     if x<=0: alfa=0
#     if x>=800: alfa=pi
#     if y<=0: alfa=pi/2
#     if y>=800: alfa=-pi/2


#z.7
x=400
y=400
pt=Point(x,y)
pt.draw(win)
dl=5
while 1:
    for i in range(dl):
        x=x+1
        pt = Point(x, y)
        pt.draw(win)
    for i in range(dl):
        y=y-1
        pt = Point(x, y)
        pt.draw(win)
    dl=dl+5
    for i in range(dl):
        x=x-1
        pt = Point(x, y)
        pt.draw(win)
    for i in range(dl):
        y=y+1
        pt = Point(x, y)
        pt.draw(win)
    dl=dl+5

win.getMouse()
win.close()