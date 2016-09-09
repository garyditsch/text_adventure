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

        self.sunday = Training_actions()
        self.monday = Training_actions()
        self.tuesday = Training_actions()
        self.wednesday = Training_actions()
        self.thursday = Training_actions()
        self.friday = Training_actions()
        self.saturday = Training_actions()
        
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
            print(display.current_day)
            print("Today is {}".format(self.title[self.day_count]))
            self.day_count += 1
            # print(current_day)
            # while played_football == False:

            if day == self.saturday:
                display.current_day.play_football()
                # print("Good Luck!")
            else:
                display.display_main()



# create current_player, use in display



