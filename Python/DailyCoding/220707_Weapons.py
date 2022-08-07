class Warrior:
    def __init__(self, health=50, attack=5, \
                    defense=None, vampirism=None, heal_power=None):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.vampirism = vampirism
        self.heal_power = heal_power
        self.initHealth = health
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
            if int(self.health + damage*self.vampirism//100) <= self.initHealth:
                self.health += int((damage*self.vampirism)//100)
            else:
                self.health = self.initHealth

    def isAlive(self):
        return True if self.health > 0 else False

    def equip_weapon(self, weapon_name):
        if type(weapon_name) == Sword:
            self.setHealth(weapon_name)
            self.setAttack(weapon_name)
        elif type(weapon_name) == Shield:
            self.setHealth(weapon_name)
            self.setAttack(weapon_name)
            if (type(self) == Defender): self.setDefense(weapon_name)
        elif type(weapon_name) == GreatAxe:
            self.setHealth(weapon_name)
            self.setAttack(weapon_name)
            if (type(self) == Defender): self.setDefense(weapon_name)
            if (type(self) == Vampire): self.setVampirism(weapon_name)
        elif type(weapon_name) == Katana:
            self.setHealth(weapon_name)
            self.setAttack(weapon_name)
            if (type(self) == Defender): self.setDefense(weapon_name)
            if (type(self) == Vampire): self.setVampirism(weapon_name)
        elif type(weapon_name) == MagicWand:
            self.setHealth(weapon_name)
            self.setAttack(weapon_name)
            if (type(self) == Healer): self.setHealPower(weapon_name)
        elif type(weapon_name) == Weapon:
            self.setHealth(weapon_name)
            self.setAttack(weapon_name)
            self.setDefense(weapon_name)
            self.setVampirism(weapon_name)
            self.setHealPower(weapon_name)

        return
    
    def setHealth(self, weapon_name):
        if self.health + weapon_name.health > 0:
            self.health += weapon_name.health
            self.initHealth += weapon_name.health
        else: 
            self.health = 0
            self.initHealth = 0

    def setAttack(self, weapon_name):
        if self.attack + weapon_name.attack > 0:
            self.attack += weapon_name.attack
        else:
            self.attack = 0
    
    def setVampirism(self, weapon_name):
        if (self.vampirism != None and self.vampirism + weapon_name.vampirism > 0):
            self.vampirism += weapon_name.vampirism
        else:
            self.vampirism = 0
    
    def setDefense(self, weapon_name):
        if (self.defense != None and self.defense + weapon_name.defense > 0):
            self.defense += weapon_name.defense
        else:
            self.defense = 0

    def setHealPower(self, weapon_name):
        if (self.heal_power != None and self.heal_power + weapon_name.heal_power > 0):
            self.heal_power += weapon_name.heal_power
        else:
            self.heal_power = 0


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
        super().__init__(health, attack, defense)

class Vampire(Warrior):
    def __init__(self, health=40, attack=4, defense=None, vampirism=50):
        super().__init__(health, attack, defense, vampirism)

class Lancer(Warrior):
    def __init__(self, health=50, attack=6):
        super().__init__(health, attack)

class Healer(Warrior):
    def __init__(self, health=50, attack=0, defense=None, vampirism=None, heal_power=2):
        super().__init__(health, attack, defense, vampirism, heal_power)

    def heal(self, other):
        if other.health + self.heal_power <= other.initHealth:
            other.health = other.health + self.heal_power
        else:
            other.health = other.initHealth

class Warlord(Warrior):
    def __init__(self, health=100, attack=4, defense=2):
        super().__init__(health, attack, defense)


class Weapon:
    def __init__(self, health=None, attack=None, \
                defense=None, vampirism=None, heal_power=None):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.vampirism = vampirism
        self.heal_power = heal_power

class Sword(Weapon):
    def __init__(self, health=5, attack=2):
        super().__init__(health, attack)

class Shield(Weapon):
    def __init__(self, health=20, attack=-1, defense=2):
        super().__init__(health, attack, defense)

class GreatAxe(Weapon):
    def __init__(self, health=-15, attack=5, defense=-2, vampirism=10, heal_power=None):
        super().__init__(health, attack, defense, vampirism, heal_power)

class Katana(Weapon):
    def __init__(self, health=-20, attack=6, defense=-5, vampirism=50, heal_power=None):
        super().__init__(health, attack, defense, vampirism, heal_power)

class MagicWand(Weapon):
    def __init__(self, health=30, attack=3, defense=None, vampirism=None, heal_power=3):
        super().__init__(health, attack, defense, vampirism, heal_power)

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
        if Warlord not in self.units:
            for _ in range(num):
                self.units.append(unit())
        # if unit == Warrior:
        #     for i in range(num):
        #         self.units.append(Warrior())
        # elif unit == Knight:
        #     for i in range(num):
        #         self.units.append(Knight())
        # elif unit == Defender:
        #     for i in range(num):
        #         self.units.append(Defender())
        # elif unit == Vampire:
        #     for i in range(num):
        #         self.units.append(Vampire())
        # elif unit == Lancer:
        #     for i in range(num):
        #         self.units.append(Lancer())
        # elif unit == Rookie:
        #     for i in range(num):
        #         self.units.append(Rookie())
        # elif unit == Healer:
        #     for i in range(num):
        #         self.units.append(Healer())

    def move_units(self):
        for unit in self.units:
            if type(unit) == Warlord:
            # Locate Lancer at the first position
                print ("Warlord is in the unit")

                break

            # Locate healers at the following positions


class Battle():

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
        # Print out
        print("Before fight")
        print("army1: ", *[(str(type(unit)) + ' ' + str(unit.health) + ' |') for unit in army1.units])
        print("army2: ", *[(str(type(unit)) + ' ' + str(unit.health) + ' |') for unit in army2.units])
        print()
        
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
            print("army1: ", *[(str(type(unit)) + ' ' + str(unit.health) + ' |') for unit in army1.units])
            print("army2: ", *[(str(type(unit)) + ' ' + str(unit.health) + ' |') for unit in army2.units])
            print()
        
        return army1.units != []

    def recover(self, unit1, army1, unit2, army2):
        if unit1.is_alive: army1.units.append(unit1)
        elif unit2.is_alive: army2.units.append(unit2)

    def removeDeadUnits(self, army, deadList):
        for i in range(len(deadList)):
            army.units.remove(deadList.pop())



# ##################### TEST1 #######################

ronald = Warlord()
heimdall = Knight()

fight(heimdall, ronald) == False

my_army = Army()
my_army.add_units(Warlord, 1)
my_army.add_units(Warrior, 2)
my_army.add_units(Lancer, 2)
my_army.add_units(Healer, 2)

enemy_army = Army()
enemy_army.add_units(Warlord, 3)
enemy_army.add_units(Vampire, 1)
enemy_army.add_units(Healer, 2)
enemy_army.add_units(Knight, 2)

battle = Battle()
my_army.move_units()
print(battle.fight(my_army, enemy_army))