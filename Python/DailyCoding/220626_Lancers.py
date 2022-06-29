class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack
        self.is_alive = True

    def hit(self, unit2, unit3=None):
        # Attack
        damage = 0
        if type(unit2) == Defender:
            if type(self) != Lancer:
                damage = self.attack - unit2.defense if self.attack - unit2.defense > 0 else 0
                unit2.health -= damage
                unit2.is_alive = unit2.isAlive()
                self.recover(damage)
            else:
                damage = self.attack - unit2.defense if self.attack - unit2.defense > 0 else 0
                unit2.health -= damage
                unit2.is_alive = unit2.isAlive()
                self.recover(damage)
                if unit3 != None:
                    if type(unit3) == Defender:
                        damage = damage - unit3.defense if damage - unit3.defense > 0 else 0 
                    unit3.health -= damage*0.5
                    unit3.is_alive = unit3.isAlive()
                    self.recover(damage)
        else:
            if type(self) != Lancer:
                damage = self.attack
                unit2.health -= damage
                unit2.is_alive = unit2.isAlive()
                self.recover(damage)
            else:
                damage = self.attack
                unit2.health -= damage
                unit2.is_alive = unit2.isAlive()
                self.recover(damage)
                if unit3 != None:
                    if type(unit3) == Defender:
                        damage = damage - unit3.defense if damage - unit3.defense > 0 else 0
                    unit3.health -= damage*0.5
                    unit3.is_alive = unit3.isAlive()
                    self.recover(damage)
        return

    def recover(self, damage):
        if type(self) == Vampire:
            self.health += damage*self.vampirism/100

    def isAlive(self):
        return True if self.health > 0 else False

class Rookie(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.health = 50
        self.attack = 1

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

class Lancer(Warrior):
    def __init__(self, health=50, attack=6):
        super().__init__(health, attack)

# @staticmethod
def fight(unit1, unit2):
    round = "left"
    while unit1.is_alive and unit2.is_alive:
        if round == "left":
            unit1.hit(unit2)
            round = "right"
        elif round == "right":
            unit2.hit(unit1)
            round = "left"
    return unit1.is_alive

class Army():
    def __init__(self):
        self.units = []

    def add_units(self, unit, num):
        if unit == Warrior:
            for i in range(num):
                self.units.append(Warrior())
                # self.units = [Warrior()] + self.units
        elif unit == Knight:
            for i in range(num):
                self.units.append(Knight())
                # self.units = [Knight()] + self.units
        elif unit == Defender:
            for i in range(num):
                self.units.append(Defender())
                # self.units = [Defender()] + self.units
        elif unit == Vampire:
            for i in range(num):
                self.units.append(Vampire())
                # self.units = [Vampire()] + self.units
        elif unit == Lancer:
            for i in range(num):
                self.units.append(Lancer())
                # self.units = [Lancer()] + self.units
        elif unit == Rookie:
            for i in range(num):
                self.units.append(Rookie())


class Battle():
    def __init__(self):
        self.isWin = False

    def fight(self, army1, army2):
        while (army1.units != [] and army2.units != []):
            unit1, unit2 = army1.units.pop(), army2.units.pop()
            unit0, unit3 = None, None
            if type(unit1) != Lancer and type(unit2) != Lancer:
                fight(unit1, unit2)
                self.recover(unit1, army1, unit2, army2)
            else:
                round = "left"
                while unit1.is_alive and unit2.is_alive:
                    if round == "left":
                        if type(unit1) == Lancer and army2.units != []:
                            unit3 = army2.units.pop()
                            unit1.hit(unit2, unit3)
                            if unit3.is_alive: army2.units.append(unit3)
                            round = "right"
                        else:
                            unit1.hit(unit2)
                            round = "right"
                    elif round == "right":
                        if type(unit2) == Lancer and army1.units != []:
                            unit0 = army1.units.pop()
                            unit2.hit(unit1, unit0)
                            if unit0.is_alive: army1.units.append(unit0)
                            round = "left"
                        else:
                            unit2.hit(unit1)
                            round = "left"

                if unit1.is_alive: army1.units.append(unit1)
                elif unit2.is_alive: army2.units.append(unit2)

        return True if army1.units != [] else False

    def recover(self, unit1, army1, unit2, army2):
        if unit1.is_alive: army1.units.append(unit1)
        elif unit2.is_alive: army2.units.append(unit2)

# battle = Battle()

# army_3 = Army()
# army_3.add_units(Knight, 2)
# army_3.add_units(Warrior, 1)

# army_4 = Army()
# army_4.add_units(Knight, 1)
# army_4.add_units(Warrior, 2)

# print(battle.fight(army_3, army_4))

# chuck = Warrior()
# bruce = Warrior()
# print(fight(chuck, bruce))

# rog = Warrior()
# lancelot = Defender()
# print(fight(lancelot, rog))

# my_army = Army()
# my_army.add_units(Defender, 2)
# my_army.add_units(Vampire, 2)
# my_army.add_units(Lancer, 4)
# my_army.add_units(Warrior, 1)

# enemy_army = Army()
# enemy_army.add_units(Warrior, 2)
# enemy_army.add_units(Lancer, 2)
# enemy_army.add_units(Defender, 2)
# enemy_army.add_units(Vampire, 3)
# battle = Battle()
# print(battle.fight(my_army, enemy_army))

# army_1 = Army()
# army_2 = Army()
# army_1.add_units(Lancer, 7)
# army_1.add_units(Vampire, 3)
# army_1.add_units(Warrior, 4)
# army_1.add_units(Defender, 2)
# army_2.add_units(Warrior, 4)
# army_2.add_units(Defender, 4)
# army_2.add_units(Vampire, 6)
# army_2.add_units(Lancer, 4)
# battle = Battle()
# print(battle.fight(army_1, army_2))

unit_1 = Defender()
unit_2 = Rookie()
fight(unit_1, unit_2)
print(unit_1.health)