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
    t = 0
    for i in range(3):
        print(" "+str(t)+" "+"|"+" "+str(t+1)+" "+"|"+" "+str(t+2)+" ")
        t = t + 3
        if i != 2:
            print("-----------")


def print_space():
    print("")
    print("")


if __name__ == "__main__":
    print_welcome_message()
    game = Game.Game()
    turn_played = 0
    current_player = ""

    while turn_played <=9:

        print_space()
        game.draw_board()
        if turn_played % 2 == 0:
            current_player = "X"
        else:
            current_player = "O"
        print(current_player+" inserts your next move")
        move = input()
        move = int(move)
        if move not in range(1, 10):
            print("Input not recognised, please try again")
            continue
        elif game.insert_symbol(move, current_player):
            turn_played += 1
        else:
            print("Invalid move, please try again")




