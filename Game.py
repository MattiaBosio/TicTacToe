class Game:

    def __init__(self):
        self._board = ["    "] * 9
        self._bar = "|"
        self._line = "--------------"

    def drawBoard(self):
        for i in range(3):
            print(self._board[i]+self._bar+self._board[i+1]+self._bar+self._board[i+2])
            if i != 2:
                print(self._line)

