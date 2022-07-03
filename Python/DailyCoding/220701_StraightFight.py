class Warrior:
    def __init__(self, health=50, attack=5):
        self.initHealth = health
        self.health = health
        self.attack = attack
        self.is_alive = True

    def hit(self, unit2, unit3=None):
        # Attack
        damage = 0
        if type(unit2) == Defender:
            if type(self) != Lancer:
                damage = (self.attack - unit2.defense) if (self.attack - unit2.defense) > 0 else 0
                # if damage > unit2.health: damage = unit2.health
                unit2.health -= damage
                unit2.is_alive = unit2.isAlive()
                self.recover(damage)
            else:
                damage = (self.attack - unit2.defense) if (self.attack - unit2.defense) > 0 else 0
                # if damage > unit2.health: damage = unit2.health
                unit2.health -= damage
                unit2.is_alive = unit2.isAlive()
                self.recover(damage)
                if unit3 != None:
                    if type(unit3) == Defender:
                        damage = (damage - unit3.defense) if (damage - unit3.defense) > 0 else 0
                        # if damage > unit3.health: damage = unit3.health 
                    unit3.health -= damage*0.5
                    unit3.is_alive = unit3.isAlive()
                    self.recover(damage)
        else:
            if type(self) != Lancer:
                damage = self.attack
                # if damage > unit2.health: damage = unit2.health
                unit2.health -= damage
                unit2.is_alive = unit2.isAlive()
                self.recover(damage)
            else:
                damage = self.attack
                # if damage > unit2.health: damage = unit2.health
                unit2.health -= damage
                unit2.is_alive = unit2.isAlive()
                self.recover(damage)
                if unit3 != None:
                    if type(unit3) == Defender:
                        damage = (damage - unit3.defense) if (damage - unit3.defense) > 0 else 0
                        # if damage > unit3.health: damage = unit3.health
                    unit3.health -= damage*0.5
                    unit3.is_alive = unit3.isAlive()
                    self.recover(damage)
        return

    def recover(self, damage):
        if type(self) == Vampire:
            if (self.health + damage*self.vampirism//100) <= self.initHealth:
                self.health += (damage*self.vampirism)//100
            else:
                self.health = self.initHealth

    def isAlive(self):
        return True if self.health > 0 else False

class Rookie(Warrior):
    def __init__(self, health = 50, attack = 1):
        super().__init__(health, attack)
    #     # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.health = 50
    #     self.attack = 1

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

class Healer(Warrior):
    def __init__(self, health=50, attack=0, heals=2):
        super().__init__(health, attack)
        self.heals = heals

    def heal(self, other):
        if other.health + self.heals <= other.initHealth:
            other.health = other.health + self.heals
        else:
            other.health = other.initHealth
        
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
        elif unit == Knight:
            for i in range(num):
                self.units.append(Knight())
        elif unit == Defender:
            for i in range(num):
                self.units.append(Defender())
        elif unit == Vampire:
            for i in range(num):
                self.units.append(Vampire())
        elif unit == Lancer:
            for i in range(num):
                self.units.append(Lancer())
        elif unit == Rookie:
            for i in range(num):
                self.units.append(Rookie())
        elif unit == Healer:
            for i in range(num):
                self.units.append(Healer())


class Battle():
    def __init__(self):
        self.isWin = False

    def fight(self, army1, army2):
        while (army1.units != [] and army2.units != []):
            unit1, unit2 = army1.units.pop(), army2.units.pop()
            unit0, unit3 = None, None
            # Combat with two units
            if type(unit1) != Lancer and type(unit2) != Lancer and \
                army1.units != [] and type(army1.units[-1]) != Healer and \
                army2.units != [] and type(army2.units[-1]) != Healer:
                fight(unit1, unit2)
                self.recover(unit1, army1, unit2, army2)
            # Combat with more than two units
            else:
                round = "left"
                while unit1.is_alive and unit2.is_alive:
                    if round == "left":
                        if type(unit1) == Lancer and army2.units != []:
                            unit3 = army2.units.pop()
                            unit1.hit(unit2, unit3)
                            # Heal
                            if army1.units != [] and type(army1.units[-1]) == Healer:
                                army1.units[-1].heal(unit1)
                            if unit3.is_alive: army2.units.append(unit3)
                            round = "right"
                        else:
                            unit1.hit(unit2)
                            if army1.units != [] and type(army1.units[-1]) == Healer:
                                army1.units[-1].heal(unit1)
                            round = "right"
                    elif round == "right":
                        if type(unit2) == Lancer and army1.units != []:
                            unit0 = army1.units.pop()
                            unit2.hit(unit1, unit0)
                            if army2.units != [] and type(army2.units[-1]) == Healer:
                                army2.units[-1].heal(unit1)
                            if unit0.is_alive: army1.units.append(unit0)
                            round = "left"
                        else:
                            unit2.hit(unit1)
                            if army2.units != [] and type(army2.units[-1]) == Healer:
                                army2.units[-1].heal(unit1)
                            round = "left"

                if unit1.is_alive: army1.units.append(unit1)
                elif unit2.is_alive: army2.units.append(unit2)

        return army1.units != []

    def straight_fight(self, army1, army2):
        while army1.units != [] and army2.units != []:
            minNum = min(len(army1.units), len(army2.units))
            deadList1 = []
            deadList2 = []

            # Fight respectively
            for i in range(minNum):
                unit1 = army1.units[i]
                unit2 = army2.units[i]
                fight(unit1, unit2)

            # Recover units to the army
            for i in range(minNum):
                unit1 = army1.units[i]
                unit2 = army2.units[i]
                if not unit1.is_alive: deadList1.append(unit1)
                if not unit2.is_alive: deadList2.append(unit2)
            
            # Remove dead units in the deadList1
            self.removeDeadUnits(army1, deadList1)
            self.removeDeadUnits(army2, deadList2)
                
            # Print out
            print("army1: ", *[unit.health for unit in army1.units])
            print("army2: ", *[unit.health for unit in army2.units])
            print()
        
        return army1.units != []

    def recover(self, unit1, army1, unit2, army2):
        if unit1.is_alive: army1.units.append(unit1)
        elif unit2.is_alive: army2.units.append(unit2)

    def removeDeadUnits(self, army, deadList):
        for i in range(len(deadList)):
            army.units.remove(deadList.pop())

army_1 = Army()
army_2 = Army()
army_1.add_units(Lancer, 7)
army_1.add_units(Vampire, 3)
army_1.add_units(Healer, 1)
army_1.add_units(Warrior, 4)
army_1.add_units(Healer, 1)
army_1.add_units(Defender, 2)
army_2.add_units(Warrior, 4)
army_2.add_units(Defender, 4)
army_2.add_units(Healer, 1)
army_2.add_units(Vampire, 6)
army_2.add_units(Lancer, 4)
battle = Battle()
print(battle.straight_fight(army_1, army_2))

# lanc = Lancer()
# warr = Warrior()
# print(fight(lanc, warr))
# print("Lancer: %d, Warrior: %d" % (lanc.health, warr.health))

# lanc = Lancer()
# defn = Defender()
# print(fight(lanc, defn))
# print("Lancer: %d, Defender: %d" % (lanc.health, defn.health))

# vamp = Vampire()
# defn = Defender()
# print(fight(vamp, defn))
# print("Vampire: %d, Defender: %d" % (vamp.health, defn.health))

# vamp1 = Vampire()
# vamp2 = Vampire()
# print(fight(vamp1, vamp2))
# print("Vampire1: %d, Vampire2: %d" % (vamp1.health, vamp2.health))

# warr = Warrior()
# vamp = Vampire()
# print(fight(warr, vamp))
# print("Warrior: %d, Vampire: %d" % (warr.health, vamp.health))

# defn = Defender()
# lanc = Lancer()
# print(fight(defn, lanc))
# print("Defender: %d, Lancer: %d" % (defn.health, lanc.health))

# army_1 = Army()
# army_2 = Army()
# army_1.add_units(Lancer, 7)
# army_1.add_units(Vampire, 3)
# army_1.add_units(Healer, 1)
# army_1.add_units(Warrior, 4)
# army_1.add_units(Healer, 1)
# army_1.add_units(Defender, 2)
# army_2.add_units(Lancer, 4)
# army_2.add_units(Warrior, 4)
# army_2.add_units(Defender, 4)
# army_2.add_units(Healer, 1)
# army_2.add_units(Vampire, 6)
# battle = Battle()
# print(battle.straight_fight(army_1, army_2))