#z.1
# ntka=(1,'alfa', 5, 3.14)
# print(ntka[0],ntka[2],ntka[-1])
# print(ntka[1:])
# print(type(ntka))
# l=list(ntka)
# print(l)
# t2=tuple(l)
# print(t2)
# print(ntka+(1,2,3))
# print(ntka*2)
# print(len(ntka))
# t=(1,9.2,3)
# # print(max(ntka)) #nie działa bo są str
# print(max(t))

# t1=(1,9.2,3)
# l=list(t1)
# l[0]=100
# t2=tuple(l)
# print(t2)

#z.2
# sl={'Imię': 'Anna', 'Wiek': 30, 5:'Costam', (6,2): 32} #nie może być w środku listy
# print(sl)
# print(sl['Wiek'])
# print(sl[5])
# sl['ekstra']=999
# print(sl)
# print(type(sl))
# print(sl.keys())
# print(list(sl.keys()))
# print(sl.values())
# print(list(sl.values()))
# del sl['ekstra']
# print(sl)

# l1=['alfa', 5, 2] #klucze
# l2=[3, 'beta', 200] #wartości
#
# sl={}
# for i in range(len(l1)):
#     sl[l1[i]]=l2[i]
#
# print(sl)

#z.3
# def bezpowt(sl):
#     l=list(sl.values())
#     for i in range(len(l)):
#         for j in range(len(l)):
#             if i != j and l[i] == l[j]:
#                 return 0
#     return 1

def bezpowt(sl):
    l=list(sl.values())
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] == l[j]:
                return 1
    return 0

# sl1={'dwa':2, 3:'trzy',  'cztery':4}
# sl2={'dwa':2, 3:'trzy',  'cztery':2}
#
# print(bezpowt(sl1))
# print(bezpowt(sl2))  #jak powtórzenie to jeden

#z.4
def odwr(sl):
    #sprawdziamy czy są powtórzenia w wartościach, jak tak zwracamy 0
    if print(bezpowt(sl)) == 1: return 0
    sl2={}
    k=list(sl.keys())
    v=list(sl.values())
    for i in range(len(sl)):
        sl2[v[i]]=k[i]
    return sl2

# sl={'kot':'cat', 'dom':'house', 'mysz': 'mouse'}
# sl=odwr(sl)
# print(sl) #słownik na odwrót

#z.5
# sl={'kot':'cat', 'dom':'house', 'mysz': 'mouse'}
#w pliku  kot:cat; dom;house; ....

#for i in sl:
    # print(i, sl[i])

# fo = open('slownik.txt', 'w')
#
# for i in sl:
#   fo.write(i+':'+sl[i]+';')
#
# fo.close()

#z.6
# fo = open('slownik.txt', 'r')
# s=fo.read()
# print(s)
# fo.close()

# s='Ala ma kota'
# t='Ala ma kota;Drugie zdanie;I trzecie'
# l=s.split(' ')
# k=t.split(';')
# print(l)
# print(k)

fo = open('slownik.txt', 'r')
s=fo.read()
fo.close()

sl={}
l=s.split(';')
del l[-1]
for l2 in l:
    # print(l2)
    p=l2.split(':')
    print(p)
    sl[p[0]]=p[1]

print(sl)
