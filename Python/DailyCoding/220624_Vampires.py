class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack
        self.is_alive = True

class Knight(Warrior):
    def __init__(self, health=50, attack=7):
        super().__init__(health, attack)

class Defender(Warrior):
    def __init__(self, health=60, attack=3, defense=2):
        super().__init__(health, attack)
        self.defense = defense

class Vampire(Warrior):
    def __init__(self, health=40, attack=4, vampirism=50):
        super().__init__(health, attack)
        self.vampirism = vampirism

def fight(unit_1, unit_2):
    round = "left"
    while unit_1.is_alive and unit_2.is_alive:
        # Unit_1 Attack
        if round == "left":
            # Attack
            damage = 0
            if type(unit_2) == Defender:
                damage = unit_1.attack - unit_2.defense
                if damage > 0: unit_2.health -= damage
            else:
                damage = unit_1.attack
                unit_2.health -= damage

            # Recover
            if type(unit_1) == Vampire:
                if damage > 0:
                    unit_1.health += damage*unit_1.vampirism/100

            unit_2.is_alive = True if unit_2.health > 0 else False
            round = "right"
        # Unit_2 Attack
        elif round == "right":
            # Attack
            damage = 0
            if type(unit_1) == Defender:
                damage = unit_2.attack - unit_1.defense
                if damage > 0: unit_1.health -= damage
            else:
                damage = unit_2.attack
                unit_1.health -= damage

            # Recover
            if type(unit_2) == Vampire:
                if damage > 0:
                    unit_2.health += damage*unit_2.vampirism/100
                    
            unit_1.is_alive = True if unit_1.health > 0 else False
            round = "left"

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
        elif unit == Vampire:
            for i in range(num):
                self.units.append(Vampire())

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

battle = Battle()

army_3 = Army()
army_3.add_units(Warrior, 1)
army_3.add_units(Defender, 4)

army_4 = Army()
army_4.add_units(Vampire, 3)
army_4.add_units(Warrior, 2)

print(battle.fight(army_3, army_4))
