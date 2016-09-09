def get_menu_selection(menu_items):
    """
    Display a menu and return the user's selection
    """
    print("\n")
    for menu_items in menu_items:
        print(menu_items)

    return input("\nPlease select an option from above.")

def display_selection_error(menu_selection):
    if menu_selection.isdigit():
        print("\n{} is an invalid option, please try again" .format(menu_selection))
    else:
        print("\n{} is not a number, please enter a number from the menu above" .format(menu_selection))


class Display():

    def __init__(self):
        self.current_day = None

    MENU_ITEMS = (
       "1: Prepare for Game Day",
       "2: Play Football Game",
       "3: Save Game", 
       "0: Go to next day",
       # """ add exit option """
    )

    FOCUS_AREA = (
       "1: Focus on your training", 
       "2: Focus on your nutrition",
       "3: Focus on your rest", 
       "0: Return to main menu",
    )

    def display_main(self):
        while True:
            print('=='*10)
            # print('\nYou currently have a strength of: {}'.format(banana.player.strength))

            menu_selection = get_menu_selection(self.MENU_ITEMS)
            if menu_selection == "0":
                break
            elif menu_selection == "1":
                self.display_focus()
            elif menu_selection == "2":
                pass
            elif menu_selection == "3":
                pass
            else:
                display_selection_error(menu_selection)

    def display_focus(self):
        print('\n')
        print('=='*10)
        # if self.training_option > 0:
        menu_selection = get_menu_selection(self.FOCUS_AREA)

        if menu_selection == "0": 
            pass
        elif menu_selection == "1":
            # self.training_option -= 1
            self.current_day.play_training()
            # pass
        elif menu_selection == "2":
            # self.training_option -= 1
            self.current_day.play_nutrition()
            pass
        elif menu_selection == "3":
            # self.training_option -= 1
            self.current_day.play_rest()
            pass
        else:
            display_selection_error(menu_selection)
        # else:
        #     print('\n'*50)
        #     print('Hey {}... you already chosen your focus for today.'.format(self.player.name))
        #     print('It is time to move on to tomorrow.')
        #     print('The rest of the {} are waiting for you to join them!'.format(self.player.team))
        #     print('\nSelect "0" from the menu below to get to the next day.')

