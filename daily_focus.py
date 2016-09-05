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
    DAILY_FOCUS = (
       "1: Focus on your training", 
       "2: Focus on your nutrition",
       "3: Focus on your rest", 
       "0: Exit",
    )

    def __init__(self):
        self.focus = []

    def play_training(training):
        pass

    def play_nutrition(nutrition):
        pass

    def play_rest(rest):
        pass

    def display_focus(self):
        while True:
            menu_selection = get_menu_selection(self.DAILY_FOCUS)

            if menu_selection == "0": 
                break
            elif menu_selection == "1":
                self.play_training()
            elif menu_selection == "2":
                self.play_nutrition()
            elif menu_selection == "3":
                self.play_rest()
            else:
                display_selection_error(menu_selection)

def main():
    """
    Main Loop
    """

    display = Display()
    display.display_focus()

if __name__ == '__main__':
    main()