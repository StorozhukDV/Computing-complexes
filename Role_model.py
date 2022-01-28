import random, operator

print('Игра Role model')

def roll_dice(dice_type = 6): # 1
    # бросок кубика
    return random.randint(1, dice_type)
    
class Creature():
    
    def __init__(self, name, fraction, max_hp, power): # 2
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
        
    def do_action(self, unit_list): # 3
        # берем те элемнты из списка unit_list, для которых фракция не равна фракции объекта
        emeny = []
        for unit in unit_list:
            if self.fraction != unit.fraction:
                emeny.append(unit)
        # атакуем первого в списке врага       
        if not emeny:
            print('Net vragov')
        else:
            self.attack(target = emeny[0])
            
    def attack(self, target): # 4
        damage = roll_dice(self.power)
        print(f'{self.get_name()} deal {damage} damage to {target.get_name()}')
        # print (self.get_name() + ' deal' + str(damage) + ' damage to ' + target.get_name())
        target.get_damage(damage)
    
    def get_damage(self, count): # 5
        self.current_hp -= count
        if self.current_hp <= 0:
            self.is_defeat = True
            
    def heal(self, target):
        heal =


            
    def print_stars(self): # 6
        print(', '.join('%s: %s' % item for item in vars(self).items()))
            
    def get_name(self): # 7
        return self.name
    
class Human(Creature):
    def __init__(self, name, creature_fraction): # 8
        base_human_power = 10
        base_human_max_hp = 20
        Creature.__init__(self, name, creature_fraction, base_human_max_hp, base_human_power)
        self.luck = 10
        
    def get_name(self): # 9
        return 'human ' + self.name

class Monah(Human):
    def __init__(self, name, creature_fraction):
        base_human_power = 5
        base_human_max_hp = 15
        Creature.__init__(self, name, creature_fraction, base_human_max_hp, base_human_power)
        self.luck = 10

    def get_name(self):
        return 'monah ' + self.name

class Goblin(Creature):
    def __init__(self, name, creature_fraction): # 10
        base_goblin_power = 4
        base_goblin_max_hp = 10
        Creature.__init__(self, name, creature_fraction, base_goblin_max_hp, base_goblin_power)
        self.luck = 10
        
    def get_name(self): # 11
        return 'goblin ' + self.name
    
# вспомогательная функция

def remove_defeated(creature_list): # 12
    result_list = list(filter(lambda unit: not unit.is_defeat, creature_list))
    defeated_list = list(filter(lambda unit: unit.is_defeat, creature_list))
    if defeated_list:
        print(', '.join('%s' % unit.get_name() for unit in defeated_list) + ' defeated')
    return result_list

def check_battle_result(creature_list): # 13
    if not creature_list:
        return True
    first_fraction = creature_list[0].fraction
    for unit in creature_list:
        if first_fraction != unit.fraction:
            return False
        
    return True

# игра начинается отсюда

human_1 = Human('Boris', 'hero')
human_2 = Monah('Monax_Omar', 'hero')
unit_list = []
goblin_1 = Goblin('Klo-klo', 'evil')
goblin_2 = Goblin('Kwak', 'evil')
unit_list.append(goblin_1)
unit_list.append(goblin_2)
unit_list.append(human_1)
unit_list.append(human_2)

    
for unit in unit_list:
    unit.initiative = roll_dice()
    
unit_list.sort(key = operator.attrgetter('initiative'), reverse = True)

for unit in unit_list:
    unit.print_stars()
print()

is_battle_over = False
round_number = 1
max_round = 30
while not is_battle_over and round_number <= max_round:
    unit = unit_list.pop(0)
    unit.do_action(unit_list)
    unit_list.append(unit)
    unit_list = remove_defeated(unit_list)
    is_battle_over = check_battle_result(unit_list)
    round_number += 1
    
    print ()
    
if is_battle_over:
    print(', '.join('%s' % unit.get_name() for unit in unit_list) + ' win')



    

    
        
    
        
    
    
