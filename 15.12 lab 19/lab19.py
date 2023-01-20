from graphics import *
from time import sleep
from random import randint
win = GraphWin('Window',500,500)
win.setBackground('white')

#z.1
# win.setCoords(0,0,10,10)
# l=[Point(1,1), Point(2,8), Point(6,9), Point(8,5), Point(7,2)]
# poly=Polygon(l)
# poly.setFill('red')
# poly.draw(win)

#z.2
# win.setCoords(0,0,10,10)
#
# for i in range(11):
#     l=Line(Point(i,0), Point(i,10))
#     l.draw(win)
#     l=Line(Point(0,i), Point(10,i))
#     l.draw(win)

def pionek(x,y,kolor):
    c=Circle(Point(x-0.5,y-0.5),0.5)
    c.setFill(kolor)
    c.draw(win)

# pionek(2,1,'red')

# kol=['red','blue']
# z=0
# while 1:
    #jeden pionek
    # x = randint(1, 10)
    # y = randint(1, 10)
    # pionek(x, y, 'blue')

    #dwa randomowe pionki
    # pionek(randint(1,10),randint(1,10),'blue')
    # pionek(randint(1,10),randint(1,10),'red')

    #dwa randomowe pionki chyba lepiej
    # z=(z+1)%2
    # x = randint(1, 10)
    # y = randint(1, 10)
    # pionek(x, y, kol[z])
    # sleep(0.1)

#z.3
# win.setCoords(0,0,10,10)
#
# for i in range(11):
#     l=Line(Point(i,0), Point(i,10))
#     l.draw(win)
#     l=Line(Point(0,i), Point(10,i))
#     l.draw(win)

# t=[[1,4,55],[30,16,14]]
# print(t[1][2])

# t=[[0 for i in range(4)] for j in range(3)]
# print(t)

# t=[[i for i in range(4)] for j in range(3)]
# print(t)

# t=[[randint(-1,1) for i in range(4)] for j in range(3)]
# print(t)
# print(t[0][1])


# t=[[randint(-1,1) for i in range(10)] for j in range(10)]
# print(t)
#
# for i in range(11):
#     for j in range(11):
#         if t[i-1][j-1]==1:
#             pionek(i,j,'red')
#         if t[i-1][j-1]==-1:
#             pionek(i,j,'blue')

#z.4
win.setCoords(0,0,10,10)

for i in range(11):
    l=Line(Point(i,0), Point(i,10))
    l.draw(win)
    l=Line(Point(0,i), Point(10,i))
    l.draw(win)

# pt=win.getMouse()
# print(pt)
# x=pt.getX() #wybiera x-sową współrzędną punktu
# print(x)

kol=['red','blue']
z=0
t=[[0 for i in range(10)] for i in range(10)]
while 1:
    z = (z + 1) % 2
    while 1:
        pt=win.getMouse()
        print(pt)
        x=int(pt.getX())
        y=int(pt.getY())
        if t[int(x)][int(y)]==0:
            break
    # pionek(x+1,y+1,'red') #jeden punkt czerwony
    pionek(x + 1, y + 1, kol[z])  #randomowe dwa kolory
    if z==0:
        t[int(x)][int(y)]=1; bk = 1
    else:
        t[int(x)][int(y)]=-1; bk = -1
    print(t)

    #z.5
    #poziomo
    li=1
    xx=x-1
    yy=y
    while xx>=0 and t[xx][y]==bk:
        li=li+1; xx=xx-1
    xx=x+1
    while xx<=9 and t[xx][y]==bk:
        li=li+1; xx=xx+1

    if li>=5: print('KONIEC'); break

    #pionowo
    li=1
    xx=x
    yy=y-1
    while yy>=0 and t[x][yy]==bk:
        li=li+1; yy=yy-1
    yy=y+1
    while yy<=9 and t[x][yy]==bk:
        li=li+1; yy=yy+1
    if li >= 5: print('KONIEC'); break

win.getMouse()
win.close()