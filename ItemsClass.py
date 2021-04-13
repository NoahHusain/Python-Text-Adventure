

class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def return_description():
        print(self.description)

    def return_name():
        print(self.name)


class Weapon(Item):
    def __init__(self, name, description, damage, accuracy):
        self.damage = damage
        self.accuracy = accuracy
        super().__init__(name, description)


class armors(Item):
    def __init__(self, name, description, defense, evasion):
        self.defense = defense
        self.evasion = evasion
        super().__init__(name, description)
