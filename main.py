a,b,c = map(int,input().split())
def list1(a,b,c):
    list=[]
    for i in range(a,b,c):
      list.append(i)
    return list
Zadanie=list1(a,b,c)
print(Zadanie)

kol=0
m=set()
for i in range(len(Zadanie)):
    g=Zadanie[i]%2
    if g==0:
        m.add(Zadanie[i])
    elif g==1:
        kol+=1
print('количество нечетных элементов списка',kol)
print(m)
list2=list(m)
for i in range(len(m)):
    j=list2[i]
    Zadanie.append(j)
print(Zadanie)

for i in range(len(Zadanie)):
    m.add(Zadanie[i])
print(m)




