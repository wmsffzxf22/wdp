from graphics import *
from random import randint

class Guzik(Rectangle):
    def __init__(self, p1, p2, kol='red'):
        super().__init__(p1, p2)
        self.setFill(kol)
        self.pushed = False

    def addtext(self, tx, win):
        pt = self.getCenter()
        t = Text(pt,tx)
        t.draw(win)

    def ispushed(self, pt):
        x = pt.getX()
        y = pt.getY()
        pt1 = self.getP1()
        pt2 = self.getP2()
        xx = pt1.getX(); xxx = pt2.getX()
        x1 = min(xx, xxx); x2 = max(xx, xxx)
        yy = pt1.getY(); yyy = pt2.getY()
        y1 = min(yy, yyy); y2 = max(yy, yyy)
        if x1 <= x <= x2 and y1 <= y <= y2: self.pushed = True


win = GraphWin('', 500, 500)

g1 = Guzik(Point(20, 20), Point(60, 40))
g1.draw(win)
# print(g1.getP1())
# print(g1.getP2())
g1.addtext('1', win)

g2 = Guzik(Point(120, 20), Point(160, 40), 'orange')
g2.draw(win)
g2.addtext('2', win)

g3 = Guzik(Point(220, 20), Point(260,40), 'lightgreen')
g3.draw(win)
g3.addtext('+', win)

g4 = Guzik(Point(320, 20), Point(360,40), 'lightblue')
g4.draw(win)
g4.addtext('=', win)


t=Text(Point(250,250),'0')
t.draw(win)
z = ''
az = 0
while 1:
    pt = win.checkMouse()
    if pt != None:
        g1.ispushed(pt)
        g2.ispushed(pt)
        g3.ispushed(pt)
        g4.ispushed(pt)
    if g1.pushed:
        z = z + '1'
        t.undraw()
        t = Text(Point(250, 250), z)
        t.draw(win)
    if g2.pushed:
        z = z + '2'
        t.undraw()
        t = Text(Point(250, 250), z)
        t.draw(win)
    if g3.pushed:
        z = z + '+'
        t.undraw()
        t = Text(Point(250, 250), z)
        t.draw(win)
    if g4.pushed:
        w = 'az='+z
        exec(w)
        t.undraw()
        t = Text(Point(250, 250), az)
        t.draw(win)
        z = ''
    g1.pushed = False
    g2.pushed = False
    g3.pushed = False
    g4.pushed = False


#zad 2.3
# x=250; y=250
# sk=1
# while 1:
#     pt = win.checkMouse()
#     if pt != None:
#         print(pt)
#         x = pt.getX()
#         y = pt.getY()
#     k = win.checkKey()
#     if k == 'q':
#         break
#     if k == 'a':
#         sk += 1
#     win.plot(x, y, 'black')
#     r = randint(1,4)
#     if r == 1:
#         x += sk
#     if r == 2:
#         x -= sk
#     if r == 3:
#         y += sk
#     if r == 4:
#         y -= sk


win.getMouse()
win.close()
