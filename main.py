from game import Game 

def main():
    """
    Main Loop
    """
    game = Game()
    game.game_setup()
    game.game_play()

if __name__ == '__main__':
    main()