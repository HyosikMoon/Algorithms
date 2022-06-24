class Warrior:
    def __init__(self, health=50, attack=5, defense=0):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.is_alive = True

class Knight(Warrior):
    def __init__(self, health=50, attack=7, defense=0):
        super().__init__(health, attack, defense)

class Defender(Warrior):
    def __init__(self, health=60, attack=3, defense=2):
        super().__init__(health, attack, defense)

def fight(unit_1, unit_2):
    round = 0
    while unit_1.is_alive and unit_2.is_alive:
        if round % 2 == 0:
            if unit_1.attack - unit_2.defense > 0:
                unit_2.health -= unit_1.attack - unit_2.defense
            unit_2.is_alive = True if unit_2.health > 0 else False
            round += 1
        else:
            if unit_2.attack - unit_1.defense > 0:
                unit_1.health -= unit_2.attack - unit_1.defense
            unit_1.is_alive = True if unit_1.health > 0 else False
            round += 1
    return True if unit_1.is_alive else False

class Army():
    def __init__(self):
        self.units = []

    def add_units(self, unit, num):
        if unit == Warrior:
            for i in range(num):
                self.units.append(Warrior())
        elif unit == Knight:
            for i in range(num):
                self.units.append(Knight())
        elif unit == Defender:
            for i in range(num):
                self.units.append(Defender())

class Battle():
    def __init__(self):
        self.isWin = False

    def fight(self, army1, army2):
        round = 'left'
        while (army1.units != [] and army2.units != []):
            if round == 'left':
                unit1, unit2 = army1.units.pop(), army2.units.pop()
                fight(unit1, unit2)
                if unit1.is_alive:
                    army1.units.append(unit1)
                elif unit2.is_alive:
                    army2.units.append(unit2)
                    round = 'right'
            elif round == 'right':
                unit1, unit2 = army1.units.pop(), army2.units.pop()
                fight(unit1, unit2)
                if unit1.is_alive:
                    army1.units.append(unit1)
                    round = 'left'
                elif unit2.is_alive:
                    army2.units.append(unit2)
        
        return True if army1.units != [] else False