

def game_start():
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
        fight()


def fight():
    # combat sequence here
    # while enemyhealth > 0:
    #     # combat code
    #     print('Combat not working')
    #     Act_1_Armory()
    # if self.health <= 0:
    #     print('You have given your life for the emperor.')
    #     Act_1_Armory()
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


# def fist_combat():
#     while enemyhp > 0


game_over = False

# game_start()
