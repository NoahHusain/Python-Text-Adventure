from CharacterClass import Character
from ItemsClass import Weapon

Main_Character = Character('new character', 150)


def game_start():
    Char_name = input('What do you wish to name your character?')
    Char_health = input(
        "What health do you want your character to have? (250 = Easy, 150 = Medium, 100 = Hard)")
    Main_Character = Character(Char_name, Char_health)
    Act_1_A = input("You wake up on the Ultramarine planet of Macragge to sirens blaring in your room. Over the intercom you hear of a chaos invasion fleet heading towards your fortress. Will you head to the armory to \ngrab your weapon and bolter or go back to sleep? (Sleep/Armory)").lower().strip()
    act_1_start(Act_1_A)


def act_1_start(Act_1_A):
    if Act_1_A == 'sleep':
        print("You go back to sleep never to wake up having been killed by a chaos marine who finds you fast asleep. You are a traitor to the Emperor!")
        print("GAME OVER!")
        game_over = True
    elif Act_1_A == 'armory':
        Act_1_B = input("As you rush towards the armory you are confronted by a wounded chaos space marine. He looks at you and pulls out his knife. Do you run back the way you came or fight the wounded chaos marine? \n(Fight/Run)").lower().strip()
        act_1_combat(Act_1_B)


def act_1_combat(Act_1_B):
    if Act_1_B == 'Run':
        print("You turn around in an attempt to run away, but the chaos space marine lets loose his chaos blade. It strikes you squarely in the back, mortally wounding you in the process. You die as a coward.")
        print("GAME OVER!")
        game_over = True
    elif Act_1_B == 'fight':
        test_character = Character('Tiberius', 20)
        enemy_character = Character('Horus', 20)
        fight(test_character, enemy_character)


def fight(Character_1, Character_2):
    #
    while Character_1.health > 0 and Character_2.health > 0:

        fight_choice = input('Do you wish to attack or heal?').strip().lower()

        if fight_choice == "attack":
            print(Character_2.name, "takes",
                  Character_1.damageoutput, "damage.")
            Character_2.takeDamage(Character_1.damageoutput)
        if fight_choice == "heal":
            Character_1.health(10)
    #     # combat code
    #     Act_1_Armory()
        # if Character_1.health <= 0:
        #     print('You have given your life for the emperor.')
        #     game_over = True
    # else:
    Act_1_Armory()


def Act_1_Armory():
    Armor_Question = input("Having dealt with the traitorous chaos space marine, you continue onto the armory. Once arrived you are met with the sight of scarce armor and weapon choices. You choose to suit up in your \narmor first as the codex astartes commands. Do you choose the lightweight standar space marine armor for maximum dexterity or the tanky exterminator armor for maximum defense? (Standard/Exterminator)").lower().strip()
    if Armor_Question == 'standard':
        # equip standard armor
        Act_1_Weapon()
    elif Armor_Question == 'exterminator':
        # equip standard armor
        Act_1_Weapon()


def Act_1_Weapon():
    Gun_Question = input("After putting on your armor, you make your way to the weapons. You have a choice between the trusty Bolter given to every space marine and renowned for its accuracy, or the more rare meltagun \nwhich due to its poor accuracy but God-Like damage is reserved for anti vehicle use. Which do you choose? (Bolter/Meltagun)").lower().strip()
    if Gun_Question == 'bolter':
        # grab bolter
        print('You grab the bolter.')
    elif Gun_Question == 'meltagun':
        # grab meltagun
        print('You grab the meltagun.')


def act_1_segway():
    segway_question = input("Having grabbed your weapon and armor you hear over the helmet radio through rampant gunfire and constant static that your Astartes brothers are held up at the front fortress under heavy\nenemy fire. Do you decide to fight your way to to the front to assist your brothers or barricade yourself in the armory and wait for the invasion to come to you? (Assist/Barricade)").lower().strip()
    act_1_combat_2(segway_question)


def act_1_combat_2(segway_question):
    if segway_question == 'Barricade':
        print("While not the worst idea, your plan was cut short by a chaos marine bombardment that vaporized the armory minutes after you started barricading.")
    elif segway_question == 'Assist':
        Possible_Combat = input('You radio to your brothers that you are on your way to assist in the effort to hold back the chaos marine forces and head out of the armory towards the front of the fortress. Rushing past your\nwounded brothers you are halted by a chaos marine drop pod crashing through the roof of the hallway. You find cover as the pod door opens revealing a single chaos space marine. Do you choose to\nengage the traitor marine or try to find a different way to the front of the fortress? (Engage/Evade)').lower().strip()
        act_1_combat_3(Possible_Combat)


