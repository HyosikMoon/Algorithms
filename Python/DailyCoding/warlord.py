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
        if unit2.defense != None and unit2.defense > 0:
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
                    if unit3.defense != None and unit3.defense > 0:
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
                    if unit3.defense != None and unit3.defense > 0:
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
            self.setDefense(weapon_name)
        elif type(weapon_name) == GreatAxe:
            self.setHealth(weapon_name)
            self.setAttack(weapon_name)
            self.setDefense(weapon_name)
            self.setVampirism(weapon_name)
        elif type(weapon_name) == Katana:
            self.setHealth(weapon_name)
            self.setAttack(weapon_name)
            self.setDefense(weapon_name)
            self.setVampirism(weapon_name)
        elif type(weapon_name) == MagicWand:
            self.setHealth(weapon_name)
            self.setAttack(weapon_name)
            self.setHealPower(weapon_name)
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
        self.warlord = False
        self.lancer = False
        self.healer = False
        self.moveUnits = False

    def add_units(self, unit, num):
        if unit == Warlord and self.warlord == False:
            self.units.append(unit())
            self.warlord = True
        if unit != Warlord:
            for _ in range(num):
                self.units.append(unit())
                if unit == Lancer: self.lancer = True
                if unit == Healer: self.healer = True

    def move_units(self):
        self.moveUnits = True
        # Locate Warlord at the end (index -1)
        for i, unit in enumerate(self.units):
            if type(unit) == Warlord and len(self.units) > 1:
                self.units[i:-1], self.units[-1] = self.units[i+1:], self.units[i]
                break
        
        warrior_exist = False
        if self.lancer: # Locate Lancer at the first position
            lancer_position = 0
            for i, unit in enumerate(self.units):
                if type(unit) == Lancer and len(self.units) > lancer_position+1:
                    self.units[lancer_position], self.units[lancer_position+1:i+1] = unit, self.units[lancer_position:i]
                    if len(self.units) > lancer_position + 1: lancer_position += 1
                    warrior_exist = True
        else: # If there is no Lancer, then locate a warrior at the last position
            for i, unit in enumerate(self.units):
                if type(unit) != Warlord and type(unit) != Healer:
                    self.units[0], self.units[i] = unit, self.units[0]
                    warrior_exist = True
                    break
            
            # # if there is no warrior except for Warlord, then locate Warlord in the first position
            # if no_warrior == True and type((self.units[-1]) == Warlord):
            #     self.units[0], self.units[-1] = (self.units[-1]), self.units[0]
            
        # Locate Healer before the last position
        if self.healer:
            healer_position = 1
            for i, unit in enumerate(self.units):
                if type(unit) == Healer and warrior_exist and len(self.units) > 1:
                    self.units[healer_position], self.units[i] = unit, self.units[healer_position]
                    if len(self.units) > healer_position+1: healer_position += 1
        

class Battle():
    def fight(self, army1, army2):
        while (army1.units != [] and army2.units != []):
            self.reverseUnits(army1, army2)
            unit1, unit2 = army1.units.pop(), army2.units.pop()
            unit0, unit3 = None, None
            # Combat with two units
            if type(unit1) != Lancer and type(unit2) != Lancer and \
                army1.units != [] and type(army1.units[-1]) != Healer and \
                army2.units != [] and type(army2.units[-1]) != Healer:
                fight(unit1, unit2)
                self.recover(unit1, army1, unit2, army2)
                # Rearrange the by Warlord if a combat is finished 
                self.reverseUnits(army1, army2)
                self.rearrange(army1, army2)
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
                                army2.units[-1].heal(unit2)
                            if unit0.is_alive: army1.units.append(unit0)
                            round = "left"
                        else:
                            unit2.hit(unit1)
                            if army2.units != [] and type(army2.units[-1]) == Healer:
                                army2.units[-1].heal(unit2)
                            round = "left"

                self.recover(unit1, army1, unit2, army2)

                # Rearrange after the combat is finished by Warlord
                self.reverseUnits(army1, army2)
                self.rearrange(army1, army2)
            # print("army1: ", army1.units, "unit0 health: ", army1.units[0].health)
            # print("army2: ",army2.units,  "unit0 health: ", army2.units[0].health)

        return army1.units != []

    def rearrange(self, army1, army2):
        # Regrrange if Warlord is alive
        army1_types = set([type(unit) for unit in army1.units])
        army2_types = set([type(unit) for unit in army2.units])
        if Warlord in army1_types: army1.move_units()
        if Warlord in army2_types: army2.move_units()

    def reverseUnits(self, army1, army2=None):
        army1.units = list(reversed(army1.units))
        if army2 != None: army2.units = list(reversed(army2.units))

    def straight_fight(self, army1, army2):
        # Print out
        # print("Before fight")
        # print("army1: ", *[(str(type(unit)) + ' ' + str(unit.health) + ' |') for unit in army1.units])
        # print("army2: ", *[(str(type(unit)) + ' ' + str(unit.health) + ' |') for unit in army2.units])
        # print()

        # if army1.moveUnits: self.reverseUnits(army1)
        # if army2.moveUnits: self.reverseUnits(army2)

        # Print out
        print("After move_units()")
        print("army1: ", *[(unit.__class__.__name__ + ' h' + str(unit.health) + 
                            '|a' + str(unit.attack) + '|d' + str(unit.defense) + '|') for unit in army1.units])
        print("army2: ", *[(unit.__class__.__name__ + ' h' + str(unit.health) + 
                            '|a' + str(unit.attack) + '|d' + str(unit.defense) + '|') for unit in army2.units])
        print()

        while army1.units != [] and army2.units != []:
            minNum = min(len(army1.units), len(army2.units))
            deadList1 = []
            deadList2 = []

            for i in range(minNum):
                unit1 = army1.units[i]
                unit2 = army2.units[i]
                fight(unit1, unit2)
            for i in range(minNum):
                unit1 = army1.units[i]
                unit2 = army2.units[i]
                if not unit1.is_alive: deadList1.append(unit1)
                if not unit2.is_alive: deadList2.append(unit2)

            # Remove dead units in the deadList1
            self.removeDeadUnits(army1, deadList1)
            self.removeDeadUnits(army2, deadList2)
                
            # Print out
            print("After fight")
            print("army1: ", *[(unit.__class__.__name__ + ' h' + str(unit.health) + 
                                '|a' + str(unit.attack) + '|d' + str(unit.defense) + '|') for unit in army1.units])
            print("army2: ", *[(unit.__class__.__name__ + ' h' + str(unit.health) + 
                                '|a' + str(unit.attack) + '|d' + str(unit.defense) + '|') for unit in army2.units])
            print()
        
        # Print out
        print("Final")
        print("army1: ", *[(unit.__class__.__name__ + ' h' + str(unit.health) + 
                            '|a' + str(unit.attack) + '|d' + str(unit.defense) + '|') for unit in army1.units])
        print("army2: ", *[(unit.__class__.__name__ + ' h' + str(unit.health) + 
                            '|a' + str(unit.attack) + '|d' + str(unit.defense) + '|') for unit in army2.units])
        print()
        return army1.units != []

    def recover(self, unit1, army1, unit2, army2):
        if unit1.is_alive: army1.units.append(unit1)
        elif unit2.is_alive: army2.units.append(unit2)

    def removeDeadUnits(self, army, deadList):
        for i in range(len(deadList)):
            army.units.remove(deadList.pop())
        # else:
        #     # we should remove units from the index -1
        #     self.reverseUnits(army)
        #     for i in range(len(deadList)):
        #         army.units.remove(deadList.pop())
        #     army.move_units()
        #     self.reverseUnits(army)



