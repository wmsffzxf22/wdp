from graphics import *
from time import sleep
from math import *

#rzucanie czerwonej kulki z grawitacją
# win=GraphWin('',600,600)
# win.setBackground('white')
# win.setCoords(-10,-10,10,10)

# l=Line(Point(-10,-5),Point(10,-5))
# l.setWidth(5)
# l.draw(win)
# x=-8
# y=-5
# c=Circle(Point(x,y),0.2)
# c.setFill('red')
# c.draw(win)
#
# # vx=0.3
# # vy=1.5
# pt=win.getMouse()
# xx=pt.getX()
# yy=pt.getY()
# vx=xx+8
# vy=yy+5
# dt=0.1 #sprawdzamy po jakim czasie sie wyswietla jak zmienia sie trasa kółka
# ay=-0.1
# while 1:
#     x=x+dt*vx
#     y=y+dt*vy
#     c = Circle(Point(x, y), 0.2)
#     c.setFill('red')
#     c.draw(win)
#     vy=vy+dt*ay
#     if y<-5.1: break
#     sleep(0.01)
#     c.undraw()
#
#
# win.getMouse()
# win.close()


#słoneczko w centrum
# win=GraphWin('',600,600)
# win.setBackground('white')
# win.setCoords(-10,-10,10,10)
# c=Circle(Point(0,0),0.3)
# c.setFill('yellow')
# c.draw(win)
# x=5
# y=0
# z=Circle(Point(5,0),0.2)
# z.setFill('blue')
# # z=Point(x,y)
# z.draw(win)
# vx=0
# vy=0.5
# dt=0.1
# while 1:
#     ax=-x/sqrt(x**2+y**2)**3
#     ay=-y/sqrt(x**2+y**2)**3
#     vx = vx + dt * ax
#     vy = vy + dt * ay
#     x=x+dt*vx
#     y=y+dt*vy
#     z = Circle(Point(x, y), 0.2)
#     z.setFill('blue')
#     # z = Point(x,y)
#     z.draw(win)

# win.getMouse()
# win.close()

#idk co XD

win=GraphWin('',600,600)
win.setBackground('white')
win.setCoords(-10,-10,10,10)
xs=0; ys=0; vsx=0; vsy=-0.3
c=Circle(Point(xs,ys),0.3)
c.setFill('yellow')
c.draw(win)
c.undraw()
x=5; y=0
z=Circle(Point(x,y),0.2)
z.setFill('blue')
#z=Point(x,y)
z.draw(win)
z.undraw()

vx=0;vy=0.3
dt=0.1
#win.getMouse()
while 1:
    ax=-(x-xs)/sqrt((x-xs)**2+(y-ys)**2)**3  #  sqrt(x**2+y**2)**3=sqrt(x**2+y**2) * (x**2+y**2)
    ay=-(y-ys)/sqrt((x-xs)**2+(y-ys)**2)**3
    asx=-(xs-x)/sqrt((x-xs)**2+(y-ys)**2)**3
    asy=-(ys-y)/sqrt((x-xs)**2+(y-ys)**2)**3
    vx = vx + dt * ax
    vy = vy + dt * ay
    vsx=vsx+dt*asx
    vsy=vsy+dt*asy
    x=x+dt*vx
    y=y+dt*vy
    xs=xs+dt*vsx
    ys=ys+dt*vsy
    z = Circle(Point(x, y), 0.2)
    z.setFill('blue')
    #z = Point(x, y)
    z.draw(win)
    c = Circle(Point(xs, ys), 0.3)
    c.setFill('yellow')
    c.draw(win)
    sleep(0.01)
    z.undraw()
    c.undraw()

win.getMouse()
win.close()

#idk jeszcze bardziej