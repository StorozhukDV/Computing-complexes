import random as r
import operator as o


def roll_dice(dice_type=6):
    return r.randint(1, dice_type)


class Creature():

    def __init__(self, name, max_hp, fraction, power):
        self.name = name
        self.max_hp = max_hp
        self.fraction = fraction
        self.power = power
        self.current_hp = max_hp
        self.is_defeat = False
        self.initiative = 0
        self.blinded = False
        self.fired = False
        self.fire_count = 0

    def get_name(self):
        return self.name

    def attack(self, target):
        damage = roll_dice(self.power)
        if self.fire_count > 0:
            self.get_damage(1)
            print(f'{self.get_name()} get 1 damaged coz he had been fire')
            self.fire_count -= 1
        else:
            self.fired = False

        if self.blinded == False and self.is_defeat == False:
            print(f'{self.get_name()} deal {damage} damaged to {target.get_name()}')
            target.get_damage(damage)
        elif self.blinded == True and self.is_defeat == False:
            print(f'{self.get_name()} missed to {target.get_name()} coz he was blind')
            self.blinded = False

    def get_damage(self, damage):
        friend = []
        for unit in unit_list:
            if self.fraction == unit.fraction:
                friend.append(unit)
        self.current_hp -= damage
        if self.current_hp <= 0:
            self.is_defeat = True
            self.heal(friend[0])

    def print_stats(self):
        print(','.join('%s:%s' % item for item in vars(self).items()))
        print('\n')

    def do_action(self, unit_list):
        enemy = []
        for unit in unit_list:
            if self.fraction != unit.fraction:
                enemy.append(unit)

        if not enemy:
            print('нет врагов')
        else:
            self.attack(r.choice(enemy))

    def get_effect(self, effect):
        if effect == 'blind':
            self.blinded = True
        elif effect == 'fired':
            self.fired = True
            self.fire_count = 2

    def heal(self, target):
        print(f'{self.get_name()} heal {self.power} to {target.get_name()}')
        target.current_hp += self.power
        if target.current_hp > target.max_hp:
            target.current_hp = target.max_hp


unit_list = []
Vasya = Creature('Vasya', 10, 'human', 3)
Kolya = Creature('Kolya', 9, 'human', 4)
Peter = Creature('Peter', 6, 'goblin', 1)
unit_list.append(Vasya)
unit_list.append(Kolya)
Peter.do_action(unit_list)



class Human(Creature):
    def __init__(self, name, create_fraction):
        base_human_power = 10
        base_human_max_hp = 40
        Creature.__init__(self, name, base_human_max_hp, create_fraction, base_human_power)
        self.luck = 10

    def get_name(self):
        return 'human ' + self.name

    def attack(self, target):
        damage = roll_dice(self.power) + self.luck
        if self.fire_count > 0:
            self.get_damage(1)
            print(f'{self.get_name()} get 1 damaged coz he had been fire')
            self.fire_count -= 1
        else:
            self.fired = False

        if self.blinded == False and self.is_defeat == False:
            print(f'{self.get_name()} deal {damage} damaged to {target.get_name()}')
            target.get_damage(damage)
        elif self.blinded == True and self.is_defeat == False:
            print(f'{self.get_name()} missed to {target.get_name()} coz he was blind')
            self.blinded = False


class Goblin(Creature):
    def __init__(self, name, create_fraction):
        base_goblin_power = 17
        base_goblin_max_hp = 25
        Creature.__init__(self, name, base_goblin_max_hp, create_fraction, base_goblin_power)

    def get_name(self):
        return 'goblin ' + self.name


class Dwarf(Creature):
    def __init__(self, name, create_fraction):
        base_dwarf_power = 4
        base_dwarf_max_hp = 35
        Creature.__init__(self, name, base_dwarf_max_hp, create_fraction, base_dwarf_power)

    def get_name(self):
        return 'dwarf ' + self.name

    def attack(self, target):
        damage = roll_dice(self.power)
        if self.fire_count > 0:
            self.get_damage(1)
            print(f'{self.get_name()} get 1 damaged coz he had been fire')
            self.fire_count -= 1
        else:
            self.fired = False

        if self.blinded == False and self.is_defeat == False:
            print(f'{self.get_name()} deal {damage} damaged to {target.get_name()}')
            target.get_damage(damage)
            self.power += round(self.power / 2)
        elif self.blinded == True and self.is_defeat == False:
            print(f'{self.get_name()} missed to {target.get_name()} coz he was blind')
            self.blinded = False


