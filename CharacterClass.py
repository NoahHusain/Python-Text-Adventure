

class Character():
    def __init__(self, name, health):
        self.damageoutput = 10
        self.name = name
        self.health = health

    def takeDamage(self, damage):
        self.health = self.health - damage

    def heal(self, heal_amount):
        self.health = self.health + heal_amount

        # def showInventory():

        # def equipItem():


ChaosMarine = Character("Chaos Marine", 50)

WoundedChaosSpaceMarine = Character("Wounded Chaos Space Marine", 15)


# class ChaosMarine(Enemy):
#     def __init__(self):
#         super().__init__(name="Chaos Space Marine", hp=100, damage=random.randint(26, 55)):


# class WoundedChaosSpaceMarine(Enemy):
#     def __init__(self):
#         super().__init__(name="Wounded Chaos Space Marine", hp=30, damage=random.randint(10, 20)):


# class ChaosCultist(Enemy):
#     def __init__(self):
#         super().__init__(name="Chaos Cultist", hp=50, damage=random.randint(20, 33)):


# class Chaosdemon(Enemy):
#     def __init__(self):
#         super().__init__(name="Chaos Demon", hp=66, damage=random.randint(6, 66)):
