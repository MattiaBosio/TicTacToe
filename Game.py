class Game:

    def __init__(self):
        self._space = " "
        self._empty = "   "
        self._board = [self._empty] * 9
        self._bar = "|"
        self._line = "-----------"

    def get_board(self):
        return self._board

    def get_empty_symbol(self):
        return self._empty

    def draw_board(self):
        t = 0
        for i in range(3):
            print(self._board[t]+self._bar+self._board[t+1]+self._bar+self._board[t+2])
            t = t + 3
            if i != 2:
                print(self._line)

    def insert_symbol(self, position, symbol):
        if self._board[position-1] != self._empty:
            return False
        self._board[position-1] = self._space + symbol + self._space
        return True

    def remove_symbol(self, position):
        self._board[position] = self._empty
        
    def _check_rows(self):
        t = 0
        for i in range(3):
            if self._board[t] == self._board[t + 1] and self._board[t + 1] == self._board[t + 2] and \
                    self._empty not in self._board[t:t+2]:
                return True
            t = t + 3
        return False

    def _check_columns(self):
        t = 0
        for i in range(3):
            if self._board[t] == self._board[t + 3] and self._board[t + 3] == self._board[t + 6] and \
                    self._empty not in self._board[t:t+6:3]:
                return True
            t = t + 1
        return False

    def _check_diagonals(self):

        return (self._board[0] != self._empty and self._board[0] == self._board[4] and
                self._board[4] == self._board[8]) or \
               (self._board[2] != self._empty and self._board[2] == self._board[4] and
                self._board[4] == self._board[6])

    def check_game_status(self):
        return self._check_rows() or self._check_columns() or self._check_diagonals()
