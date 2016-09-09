import random 

class Training_actions():

    def __init__(self):
        self.training_option = 1

    
    def play_training(self, player):
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
                player.strength = player.strength + 15
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
                print("\nUg.. bad choice! It must have been a bad batch and made your stomach upset. Train hard tomorrow.")
            elif self.random_nutrition_choice == "CREATINE":
                print("\nCongrats your strength training is going to pay off. You increased your strength by 15!")
                self.player.strength = self.player.strength + 15
            else:
                 print("\nUg.. bad choice! It must have been a bad batch and made your stomach upset. Train hard tomorrow.")
        elif self.nutrition_choice == "CREATINE":
            if self.random_nutrition_choice == "WHEY":
                 print("\nUg.. bad choice! It must have been a bad batch and made your stomach upset. Train hard tomorrow.")
            elif self.random_nutrition_choice == "CREATINE":
                 print("\nUg.. bad choice! It must have been a bad batch and made your stomach upset. Train hard tomorrow.")
            else:
                print("\nCongrats your strength training is going to pay off. You increased your strength by 15!")
                self.player.strength = self.player.strength + 15
        else:
            if self.random_nutrition_choice == "WHEY":
                print("\nCongrats your strength training is going to pay off. You increased your strength by 15!")
                self.player.strength = self.player.strength + 15
            elif self.random_nutrition_choice == "CREATINE":
                 print("\nUg.. bad choice! It must have been a bad batch and made your stomach upset. Train hard tomorrow.")
            else:
                 print("\nUg.. bad choice! It must have been a bad batch and made your stomach upset. Train hard tomorrow.")
        

    def play_rest(self):
        print("\n"*50)
        print("==="*10)
        print("Getting a good night's sleep is critical to good preparation.")
        print("Congrats on focusing on sound sleep.")
        print("Now go to sleep and see how rested you wake up.")
        print("==="*10)
    
        self.answer = random.randrange(1, 100)

        print("==="*10)
        while True: 
            blank = input("Press the ENTER key to wake up: ")
            if not blank == "":
                print('Hey.. you are not waking up very quickly. Try hitting ENTER again.')
                continue
            else:
                if self.answer >= 50:
                    print("\n"*50)
                    print("==="*10)
                    print('It looks like you got a great night of sleep. Your strength benefit from that!')
                    self.player.strength = self.player.strength + 15
                    print("==="*10)
                    break
                else:
                    print("\n"*50)
                    print("==="*10)
                    print('It seems that the coeds were out late and kept you up.')
                    print('Sometimes students just do not understand what it takes to prepare.')
                    print("==="*10)
                    break

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
                    print("\n"*20)
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
                    sys.exit()
                else:
                    print("\n"*20)
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
                    sys.exit()