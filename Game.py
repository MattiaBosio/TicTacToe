class Game:
    """
    A class which represents a game of TicTacToe.

    ...

    Attributes
    ----------
    _space : str
        a formatted string which is a space character
    _empty : str
        a formatted string which represents the blank space in the board
    _board : list
        the 9x9 board of TicTacToe game
    _bar : str
        a formatted string which is the "|" character used for drawing the board in the shell output
    _line : str
        a formatted string which represents a  line and it is used for drawing the board in the shell output

    """

    def __init__(self):
        self._space = " "
        self._empty = "   "
        self._board = [self._empty] * 9
        self._bar = "|"
        self._line = "-----------"

    def get_board(self):
        """Getter for the _board attribute of Game class"""
        return self._board

    def set_board(self, board):
        """Setter for the _board attribute of Game class"""
        self._board = board
        
    def get_empty_symbol(self):
        """Getter for the _empty attribute of Game class"""
        return self._empty

    def draw_board(self):
        """Method which draws the board in the shell output"""
        t = 0
        for i in range(3):
            print(self._board[t]+self._bar+self._board[t+1]+self._bar+self._board[t+2])
            t = t + 3
            if i != 2:
                print(self._line)

    def insert_symbol(self, position, symbol):
        """Method which insert the symbol of the player, playing in the current turn, in the position of the board
            selected by the player

        Parameters
        ----------
        position : int
            The position of the board in which the player wants to insert his symbol

        symbol : str
            The symbol associated to the player
        """
        if self._board[position] != self._empty:
            return False
        self._board[position] = self._space + symbol + self._space
        return True

    def remove_symbol(self, position):
        """Method used to remove the symbol, specified in the position parameter, in the board

         Parameters
        ----------
        position : int
            The position of the board in which the symbol has to be removed

        """
        self._board[position] = self._empty
        
    def _check_rows(self):
        """Private method which checks if there is a winning combination of symbols in the rows of the board"""
        t = 0
        for i in range(3):
            if self._board[t] == self._board[t + 1] and self._board[t + 1] == self._board[t + 2] and \
                    self._empty not in self._board[t:t+2]:
                return True
            t = t + 3
        return False

    def _check_columns(self):
        """Private method which checks if there is a winning combination of symbols in the columns of the board"""
        t = 0
        for i in range(3):
            if self._board[t] == self._board[t + 3] and self._board[t + 3] == self._board[t + 6] and \
                    self._empty not in self._board[t:t+6:3]:
                return True
            t = t + 1
        return False

    def _check_diagonals(self):
        """Private method which checks if there is a winning combination of symbols in the main diagonals
        of the board"""
        return (self._board[0] != self._empty and self._board[0] == self._board[4] and
                self._board[4] == self._board[8]) or \
               (self._board[2] != self._empty and self._board[2] == self._board[4] and
                self._board[4] == self._board[6])

    def check_game_status(self):
        """Method which checks the game status.
            It returns true when the game is won by a player"""
        return self._check_rows() or self._check_columns() or self._check_diagonals()
