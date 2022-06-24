class Warrior:
    def __init__(self, health=50, attack=5):
        self.type = "warrior"
        self.health = health
        self.attack = attack
        self.is_alive = True

class Knight(Warrior):
    def __init__(self, health=50, attack=7):
        self.type = "kinght"
        self.health = health
        self.attack = attack
        self.is_alive = True

def fight(unit_1, unit_2):
    round = 0
    while unit_1.is_alive and unit_2.is_alive:
        if round % 2 == 0:
            unit_2.health -= unit_1.attack
            unit_2.is_alive = True if unit_2.health > 0 else False
            round += 1
        else:
            unit_1.health -= unit_2.attack
            unit_1.is_alive = True if unit_1.health > 0 else False
            round += 1
    return True if unit_1.is_alive else False
