import random, operator

print('Игра Role model')


def roll_dice(dice_type=6):  # 1
    # бросок кубика
    return random.randint(1, dice_type)


class Creature():

    def __init__(self, name, fraction, max_hp, power):  # 2
        # конструктор класса, вызывается при создании экземпляра класса
        # запрещает создавать экземпляр класса без указания обязательных аргументов
        # аргумент self указывает на экземпляр класса, из которого вызывается метод
        self.name = name
        self.max_hp = max_hp
        self.fraction = fraction
        self.power = power
        self.current_hp = self.max_hp
        self.initiative = 6
        self.is_defeat = False
        self.propusk = False

    def do_action(self, unit_list):  # 3
        # берем те элемнты из списка unit_list, для которых фракция не равна фракции объекта
        emeny = []
        for unit in unit_list:
            if self.fraction != unit.fraction:
                emeny.append(unit)
        # атакуем первого в списке врага
        if not emeny:
            print('Net vragov')
        else:
            if self.propusk == False:
                self.attack(unit_list, target=emeny[0])
            else:
                self.propusk = False
                print('PROPUSKAET HOD',self.get_name())


    def attack(self,unit_list, target):  # 4
        damage = roll_dice(self.power)
        print(f'{self.get_name()} deal {damage} damage to {target.get_name()}')
        # print (self.get_name() + ' deal' + str(damage) + ' damage to ' + target.get_name())
        friends = []
        for unit in unit_list:
            if self.fraction == unit.fraction:
                friends.append(unit)
        target.get_damage(damage, targetp=friends[0])

    def get_prop(self):
        self.propusk = True

    def get_damage(self, count, targetp):  # 5
        self.current_hp -= count
        if self.current_hp <= 0:
            self.is_defeat = True
            targetp.get_prop()

            emeny = []
            for unit in unit_list:
                if self.fraction != unit.fraction:
                    emeny.append(unit)
            self.get_uron(emeny)

    def get_uron(self,emeny):
        target = emeny[0]
        print('Текущее хп',target.current_hp, target.get_name())
        for unit in emeny:
            unit.current_hp -= 1
        print('Текущее хп после урона',target.current_hp, target.get_name())



    def lechenie(self, target, count):
        print(f'{self.get_name()} deal {count} heal to {target.get_name()}')
        # print (self.get_name() + ' deal' + str(damage) + ' damage to ' + target.get_name())
        target.get_heal(count)

    def get_heal(self, count):
        self.current_hp += count
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp

    def print_stars(self):  # 6
        print(', '.join('%s: %s' % item for item in vars(self).items()))

    def get_name(self):  # 7
        return self.name


class Human(Creature):
    def __init__(self, name, creature_fraction):  # 8
        base_human_power = 34
        base_human_max_hp = 30
        Creature.__init__(self, name, creature_fraction, base_human_max_hp, base_human_power)
        self.luck = 10


    def get_name(self):  # 9
        return self.name
    def attack(self, target, unit_list):  # 4
        damage = roll_dice(self.power)+ self.luck
        print(f'{self.get_name()} deal {damage} damage to {target.get_name()}')
        # print (self.get_name() + ' deal' + str(damage) + ' damage to ' + target.get_name())
        friends = []
        for unit in unit_list:
            if self.fraction == unit.fraction:
                friends.append(unit)
        target.get_damage(damage, targetp=friends[0])


class Monah(Creature):
    def __init__(self, name, creature_fraction):
        base_monah_power = 5
        base_monah_max_hp = 15
        Creature.__init__(self, name, creature_fraction, base_monah_max_hp, base_monah_power)
        self.sila_lechenie = 8

    def get_name(self):
        return 'monah ' + self.name

    def do_action(self, unit_list):  # 3
        # берем те элемнты из списка unit_list, для которых фракция не равна фракции объекта
        self.lechenie(self, count=self.sila_lechenie)
        emeny = []
        friends = []
        for unit in unit_list:
            if self.fraction != unit.fraction:
                emeny.append(unit)
            else:
                friends.append(unit)
        # атакуем первого в списке врага
        if not emeny:
            print('Net vragov')
        if not friends:
            print('Net druzey ryadom')
        if emeny:
            self.attack(unit_list, target=emeny[0])
        if friends:
            self.lechenie(target=friends[0], count=self.sila_lechenie)




