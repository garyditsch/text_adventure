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

    MENU_ITEMS = (
       "1: Prepare for Game Day",
       "2: Play Football Game",
       "3: Save Game", 
       "0: Go to next day",
    )

    def display_main(self, banana):
        while True:
            print('=='*10)
            # print('\nYou currently have a strength of: {}'.format(banana.player.strength))

            menu_selection = get_menu_selection(self.MENU_ITEMS)
            if menu_selection == "0":
                break
            elif menu_selection == "1":
                banana.display_focus()
            elif menu_selection == "2":
                banana.play_football()
            elif menu_selection == "3":
                pass
            else:
                display_selection_error(menu_selection)