class Priest(Creature):
    def __init__(self, name, create_fraction):
        base_priest_power = 2
        base_priest_max_hp = 35
        Creature.__init__(self, name, base_priest_max_hp, create_fraction, base_priest_power)
        self.count = 0

    def get_name(self):
        return 'priest ' + self.name

    def do_action(self, unit_list):
        enemy = []
        for unit in unit_list:
            if self.fraction != unit.fraction:
                enemy.append(unit)
        if not enemy:
            print('нет врагов')
        else:
            if self.propusk == False:
                if self.count == 2:
                    self.magic(r.choice(enemy))
                else:
                    self.attack(unit_list, target=emeny[0])
                    self.count += 1
            else:
                self.propusk = False
                print('PROPUSKAET HOD', self.get_name())



    def magic(self, target):
        if self.fire_count > 0:
            self.get_damage(1)
            print(f'{self.get_name()} get 1 damaged coz he had been fire')
            self.fire_count -= 1
        else:
            self.fired = False
        if self.is_defeat == False:
            print(f'{self.get_name()} blinded {target.get_name()} for one round')
            target.get_effect('blind')
            self.count = 0


class Mage(Creature):
    def __init__(self, name, create_fraction):
        base_mage_power = 2
        base_mage_max_hp = 35
        Creature.__init__(self, name, base_mage_max_hp, create_fraction, base_mage_power)

    def get_name(self):
        return 'mage ' + self.name

    def do_action(self, unit_list):
        enemy = []
        for unit in unit_list:
            if self.fraction != unit.fraction:
                enemy.append(unit)
        if not enemy:
            print('нет врагов')
        else:
            self.magic(r.choice(enemy))

    def magic(self, target):
        damage = roll_dice(self.power)
        if self.fire_count > 0:
            self.get_damage(1)
            print(f'{self.get_name()} get 1 damaged coz he had been fire')
            self.fire_count -= 1
        else:
            self.fired = False
        if self.blinded == False and self.is_defeat == False:
            x = roll_dice(2)
            if x == 2:
                print(f'{self.get_name()} fired {target.get_name()} for two rounds')
                target.get_effect('fired')
            print(f'{self.get_name()} deal {damage} damaged to {target.get_name()}')
            target.get_damage(damage)
        elif self.blinded == True and self.is_defeat == False:
            print(f'{self.get_name()} missed to {target.get_name()} coz he was blind')
            self.blinded = False


def remove_defeated(creature_list):
    result_list = list(filter(lambda unit: not unit.is_defeat, creature_list))
    defeated_list = list(filter(lambda unit: unit.is_defeat, creature_list))
    if defeated_list:
        print(','.join('%s' % unit.get_name() for unit in defeated_list) + ' defeated')

    return result_list


def check_battle_results(creature_list):
    if not creature_list: return True
    first_fraction = creature_list[0].fraction
    for unit in creature_list:
        if first_fraction != unit.fraction:
            return False
    return True


def hp_check(unit_list):
    light_hp = 0
    dark_hp = 0
    for i in unit_list:
        if i.fraction == 'light':
            light_hp += i.current_hp
        else:
            dark_hp += i.current_hp
    if light_hp == dark_hp:
        print(f'Draw because light_hp= {light_hp} vs dark_hp= {dark_hp}\n')
    elif light_hp > dark_hp:
        print(f'Fraction Light win because light_hp= {light_hp} vs dark_hp= {dark_hp}\n')
        return 1
    else:
        print(f'Fraction Dark win because light_hp= {light_hp} vs dark_hp= {dark_hp}\n')
        return 2


war_number = 1
max_war = 5

light_win = 0
dark_win = 0

for unit in unit_list:
    unit.print_stats()

while war_number <= max_war:
    unit_list = []
    check = 0

    goblin1 = Goblin('klo-klo', 'dark')
    goblin2 = Goblin('Kwak', 'dark')
    dwarf1 = Dwarf('Android', 'dark')
    mage1 = Mage('Anto', 'dark')
    human1 = Human('Boris', 'light')
    dwarf2 = Dwarf('Magor', 'light')
    priest1 = Priest('Euclid', 'light')

    unit_list.append(goblin1)
    unit_list.append(goblin2)
    unit_list.append(dwarf1)
    unit_list.append(mage1)
    unit_list.append(human1)
    unit_list.append(dwarf2)
    unit_list.append(priest1)

    for unit in unit_list:
        unit.initiative = roll_dice()

    unit_list.sort(key=o.attrgetter('initiative'), reverse=True)

    is_battle_over = False
    round_number = 1
    max_round = 25

    while not is_battle_over and round_number <= max_round:
        unit = unit_list.pop(0)
        unit.do_action(unit_list)
        unit_list.append(unit)
        unit_list = remove_defeated(unit_list)
        is_battle_over = check_battle_results(unit_list)
        round_number += 1
    print('\n')

    if is_battle_over:
        print(','.join('%s' % unit.get_name() for unit in unit_list) + ' win')
        if not unit_list:
            print('Battle draw')
        elif unit_list[0].fraction == 'light':
            light_win += 1
        else:
            dark_win += 1
    else:
        check = hp_check(unit_list)
        if check == 1:
            light_win += 1
        elif check == 2:
            dark_win += 1

    print('Fraction LIGHT wins', light_win, 'times.')
    print('Fraction DARK wins', dark_win, 'times.')
    print('The battle ends.\n')
    war_number += 1

print('The war is over.\n')

if light_win > dark_win:
    print('Fraction LIGHT wins the war!')
elif light_win < dark_win:
    print('Fraction DARK wins the war!')
else:
    print('Draw!')