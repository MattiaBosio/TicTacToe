class Game:

    def __init__(self):
        self._space = " "
        self._empty = "    "
        self._board = [self._empty] * 9
        self._bar = "|"
        self._line = "--------------"

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


