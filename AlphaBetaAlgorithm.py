from Game import Game


class AlphaBetaAlgorithm:

    def __init__(self, max_symbol, min_symbol, turn):
        self._max_symbol = max_symbol
        self._min_symbol = min_symbol
        self._game = None
        self._turn = turn

    def set_game(self, game: Game):
        self._game = game

    def min(self, alpha, beta, turn):
        minv = 2
        move = None
        if self._game.check_game_status():
            return 1, 0
        elif turn == 8:
            return 0, 0

        for i in range(9):
            if self._game.insert_symbol(i, self._min_symbol):
                (m, max_move) = self.max(alpha, beta, turn + 1)
                if m < minv:
                    minv = m
                    move = i
                self._game.remove_symbol(i)

                if minv <= alpha:
                    return minv, move

                if minv < beta:
                    beta = minv

        return minv, move

    def max(self, alpha, beta, turn):
        maxv = -2
        move = None
        if self._game.check_game_status():
            return -1, 0
        elif turn == 8:
            return 0, 0

        for i in range(9):
            if self._game.insert_symbol(i, self._max_symbol):
                (m, min_move) = self.min(alpha, beta, turn + 1)

                if m > maxv:
                    maxv = m
                    move = i
                self._game.remove_symbol(i)

                if maxv >= beta:
                    return maxv, move

                if maxv > alpha:
                    alpha = maxv

        return maxv, move

    def make_move(self, game_status: Game, turn):
        self.set_game(game_status)
        return self.max(-2, 2, turn)[1]
