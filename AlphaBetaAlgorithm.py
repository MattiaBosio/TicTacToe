from Game import Game


class AlphaBetaAlgorithm:

    def __init__(self, max_symbol, min_symbol, turn):
        self._max_symbol = max_symbol
        self._min_symbol = min_symbol
        self._game = None
        self._turn = turn

    def set_game(self, game: Game):
        self._game = game

    def min(self, alpha, beta):
        minv = 2