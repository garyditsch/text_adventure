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

        self.sunday = Training_actions(self.player)
        self.monday = Training_actions(self.player)
        self.tuesday = Training_actions(self.player)
        self.wednesday = Training_actions(self.player)
        self.thursday = Training_actions(self.player)
        self.friday = Training_actions(self.player)
        self.saturday = Training_actions(self.player)
        
        self.day_of_week = [self.sunday, self.monday, self.tuesday, self.wednesday, self.thursday, self.friday, self.saturday]

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
            display.current_day = day
            print("\n"*50)
            print("=="*10)
            print("Today is {}".format(self.title[self.day_count]))
            self.day_count += 1
            

            if day == self.saturday:
                display.current_day.play_football()
            else:
                display.display_main()