# ##################### TEST1 #######################
# import sys
# # import weapons
# # print('Hum:', sys.modules[__name__])

# ronald = Warlord()/
# heimdall = Knight()

# fight(heimdall, ronald) == False

# my_army = Army()
# my_army.add_units(Warlord, 1)
# my_army.add_units(Warrior, 2)
# my_army.add_units(Lancer, 2)
# my_army.add_units(Healer, 2)
# my_army.move_units()

# enemy_army = Army()
# enemy_army.add_units(Warlord, 3)
# enemy_army.add_units(Vampire, 1)
# enemy_army.add_units(Healer, 2)
# enemy_army.add_units(Knight, 2)
# enemy_army.move_units()

# print(enemy_army.units)

# ##################### TEST2 #######################

# army_1 = Army()
# army_2 = Army()
# army_1.add_units(Warrior, 2)
# army_1.add_units(Lancer, 2)
# army_1.add_units(Defender, 1)
# army_1.add_units(Warlord, 3)
# army_2.add_units(Warlord, 2)
# army_2.add_units(Vampire, 1)
# army_2.add_units(Healer, 5)
# army_2.add_units(Knight, 2)
# army_1.move_units()
# army_2.move_units()
# # print(army_1.units)
# # print(army_2.units)
# battle = Battle()
# print(battle.fight(army_1, army_2))

# # ##################### TEST3 #######################

# army_1 = Army()
# army_2 = Army()
# army_1.add_units(Warrior, 2)
# army_1.add_units(Lancer, 3)
# army_1.add_units(Defender, 1)
# army_1.add_units(Warlord, 1)
# army_2.add_units(Warlord, 5)
# army_2.add_units(Vampire, 1)
# army_2.add_units(Rookie, 1)
# army_2.add_units(Knight, 1)
# army_1.units[0].equip_weapon(Sword())
# army_2.units[0].equip_weapon(Shield())
# army_1.move_units()
# army_2.move_units()
# battle = Battle()
# print(battle.straight_fight(army_1, army_2))

# ##################### TEST4 - 26 #######################
army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 2)
army_1.add_units(Lancer, 3)
army_1.add_units(Defender, 1)
army_1.add_units(Warlord, 1)
army_2.add_units(Warlord, 5)
army_2.add_units(Vampire, 1)
army_2.add_units(Rookie, 1)
army_2.add_units(Knight, 1)
army_1.units[0].equip_weapon(Sword())
army_2.units[0].equip_weapon(Shield())
army_1.move_units()
army_2.move_units()
battle = Battle()
battle.straight_fight(army_1, army_2)


# ##################### TEST4 - 10 #######################

# weapon_1 = Katana()
# weapon_2 = Shield()
# my_army = Army()
# my_army.add_units(Vampire, 2)
# my_army.add_units(Rookie, 2)
# enemy_army = Army()
# enemy_army.add_units(Warrior, 1)
# enemy_army.add_units(Defender, 2)
# my_army.units[0].equip_weapon(weapon_1)
# my_army.units[1].equip_weapon(weapon_1)
# my_army.units[2].equip_weapon(weapon_2)
# enemy_army.units[0].equip_weapon(weapon_1)
# enemy_army.units[1].equip_weapon(weapon_2)
# enemy_army.units[2].equip_weapon(weapon_2)
# battle = Battle()
# battle.straight_fight(my_army, enemy_army)