class Goblin(Creature):
    def __init__(self, name, creature_fraction):  # 10
        base_goblin_power = 4
        base_goblin_max_hp = 33
        Creature.__init__(self, name, creature_fraction, base_goblin_max_hp, base_goblin_power)
        self.luck = 10

    def get_name(self):  # 11
        return 'goblin ' + self.name


# вспомогательная функция

def remove_defeated(creature_list):  # 12
    result_list = list(filter(lambda unit: not unit.is_defeat, creature_list))
    defeated_list = list(filter(lambda unit: unit.is_defeat, creature_list))
    if defeated_list:
        print(', '.join('%s' % unit.get_name() for unit in defeated_list) + ' defeated')
    return result_list




def check_battle_result(creature_list):  # 13
    if not creature_list:
        return True
    first_fraction = creature_list[0].fraction
    for unit in creature_list:
        if first_fraction != unit.fraction:
            return False

    return True


# игра начинается отсюда

war_number = 1
max_war = 5

Pobeda_geroev = 0
Pobeda_goblins = 0

while war_number <= max_war:
    unit_list = []
    human_1 = Human('Boris ', 'hero')
    human_2 = Human('Vasiliy ', 'hero')
    monah_1 = Monah('Danya ', 'hero')

    goblin_1 = Goblin('Klo Klo', 'evil')
    goblin_2 = Goblin('Tup put', 'evil')
    goblin_3 = Goblin('Dup Dup ', 'evil')
    unit_list.append(goblin_1)
    unit_list.append(goblin_2)
    unit_list.append(human_1)
    unit_list.append(human_2)
    unit_list.append(monah_1)
    unit_list.append(goblin_3)

    for unit in unit_list:
        unit.initiative = roll_dice()

    unit_list.sort(key=operator.attrgetter('initiative'), reverse=True)

    for unit in unit_list:
        unit.print_stars()
    print()



    is_battle_over = False
    round_number = 1
    max_round = 6
    while not is_battle_over and round_number <= max_round:
        unit = unit_list.pop(0)
        unit.do_action(unit_list)
        unit_list.append(unit)
        unit_list = remove_defeated(unit_list)
        is_battle_over = check_battle_result(unit_list)
        round_number += 1

        print()
    Summa_hp_heroes = 0
    Summa_hp_goblins = 0
    if is_battle_over:
        print(', '.join('%s' % unit.get_name() for unit in unit_list) + ' win')
    else:
        for i in unit_list:
            if i.fraction == 'hero':
                Summa_hp_heroes += i.current_hp
            else:
                Summa_hp_goblins += i.current_hp
        if Summa_hp_heroes > Summa_hp_goblins:
            print(Summa_hp_goblins, Summa_hp_heroes)
            print('Герои победили,потому что сумма ХП героев больше ', Summa_hp_heroes,'чем у гоблинов', Summa_hp_goblins)
            Pobeda_geroev += 1
        elif Summa_hp_heroes < Summa_hp_goblins:
            print(Summa_hp_goblins, Summa_hp_heroes)
            print('Победили гоблины, потому что Сумма ХП гоблинов больше', Summa_hp_goblins,'чем у героев', Summa_hp_heroes)
            Pobeda_goblins += 1
        else:
            print('НИЧЬЯ','Победили гоблины, потому что Сумма ХП гоблинов больше', Summa_hp_goblins,'чем у героев', Summa_hp_heroes)

    war_number += 1

if Pobeda_geroev > Pobeda_goblins:
    print('Война окончена, победили герои,со счетом',Pobeda_geroev,'против',Pobeda_goblins,' гоблинсов')
elif Pobeda_geroev < Pobeda_goblins:
    print('Война окончена, победили гоблинсы,со счетом', Pobeda_goblins, 'против', Pobeda_geroev, ' героев')
else:
    print('НИЧЬЯ')