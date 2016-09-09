from player import Player
from weekday import Training_actions 
from display import Display

class Game():

    def __init__(self):
        self.day_count = 0


    def game_setup(self):

        print('\nWelcome to College Football Training')
        print('=='*10)

        self.player = Player()
        
        print('=='*10)
        print('\nOk ... {}  Prepare well this week to have a great game on Saturday'.format(self.player.name))
        print('\n')
        print('If you get the most out of the training, you may score a touchdown for the {}'.format(self.player.team))

        sunday = Training_actions()
        monday = Training_actions()
        tuesday = Training_actions()
        wednesday = Training_actions()
        thursday = Training_actions()
        friday = Training_actions()
        saturday = Training_actions()
        
        self.day_of_week = [sunday, monday, tuesday, wednesday, thursday, friday, saturday]

        self.title = [
           "Sunday",
           "Monday",
           "Tuesday",
           "Wednesday",
           "Thursday",
           "Friday",
           "Game Day!!"
        ]

    def game_play(self):

        """ Main menu display """
        for day in self.day_of_week: 
            display = Display()
            print("\n"*50)
            print("=="*10)
            print("Today is {}".format(self.title[self.day_count]))
            self.day_count += 1
            # while played_football == False:

            # if day == weekday.saturday:
            #     # day.play_football()
            #     print("Good Luck!")
            # else:
            display.display_main(day)







