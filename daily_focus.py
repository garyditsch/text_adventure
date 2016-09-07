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
       "1: Prepare for Game Day",
       "2: Play Football Game",
       "3: Save Game", 
       "0: Go to next day",
    )

    def display_main(self, banana):
        while True:
            print('=='*10)
            print('\nYou currently have a strength of: {}'.format(banana.player.strength))

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
        self.team = self.team.upper()

class Weekday():
    FOCUS_AREA = (
       "1: Focus on your training", 
       "2: Focus on your nutrition",
       "3: Focus on your rest", 
       "0: Return to main menu",
    )


    def __init__(self, player):
        self.player = player
        self.training_option = 1
    
    def play_training(self):
        print("==="*10)
        print("To benefit from the weight room, you need to do the right amount of reps.")
        print("\nUnfortunately your strength coach sucks and thinks you should guess the right number.")
        print("\nHe has given you 3 chances to guess a number between 1 and 15.")
        print("\nIf you get it right, he'll help you. Otherwise you are on your own.")

        self.chance = 0
        self.guesses = 3
        self.answer = random.randrange(1, 15)
        
        while self.chance < self.guesses:
            guess = input("\nWhat is your guess? ")
            self.chance += 1
            if guess == " " or not guess.isdigit():
                self.chance -= 1
                print("\nis an invalid option, please try again")
            elif int(guess) == self.answer:
                print("\nCongrats your strength training is going to pay off. You increased your strength by 15!")
                self.player.strength = self.player.strength + 15
                break
            elif self.chance < self.guesses:
                if int(guess) < self.answer:
                    print("\nToo Low, Try Again")
                    print("\nThat was guess: {} . You have {} guesses left.".format(self.chance, self.guesses - self.chance))
                else:
                    print("\nToo High, Try Again")
                    print("\nThat was guess: {} . You have {} guesses left.".format(self.chance, self.guesses - self.chance))
            else:
                print("\nSorry your training is not going to be very good today. Train harder tommorrow!")


    def play_nutrition(self):
        print("==="*10)
        print("Smart decision to think about your nutrition during the week.")
        print("Today you have 3 ways to supplement your food choices:")
        print("Your choices are: Whey, Creatine, Sword")
        self.nutrition_choice = input("\nWhat are you adding to your diet today? ").upper()

        options = ['WHEY', 'CREATINE', 'SWORD']
        self.random_nutrition_choice = random.choice(options)
        
        if self.nutrition_choice == "WHEY":
            if self.random_nutrition_choice == "WHEY":
                print("\nUg.. bad choice! It must have been a bad batch and make your stomach upset. Train hard tomorrow.")
            elif self.random_nutrition_choice == "CREATINE":
                print("\nCongrats your strength training is going to pay off. You increased your strength by 15!")
                self.player.strength = self.player.strength + 15
            else:
                 print("\nUg.. bad choice! It must have been a bad batch and make your stomach upset. Train hard tomorrow.")
        elif self.nutrition_choice == "CREATINE":
            if self.random_nutrition_choice == "WHEY":
                 print("\nUg.. bad choice! It must have been a bad batch and make your stomach upset. Train hard tomorrow.")
            elif self.random_nutrition_choice == "CREATINE":
                 print("\nUg.. bad choice! It must have been a bad batch and make your stomach upset. Train hard tomorrow.")
            else:
                print("\nCongrats your strength training is going to pay off. You increased your strength by 15!")
                self.player.strength = self.player.strength + 15
        else:
            if self.random_nutrition_choice == "WHEY":
                print("\nCongrats your strength training is going to pay off. You increased your strength by 15!")
                self.player.strength = self.player.strength + 15
            elif self.random_nutrition_choice == "CREATINE":
                 print("\nUg.. bad choice! It must have been a bad batch and make your stomach upset. Train hard tomorrow.")
            else:
                 print("\nUg.. bad choice! It must have been a bad batch and make your stomach upset. Train hard tomorrow.")
        

    def play_rest(rest):
        pass

    def play_football(self):
        print("==="*10)
        print("How about we play some football!!")
        # played_football = True

        if self.player.strength <= 30:
            self.guesses = 2
            print("You have {} downs to score a touchdown. Maybe you should have prepared better!".format(self.guesses))
        elif self.player.strength <= 60:
            self.guesses = 4
            print("You have {} downs to score a touchdown. You prepared well, but don't waste a down!".format(self.guesses))
        else:
            self.guesses = 8
            print("You have {} downs to score a touchdown. Nice work this week, preparing for the game".format(self.guesses))
        self.chance = 0
        self.answer = random.randrange(1, 50)
        
        while self.chance < self.guesses:
            guess = input("\nWhat is your guess? ")
            self.chance += 1
            if guess == " " or not guess.isdigit():
                self.chance -= 1
                print("\nis an invalid option, please try again")
            elif int(guess) == self.answer:
                print("\nTOUCHDOWN!!")
                if self.player.team == "HUSKERS":
                    print("\nThe Huskers are on their way to their 6th National Title with your help!")
                else:
                    print("\nYou helped your team win a well played game.")
                break
            elif self.chance < self.guesses:
                if int(guess) < self.answer:
                    print("\nToo Low, Try Again")
                    print("\nThat was guess: {} . You have {} guesses left.".format(self.chance, self.guesses - self.chance))
                else:
                    print("\nToo High, Try Again")
                    print("\nThat was guess: {} . You have {} guesses left.".format(self.chance, self.guesses - self.chance))
            else:
                if self.player.team == "HUSKERS":
                    print("\nAs a Husker we expect more from you, but no worries your teammates earned the win regardless of your poor effort.")
                    print('\n')
                    print('           _____                         ____                   ')
                    print('          / ____|                       / __ \                  ')
                    print('         | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __   ')
                    print("         | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \  __|  ")
                    print('         | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |     ')
                    print('          \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|     ')
                    print('\n')
                    print('=='*10)
                    break
                else:
                    print("\nPrepare better. And consider transferring to a new school, your team lost again.")
                    print('\n')
                    print('           _____                         ____                   ')
                    print('          / ____|                       / __ \                  ')
                    print('         | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __   ')
                    print("         | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \  __|  ")
                    print('         | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |     ')
                    print('          \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|     ')
                    print('\n')
                    print('=='*10)
                    break


    def display_focus(self):
        print('\n')
        print('=='*10)
        if self.training_option > 0:
            menu_selection = get_menu_selection(self.FOCUS_AREA)

            if menu_selection == "0": 
                pass
            elif menu_selection == "1":
                self.training_option -= 1
                self.play_training()
            elif menu_selection == "2":
                self.training_option -= 1
                self.play_nutrition()
            elif menu_selection == "3":
                self.training_option -= 1
                self.play_rest()
            else:
                display_selection_error(menu_selection)
        else:
            print('Hey {}... you already chosen your focus for today.'.format(self.player.name))
            print('It is time to move on to tomorrow.')
            print('The rest of the {} are waiting for you to join them!'.format(self.player.team))
            print('\nSelect "0" from the menu below to get to the next day.')
def main():
    """
    Main Loop
    """
    print('\nWelcome to College Football Training')
    print('=='*10)

    player = Player()

    print('=='*10)
    print('\nOk ... {}  Prepare well this week to have a great game on Saturday'.format(player.name))
    print('\n')
    print('If you get the most out of the training, you may score a touchdown for the {}'.format(player.team))

    sunday = Weekday(player)
    monday = Weekday(player)
    tuesday = Weekday(player)
    wednesday = Weekday(player)
    thursday = Weekday(player)
    friday = Weekday(player)
    saturday = Weekday(player)

    title = [
       "Sunday",
       "Monday",
       "Tuesday",
       "Wednesday",
       "Thursday",
       "Friday",
       "Game Day!!"
    ]

    day_count = 0

    arr = [sunday, monday, tuesday, wednesday, thursday, friday, saturday]

    for day in arr: 
        display = Display()
        print("=="*10)
        print("Today is {}".format(title[day_count]))
        day_count += 1
        # while played_football == False:
        if day == saturday:
            day.play_football()
        else:
          display.display_main(day)

if __name__ == '__main__':
    main()