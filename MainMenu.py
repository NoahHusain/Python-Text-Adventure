from MainGame import game_start


def MainMenu():
    main_menu_active = True
    while main_menu_active == True:
        menu_question = input(
            "Welcome to 'Warhammer 40k: Ultramarines' please select a main menu option (start/exit): ").lower()

        if menu_question == "start":
            game_start()
        elif menu_question == "exit":
            print("Sadge")
            main_menu_active = False
        else:
            print("We did not understand your input. Please try again")


MainMenu()
