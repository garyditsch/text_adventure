import random 

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
       "1: Start Training",
       "2: Play Football Game",
       "3: Save Game", 
       "0: Exit",
    )

    def display_main(self, day):
        while True:
            # print('\nIt is {}, how is your training going?'.format(day))
            print('\nYou currently have a strength of: {}'.format(day.player.strength))

            menu_selection = get_menu_selection(self.MENU_ITEMS)
            if menu_selection == "0":
                print(day)
                break
            elif menu_selection == "1":
                day.display_focus()
            elif menu_selection == "2":
                pass
            elif menu_selection == "3":
                pass
            else:
                display_selection_error(menu_selection)

class Player():

    def __init__(self):
        self.get_name()
        self.get_team()
        self.strength = 0

    def get_name(self):
        self.name = input("Enter your name: ")
        return self.name

    def get_team(self):
        self.team = input("Enter your team name: ")
        return self.team


class Weekday():
    FOCUS_AREA = (
       "1: Focus on your training", 
       "2: Focus on your nutrition",
       "3: Focus on your rest", 
       "0: Exit",
    )

    def __init__(self, player):
        self.player = player
        

    def play_training(self):

        print("\nYour training hard!")

        self.chance = 0
        self.guesses = 3
        self.answer = random.randrange(0, 15)
        
        while self.chance < self.guesses:
            guess = input("\nWhat is your guess? ")
            self.chance += 1
            if guess == " " or not guess.isdigit():
                self.chance -= 1
                print("\nis an invalid option, please try again")
            elif int(guess) == self.answer:
                print("\nCongrats your strength increased by 15!")
                break
            elif self.chance < self.guesses:
                if int(guess) < self.answer:
                    print("\nToo Low, Try Again")
                    print("\nThat was guess: {} . You have {} guesses left.".format(self.chance, self.guesses - self.chance))
                else:
                    print("\nToo High, Try Again")
                    print("\nThat was guess: {} . You have {} guesses left.".format(self.chance, self.guesses - self.chance))
            else:
                print("\nSorry your training was not very good today. Train harder tommorrow!")


    def play_nutrition(nutrition):
        pass

    def play_rest(rest):
        pass

    def display_focus(self):
        while True:
            menu_selection = get_menu_selection(self.FOCUS_AREA)

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
    print('\nWelcome to College Football Training')

    player = Player()

    print('\nOk ... {}  Prepare well this week to have a great game on Saturday'.format(player.name))
    print('If you get the most out of the training, you may score a touchdown for the {}'.format(player.team))

    sunday = Weekday(player)
    monday = Weekday(player)
    tuesday = Weekday(player)
    wednesday = Weekday(player)
    thursday = Weekday(player)
    friday = Weekday(player)

    arr = [sunday, monday, tuesday, wednesday, thursday, friday]

    for day in arr: 
        display = Display()
        display.display_main(day)

if __name__ == '__main__':
    main()