import Game
import AlphaBetaAlgorithm

"""Main of TicTacToe application"""


def print_welcome_message():
    """It displays the welcome message of the game and a brief tutorial about it."""

    print("** Welcome to TicTacToe !! **")
    print("Player one: X is your symbol")
    print("Player two: O is your symbol")
    print("When it's your turn, please enter the number of the square you want to fill as represented above:")
    print("")
    print_demo()
    print_space()
    print("Player one plays first, ready? Let's play ")


def print_demo():
    """It displays how the board will look like during the game."""
    t = 0
    for i in range(3):
        print(" "+str(t)+" "+"|"+" "+str(t+1)+" "+"|"+" "+str(t+2)+" ")
        t = t + 3
        if i != 2:
            print("-----------")


def print_space():
    """It prints two empty lines, used in order to obtain a clearer visualization of the output."""
    # TODO make the method more modular : pass the number of white lines as parameter and use a for loop.
    print("")
    print("")


if __name__ == "__main__":
    print_welcome_message()
    game = Game.Game()
    player = AlphaBetaAlgorithm.AlphaBetaAlgorithm("O", "X")
    turn_played = 0
    current_player = ""

    print_space()
    game.draw_board()

    while turn_played < 9:

        if turn_played % 2 == 0:
            current_player = "X"
            move = int(input(current_player + " inserts your next move: ")) - 1
        else:
            current_player = "O"
            g = Game.Game()
            g.set_board(game.get_board()[:])
            move = player.make_move(g, turn_played)

        if move not in range(9):
            print("Input not recognised, please try again")
            continue
        elif game.insert_symbol(move, current_player):
            if turn_played >= 4:
                if game.check_game_status():
                    game.draw_board()
                    print("## The winner is player " + current_player+" ##")
                    break
                elif turn_played == 8:
                    game.draw_board()
                    print("~~ It's a tie!! ~~")
                    break
            turn_played += 1
        else:
            print("Invalid move, please try again")

        game.draw_board()
        print_space()



