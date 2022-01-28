a=[]
b=[]
II=['Ia','Ib','Ic']

with open('KZcfg.cfg','r') as f:
    c=f.readlines()        #все строки в листах

n=c[7].split(',')          #забираем строку с количеством сток и превращаем ее в лист
n=int(n[1])                    #количество строк
print('Кол-во строк -',n)

s=c[1].split(',')          #забираем строку с количеством сигналов
s=int(s[0])                     #количество сигналов
print('Кол-во строк -',s)

for i in range(2,s+2):
    confI=c[i].split(',')
    a.append(float(confI[5]))  #коэфф а для I
    b.append(float(confI[6]))  #коэфф b для I

for i in range(s):
    print('Коэффициенты a и b для', II[i] ,'соответственно равны',a[i],'и',b[i])

import matplotlib.pyplot as mpl
import math


Ia=[]
Ib=[]
Ic=[]
vremya=[]

with open('KZdat.dat','r') as f:
    for row in f.readlines():
        row=row.rstrip().split(',')
        Ia.append(a[0]*(float(row[2]))+b[0])
        Ib.append(a[1]*(float(row[3]))+b[1])
        Ic.append(a[2]*(float(row[4]))+b[2])
        vremya.append(int(row[1])/1000) #v ms
import sqlite3
connection=sqlite3.connect('mylr.db')


cursor=connection.cursor()
print('Go sqlite')


cursor.execute('select * from measure ')
result = cursor.fetchall()
print(result)


for i in vremya:   #вносим объем времени
    cursor.execute('insert into time (time_value) values (?)', (i,))


for i in range(len(Ic)):
    x = Ia[i]
    z = Ib[i]
    v = Ic[i]
    cursor.execute('insert into Values1 (Ia,Ib,Ic,timeID) values (?,?,?,?)', (x,z,v,i+1))

cursor.execute('''select Ia from Values1 where ValueID < 80000 ''')
Iat = cursor.fetchall()
cursor.execute('''select Ib from Values1 where ValueID < 80000''')
Ibt = cursor.fetchall()
cursor.execute('''select Ic from Values1 where ValueID < 80000''')
Ict = cursor.fetchall()
cursor.execute('''select time_value from time where timeID < 80000''')
vremyat = cursor.fetchall()

 #фиксация изменений
connection.commit()
connection.close()

mpl.figure('grafiki')
mpl.subplot(211)
mpl.grid(True)
mpl.axis([0, 400000, -0.5, 0.5])
lines = [None, None, None]
lines[0], lines[1], lines[2] = mpl.plot(vremyat, Iat, '-', vremyat, Ibt, '-', vremyat, Ict, '-')
mpl.legend(lines, ['Ia', 'Ib', 'Ic'], loc='lower right')
mpl.show()