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