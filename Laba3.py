a = []
b = []

with open('KZcfg.cfg', 'r') as f:
    c = f.readlines()

for i in range(2, 5):
    confI = c[i].split(',')
    a.append(float(confI[5]))  # коэфф а
    b.append(float(confI[6]))  # коэфф b
import matplotlib.pyplot as mpl

Ia = []
Ib = []
Ic = []
vremya = []

with open('KZdat.dat', 'r') as f:
    for row in f.readlines():
        row = row.rstrip().split(',')
        vremya.append(int(row[1]))
        Ia.append(a[0] * (float(row[2])) + b[0])
        Ib.append(a[1] * (float(row[3])) + b[1])
        Ic.append(a[2] * (float(row[4])) + b[2])



class CurrentGenerator:
    def __init__(self,Ic):
        self.source = []
        self.Ic = Ic
    def create1stLevel(self):
        self.tok1stLevel1 = (Ic)
        for i in self.tok1stLevel1:
            yield i

class CircuitBreaker:
    def __init__(self, name):
        self.name = name
        self.__state = False

    def turn_breaker_on(self):
        self.__state = True

    def turn_breaker_off(self):
        self.__state = False

    def get_state(self):
        return self.__state



class Izmeritel1:
    def __init__(self, name, cb, generator, x):
        self.name = name
        self.cb = cb
        self.generator = generator
        self.x = x


    def get_data(self):
        if self.cb.get_state():
            return next(self.generator)/self.x
        else:
            return 0


class difzash:
    def __init__(self, name, tt1, tt2, cb, ustavka1):
        self.stepName = name
        self.measurment1 = []
        self.measurment2 = []
        self.tt1 = tt1
        self.tt2 = tt2
        self.cb = cb
        self.ustavka1 = ustavka1
        self.cb1g = []
    def tick(self):
        self.measurment1.append(self.tt1.get_data())
        self.measurment2.append(self.tt2.get_data())
        if len(self.measurment1) > 20:
            self.measurment1.pop(0)
            self.measurment2.pop(0)
        if self.cb.get_state() == True:
            self.run()
            self.cb1g.append(1)
        else:
            self.cb1g.append(0)

    def run(self):
        i_sq1 = self.calc_sq(self.measurment1)
        i_sq2 = self.calc_sq(self.measurment2)
        print('Действующее значение периода на ВН %.2f' % (i_sq1))
        print('Действующее значение периода на НН %.2f' % (i_sq2))
        print('Действующее значение диф.тока %.2f' % (i_sq1 - i_sq2))

        if i_sq1 - i_sq2 > self.ustavka1:
            self.cb.turn_breaker_off()
            print('!!! Выключатель отключен !!!')

    def calc_sq(self, value):
        return sum(((m * m) ** (1 / 2)) / len(value) for m in value)  # sqrt(sum....)



cb1 = CircuitBreaker("CB1")
cb1.turn_breaker_on()


i=1

print(cb1.name)
current_generator=CurrentGenerator(Ic)


print('Синусоида номер 1')
current_generator.source = current_generator.create1stLevel()


tt1 = Izmeritel1("TT1", cb1, current_generator.source, 0.5 )
tt2 = Izmeritel1("TT1", cb1, current_generator.source, 10)
dzt1=difzash('dzt',tt1,tt2,cb1, 10)
print('Состояние выключателя', cb1.get_state())
print()
da=int(len(vremya)/2)
vremyazash = vremya
for i in range(da):
    vremyazash[i] = vremya[i]*4



for i in range(80000):
    dzt1.tick()

while cb1.get_state(): #пока выключатель работает
    dzt1.tick()
    print()

print('Состояние выключателя', cb1.get_state())
print()

mpl.figure('grafiki')
mpl.subplot(211)
mpl.grid(True)
mpl.axis([0, 4000000, -0.5, 0.5])
lines = [None, None, None, None]
lines[0], lines[1], lines[2], lines[3] = mpl.plot(vremya, Ia, '-', vremya, Ib, '-', vremya, Ic, '-', vremya, dzt1.cb1g, '-', )
mpl.legend(lines, ['Ia', 'Ib', 'Ic', 'Состояние выключателя'], loc='lower right')
mpl.show()