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




class Game():
    """ Has attributes: player name, team name, strength """
     
    def __init__(self):
        player.name()
        player.team() 

class Football():

    def __init__(self):
        player.strength()


class Training():

    def get_daily_focus():


class Player():

    def __init__(self):
        """Return player object, getting player name, team, set initial strength"""
        self.name()
        self.team()
        self.position()
        self.strength()

    def name(self):
        self.name = input("Enter your player's name: ")
        return self.name

    def team(self):
        self.team = input("What team do you play for? ")

    def position(self):



class Physical_training():