def act_1_combat_3(Possible_Combat):
    if Possible_Combat == 'Engage':
        print('You decide to engage the enemy space marine.')
        fight()
    elif Possible_Combat == 'Evade':
        print('You decide to evade the enemy space marine and find a different way to the front of the fortress.')
        evade()


def evade():
    Evasion = input('You decide to evade the space marine in the hopes to get to the front of the fortress quicker. You wind your way through the halls of the fortress and finally make your way to the front where your\nbrothers are taking heavy fire from invading chaos forces. You see a chaos cultist, chaos marine, and chaos demon approaching the position and engage them. You"re brothers ask which one you will engage\nand they will handle the others. Which do you decide to engage? (Cultist/Marine/Demon)  ')
    act_1_combat_end(Evasion)


# def act_1_combat_end(Evasion):
#     if Evasion == 'Cultist':
#         Cultist_enemy = Character('Chaos Cultist', 50)
#         fight(, Cultist_enemy)
#     elif Evasion == 'Marine':
#         Marine_enemy = Character('Chaos Space Marine', 100)
#         fight(, Marine_enemy)
#     elif Evasion == 'Demon':
#         Demon_enemy = Character('Chaos Demon', 150)
#         fight(, Demon_enemy)


# def fight():
#     option = input('Would you like to attack or heal? (attack/heal)')
#     if option == "attack":
#         attack()
#     elif option == "heal":
#         heal()


# def firstaid():
#     pass


def attack():
    player_attack = bolter.damage
    enemy_attack = bolter.damage / 2


# def heal():


# game_over = False


# todo: Make damage a random int between 51 and 110
Bolter = Weapon("Bolter", "The standard weapon of the Adeptus Astartes and Adepta Sororitas. A .75 caliber weapon, the Boltgun fires a self-propelled explosive 'bolt' which explodes with devastating effect once it has penetrated its target, effectively blowing it apart from the inside.", 100, 85)


# class Bolter(Weapon)


# def __init__(name='BolteThe standard weapon of the Adeptus Astartes and Adepta Sororitas. A .75 caliber weapon, the Boltgun fires a self-propelled explosive "bolt" which explodes with devastating effect once it has penetrated its target, effectively blowing it apart from the inside.r',
#              description='',
#              damage=random.randint(51, 110)
#              accuracy=85)):


# class MeltaGun(Weapon)

# def __init__(name = 'MeltaGun',
#              description = 'The Meltagun, also called a "Fusion Gun," "Melter," or "Cooker," is a powerful, short-ranged anti-armour weapon that produces an intense, energetic beam of heat in the tens of thousands of degrees Centigrade.',
#              damage = random.randint(100, 200)
#              accuracy = 65)):


# class PowerArmor(Armor)

# def __init__(name='Power Armor',
#              description='Power Armour is an advanced form of powered combat armour, worn primarily by the Space Marines and the Chaos Space Marines, though suits have been created to be worn by mere mortals. It is a completely enclosed suit of combat armour composed of shaped Adamantium and Plasteel plates, encased in a Ceramite ablative layer.',
#              defense=5
#              evasion=33)):


# class TerminatorArmor(Armor)

# def __init__(name='Terminator Armor',
#              description='Tactical Dreadnought Armour, more often called Terminator Armour, is one of the strongest forms of personal Power Armour in existence and is the heaviest and most resilient model the Imperium of Man has to offer. It was developed for a mid-range of uses between the armoured chassis of a true Dreadnought and standard Power Armour. It is composed of a specially synthesized ceramite/plasteel alloy exoskeleton whose manufacture is now unknown to the Adeptus Mechanicus, with servo-assisted interfaces that link into the user"s own neurological and muscular systems to enhance movement.',
#              defense=10
#              evasion=16)):


# class SoldiersBlade(Weapons)

# def __init__(name='Soldiers Blade',
#              description='The Soldier"s Blade is a deceptively simple sword, that has been a treasure of the Ultramarines since the Chapter"s founding and has seen use in countless battles. Though it is not a power sword, the Soldier"s Blade"s monomolecular-edge, can still carve through the thickest plates of ceramite and plasteel with little resistance and without need of being re-honed.',
#              damage=random.randint(25, 40)
#              accuracy=100)):


# class Fist(Weapons)

# def __init__(name='Fist',
#              description='A space marines hardened fists. Only to be used in the most dire of situations.',
#              damage=random.randint(5, 15)
#              accuracy=100)):
