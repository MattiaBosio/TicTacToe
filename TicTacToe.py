import Game


def print_welcome_message():
    print("** Welcome to TicTacToe !! **")
    print("Player one: X is your symbol")
    print("Player two: O is your symbol")
    print("When it's your turn, please enter the number of the square you want to fill as represented above:")
    print("")
    print_demo()
    print_space()
    print("Player one plays first, ready? Let's play ")


def print_demo():

    print(" 1 " + "|" + " 2 " + "|" + " 3 ")
    print("------------")
    print(" 4 " + "|" + " 5 " + "|" + " 6 ")
    print("------------")
    print(" 7 " + "|" + " 8 " + "|" + " 9 ")


def print_space():
    print("")
    print("")


if __name__ == "__main__":
    print_welcome_message()
    game = Game.Game()
    turn_played = 0



