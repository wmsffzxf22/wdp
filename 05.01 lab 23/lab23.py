from graphics import *
from random import randint
from time import sleep

#mastermind
# win=GraphWin('',600,600)
#
# # t=Text(Point(300,300),'Jakieś zdanie na środku ekranu')
# # t.draw(win)
# # win.getMouse()
#
# kol=['red','green','blue','yellow','white','black']
# for i in range(6):
#     x=30+30*i
#     y=550
#     r=Rectangle(Point(x,y),Point(x+20,y+20))
#     r.setFill(kol[i])
#     r.draw(win)
#     t=Text(Point(x+10,y+35),str(i+1))
#     t.draw(win)
#
# l_komp=[randint(0,5) for i in range(4)]
#
# poz=0
# rzad=0
# l_gracz=[]
# while 1:
#     x=30+40*poz
#     y=30+40*rzad
#     k=win.getKey()
#     if k.isdigit() and 1<=int(k)<=6: #najpierw sprawdza pierwszy
#         c=Circle(Point(x,y),15)
#         c.setFill(kol[int(k)-1])
#         l_gracz.append(int(k)-1)
#         c.draw(win)
#         poz+=1  # zamiast poz = poz+1
#     if poz==4:
#         #print(l_gracz,l_komp)
#         w=0; b=0
#         lk=l_komp.copy()
#         for i in range(4):  # zliczanie pionków na właściwych miejsach
#             if l_gracz[i]==lk[i]: w+=1; l_gracz[i]=-1; lk[i]=-1
#         for i in range(4):  # zliczanie pionków na niewłaściwych miejscach
#             for j in range(4):
#                 if l_gracz[i]!=-1 and l_gracz[i]==lk[j]: b+=1; l_gracz[i]=-1; lk[j]=-1
#         t=Text(Point(x+100,y),'white='+str(w)+'    black='+str(b))
#         t.draw(win)
#         if w==4:
#             t=Text(Point(x,y+50),'Wygrales za '+str(rzad+1)+' razem!')
#             t.draw(win)
#             break
#         l_gracz=[]
#         rzad+=1
#         poz=0
#
# win.getMouse()
# win.close()

#gra w życie conwaya
win=GraphWin('',600,600)
mx=50
win.setCoords(0,0,mx,mx)
for i in range(mx+1):
    l=Line(Point(0,i),Point(mx,i))
    l.draw(win)
    l = Line(Point(i,0), Point(i,mx))
    l.draw(win)

def cl(x,y):
    c=Circle(Point(x+0.5,y+0.5),0.5)
    c.setFill('red')
    return c

def nbh(x,y):
    s=cells[x-1][y-1]+cells[x-1][y]+cells[x-1][y+1]
    s=s+cells[x][y-1]+cells[x][y+1]
    s=s+cells[x+1][y-1]+cells[x+1][y]+cells[x+1][y+1]
    return s

cell=[[0 for i in range(mx)] for i in range(mx)]
cells=[[0 for i in range(mx)] for i in range(mx)]

for i in range(20,30):
    cells[i][25]=1
    #cell(i,25)
    cell[i][25]=cl(i,25)
    cell[i][25].draw(win)

x=20; y=26
cells[x][y]=1
cell[x][y]=cl(x,y)
cell[x][y].draw(win)

sleep(1)

while 1:
    chgs=[]
    #sleep(0.1)
    for i in range(1,mx-1):
        for j in range(1,mx-1):
            if cells[i][j]==0 and nbh(i,j)==3: chgs.append((i,j,1))
            if cells[i][j]==1 and (nbh(i,j)<2 or nbh(i,j)>3): chgs.append((i,j,0))

    #print(chgs)

    for c in chgs:
        i=c[0]; j=c[1]
        if c[2]==0:
            cells[i][j]=0
            #cell(i,j,'white')
            cell[i][j].undraw()
            cell[i][j]=0
        if c[2]==1:
            cells[i][j]=1
            cell[i][j]=cl(i,j)
            cell[i][j].draw(win)


win.getMouse()
win.close()