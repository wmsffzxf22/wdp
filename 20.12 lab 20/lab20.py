from graphics import *
from math import *

def zakres(a,b,ile): #(0,1,4) -> [0, 0.333, 0.666, 1]
    l=[] #(-2,2,3) -> [-2,0,2]
    d = (b - a)/(ile-1)
    for i in range(ile):
        l.append(a+i*d)
    return l

# win = GraphWin('Window',800,800)
# win.setCoords(-5,-5,5,5)

#z.1
# ox=Line(Point(-5,0),Point(5,0))
# oy=Line(Point(0,-5),Point(0,5))
# ox.draw(win)
# oy.draw(win)
#
# x = zakres(-5,5,10000)
# y=[]
# for a in x:
#     y.append(sin(a))
#
# for i in range(len(x)-1): #połączyć (x[i],y[i]) z (x[i+1],y[y+1]
#     p1=Point(x[i],y[i])
#     p2=Point(x[i+1],y[i+1])
#     l=Line(p1,p2)
#     l.draw(win)

# win.getMouse()
# win.close()

#z.2
# while 1:
#     s=input('Polecenie:')
#     if s=='stop': break
#     s='print('+s+')'
#     exec(s)

#z.3
# x=zakres(-5,5,100)
# y=[]
# s=input('Podaj funkcje ze zmienną t: ')
# for t in x:
#     z='y.append('+s+')'
#     exec(z)
#
# win = GraphWin('Window',800,800)
# win.setCoords(-5,-5,5,5)
#
# ox=Line(Point(-5,0),Point(5,0))
# oy=Line(Point(0,-5),Point(0,5))
# ox.draw(win)
# oy.draw(win)
#
# for i in range(len(x)-1):
#     p1=Point(x[i],y[i])
#     p2=Point(x[i+1],y[i+1])
#     l=Line(p1,p2)
#     l.draw(win)
#
# win.getMouse()
# win.close()

#z.4
# s=input('Podaj funkcje ze zmienną t: ')
# xmin=float(input('xmin: '))
# xmax=float(input('xmax: '))
# x=zakres(xmin,xmax,100)
# y=[]
#
# for t in x:
#     z='y.append('+s+')'
#     exec(z)
#
# ymin=min(y)
# ymax=max(y)
#
# win = GraphWin('Window',800,800)
# win.setCoords(xmin,ymin,xmax,ymax)
#
# ox=Line(Point(xmin,0),Point(xmax,0))
# oy=Line(Point(0,ymin),Point(0,ymax))
# ox.draw(win)
# oy.draw(win)
#
# for i in range(len(x)-1):
#     p1=Point(x[i],y[i])
#     p2=Point(x[i+1],y[i+1])
#     l=Line(p1,p2)
#     l.draw(win)
#
# win.getMouse()
# win.close()

#z.5
# def rys():
#     s=input('Podaj funkcje ze zmienną t: ')
#     xmin=float(input('xmin: '))
#     xmax=float(input('xmax: '))
#     x=zakres(xmin,xmax,100)
#     y=[]
#
#     for t in x:
#         z='y.append('+s+')'
#         exec(z)
#
#     ymin=min(y)
#     ymax=max(y)
#
#     win = GraphWin('Window',800,800)
#     win.setCoords(xmin,ymin,xmax,ymax)
#
#     ox=Line(Point(xmin,0),Point(xmax,0))
#     oy=Line(Point(0,ymin),Point(0,ymax))
#     ox.draw(win)
#     oy.draw(win)
#
#     for i in range(len(x)-1):
#         p1=Point(x[i],y[i])
#         p2=Point(x[i+1],y[i+1])
#         l=Line(p1,p2)
#         l.draw(win)
#
#     win.getMouse()
#     win.close()
#
# while 1:
#     s=input('Polecenie:')
#     if s=='stop': break
#     if s=='rysuj':
#         rys()
#     s='print('+s+')'
#     exec(s)

#z.6

win = GraphWin('Window',800,800)
win.setCoords(-10,-10,10,10)

ox=Line(Point(-10,0),Point(10,0))
oy=Line(Point(0,-10),Point(0,10))
ox.draw(win)
oy.draw(win)

t = zakres(-10,10,100)
x=[]
y=[]
for a in t:
    x.append(a-sin(a))
for a in t:
    y.append(1-cos(a)) #samo cos i sin to kółko

for i in range(len(x)-1): #połączyć (x[i],y[i]) z (x[i+1],y[y+1]
    p1=Point(x[i],y[i])
    p2=Point(x[i+1],y[i+1])
    l=Line(p1,p2)
    l.draw(win)

win.getMouse()
win.close()
