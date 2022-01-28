a,b,c = map(int,input().split())
def tuple1(a,b,c):
    tuple2 = tuple(range(a, b, c))
    return tuple2
Zadanie = tuple1(a,b,c)
print(Zadanie)

def list1(Zadanie):
    list =[]
    for i in range(len(Zadanie)):
        g=Zadanie[i]%2
        if g == 0:
            list.append(Zadanie[i]*3)
        elif g == 1:
            list.append(Zadanie[i]/3)
    return list
zadanie2 = list1(Zadanie)
print(zadanie2)

m = set()
for i in range(len(Zadanie)):
    m.add(Zadanie[i])
print(m)