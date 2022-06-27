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


################# Best Clear Solution ###################
"""
class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack

    @property
    def is_alive(self):
        return self.health > 0

    def hit(self, other):
        other.loss(self.attack)

    def damage(self, attack):
        return attack

    def loss(self, attack):
        self.health -= self.damage(attack)


class Knight(Warrior):
    def __init__(self):
        super().__init__(attack=7)


class Defender(Warrior):
    def __init__(self):
        super().__init__(health=60, attack=3)
        self.defense = 2

    def damage(self, attack):
        return max(0, attack - self.defense)


class Vampire(Warrior):
    def __init__(self):
        super().__init__(health=40, attack=4)
        self.vampirism = 50

    def hit(self, other):
        super().hit(other)
        self.health += other.damage(self.attack) * self.vampirism // 100


def fight(unit_1, unit_2):
    while 1:
        unit_1.hit(unit_2)
        if unit_2.health <= 0:
            return True
        unit_2.hit(unit_1)
        if unit_1.health <= 0:
            return False


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit_class, count):
        for _ in range(count):
            self.units.append(unit_class())

    @property
    def first_alive_unit(self):
        for unit in self.units:
            if unit.is_alive:
                return unit

    @property
    def is_alive(self):
        return self.first_alive_unit is not None


class Battle:
    @staticmethod
    def fight(army_1, army_2):
        while army_1.is_alive and army_2.is_alive:
            fight(army_1.first_alive_unit, army_2.first_alive_unit)
        return army_1.is_alive
        
"""