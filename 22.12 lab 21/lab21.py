from graphics import *
from random import randint

# win=GraphWin('',500,500)

#z.1
# c=Circle(Point(250,250),100)
# k=color_rgb(120,120,120)
# print(k) #ff0000
# #(100,0,0), (100,100,0), (0,150,150), (120,120,120)
# c.setFill(k)
# c.draw(win)


#z.2

# im=Image(Point(250,250), 'snapG.gif') #najwyżej trzeba ścieżke dostępu
# w=im.getWidth()
# h=im.getHeight()
# # print(w,h)
# win=GraphWin('',w,h)
# im=Image(Point(w//2,h//2), 'snapG.gif') # punkt ma być środkiem obrazu dlatego dzielimy przez 2
# im.draw(win)

#z.3

# im=Image(Point(250,250), 'snapG.gif')
# w=im.getWidth()
# h=im.getHeight()
# # print(w,h)
# win=GraphWin('',w,h)
# im=Image(Point(w//2,h//2), 'snapG.gif')
# im.draw(win)

#konkretny piksel
# kol=im.getPixel(100,100)
# print(kol) #rgb
# k=color_rgb(kol[0],kol[1],kol[2])
# print(k)
# c=Circle(Point(100,100),40)
# c.setFill(k)
# c.draw(win)

#dowolny
# x=200; y=200
# kol=im.getPixel(x,y)
# print(kol) #rgb
# k=color_rgb(kol[0],kol[1],kol[2])
# print(k)
# c=Circle(Point(x,y),40)
# c.setFill(k)
# c.draw(win)

#użytkownik wybiera punkt
# c=Circle(Point(0,0),1)
# c.draw(win)
# while 1:
#     pt=win.getMouse()
#     c.undraw()
#     x=int(pt.getX()) ; y=int(pt.getY())
#     kol=im.getPixel(x,y)
#     print(kol) #rgb
#     k=color_rgb(kol[0],kol[1],kol[2])
#     print(k)
#     c=Circle(Point(x,y),40)
#     c.setFill(k)
#     c.draw(win)

#z.4
# im=Image(Point(250,250), 'snapG.gif')
# w=im.getWidth()
# h=im.getHeight()
# win=GraphWin('',w,h)
# im=Image(Point(w//2,h//2), 'snapG.gif')
# im.draw(win)

# x=100; y=100
# for i in range(20):
#     for j in range(20):
#         im.setPixel(x+i,y+j,color_rgb(255,0,0))

# for x in range(w):
#     for y in range(h):
#         kol=im.getPixel(x,y)
#         im.setPixel(x,y,color_rgb(0,kol[1],kol[2])) #usuwamy czerwony
#         # im.setPixel(x, y, color_rgb(kol[0], 0, kol[2])) #usuwamy zielony
#         # im.setPixel(x, y, color_rgb(0, 0, kol[2])) #zostawiamy sam niebieski
#     if x%20==0:
#         win.update()
# im.save('2snap.gif')

#z.5
# im=Image(Point(250,250), 'snapG.gif')
# w=im.getWidth()
# h=im.getHeight()
# win=GraphWin('',w,h)
# im=Image(Point(w//2,h//2), 'snapG.gif')
# im.draw(win)

# for x in range(w):
#     for y in range(h):
#         kol = im.getPixel(x, y)
#         for i in range(3):
#             kol[i]=min(max(kol[i]+randint(-100,100),0),255)
#         im.setPixel(x, y, color_rgb(kol[0], kol[1], kol[2]))
#     if x % 20 == 0:
#         win.update()
# im.save('3Snap.png') #trzeba dać png, bo w gif jest ograniczona liczba kolorów

#z.6
im=Image(Point(250,250), 'snapG.gif')
w=im.getWidth()
h=im.getHeight()
win=GraphWin('',w,h)
im=Image(Point(w//2,h//2), 'snapG.gif')
im.draw(win)

# for xx in range(0,w,10):
#     for yy in range(0,h,10):
#         k=[0,0,0] #kolejno: suma czerwieni, suma zielenie, suma niebieskiego, zaczynamy uśredniać kolore ze 10x10 punktów
#         for x in range(10):
#             for y in range(10):
#                 # wspolrzedne punktu (xx+x,yy+y)
#                 kol=im.getPixel(xx+x,yy+y)
#                 for i in range(3):
#                     k[i]=k[i]+kol[i]
#         for i in range(3):
#             k[i]=k[i]//100
#         col=color_rgb(k[0],k[1],k[2]) # w col - uśredniony kolor
#         for x in range(10):
#             for y in range(10):
#                 im.setPixel(xx+x,yy+y,col)
#     win.update()


#usunięcie szumu
# for x in range(1,w-1):
#     for y in range(1,h-1):
#         k=im.getPixel(x,y)
#         k2=im.getPixel(x-1,y)  # lewy sasiad
#         for i in range(3):
#             k[i]=k[i]+k2[i]
#         k2 = im.getPixel(x+1, y)
#         for i in range(3):
#             k[i] = k[i] + k2[i]
#         k2 = im.getPixel(x, y-1)
#         for i in range(3):
#             k[i] = k[i] + k2[i]
#         k2 = im.getPixel(x, y + 1)
#         for i in range(3):
#             k[i] = k[i] + k2[i]
#         for i in range(3):
#             k[i] = k[i]//5
#         im.setPixel(x,y,color_rgb(k[0],k[1],k[2]))
#     if x%20==0:
#         win.update()

#tłumienie szumu???
t=[[[0,0,0] for i in range(h)] for j in range(w)]
for x in range(2,w-2):
    for y in range(2,h-2):
        k=[0,0,0]
        for i in range(x-2,x+3):
            for j in range(y-2,y+3):
                kol = im.getPixel(i, j)
                for ii in range(3):
                    k[ii]=k[ii]+kol[ii]

        for i in range(3):
            k[i] = k[i]//25
            t[x][y][i]=k[i];
        #im.setPixel(x,y,color_rgb(k[0],k[1],k[2]))

print('TUTAJ')
for x in range(2,w-2):
    for y in range(2,h-2):
        im.setPixel(x, y, color_rgb(t[x][y][0],t[x][y][1],t[x][y][2]))
    if x%10==0: win.update()

win.getMouse()
win.close()