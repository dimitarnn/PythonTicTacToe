import Board


class GameLogic(Board.Board):
    """
    Contains the Tic Tac Toe game logic
    """
    def __init__(self, side):
        """
        Initializes the class
        """
        super(GameLogic, self).__init__(side)

    def check_win(self, tmp_state, ch):
        """
        Check if the player with symbol 'ch' has won the game
        """
        # check rows
        for i in range(self.side):
            has_won = True
            for j in range(self.side):
                el = tmp_state[i][j]
                if el != ch:
                    has_won = False
                    break

            if has_won:
                return True

        # check columns
        for i in range(self.side):
            has_won = True
            for j in range(self.side):
                el = tmp_state[j][i]
                if el != ch:
                    has_won = False
                    break

            if has_won:
                return True

        # check main diagonal
        has_won = True
        for i in range(self.side):
            el = tmp_state[i][i]
            if el != ch:
                has_won = False
                break

        if has_won:
            return True

        # check anti diagonal
        has_won = True
        for i in range(self.side):
            el = tmp_state[i][self.side - i - 1]
            if el != ch:
                has_won = False
                break

        return has_won

    def get_game_result(self, tmp_state, player_ch, opponent_ch):
        """
        Returns 1  - if the player has won the game,
               -1  - if the player has lost the game,
                0  - if the game is a draw, or incomplete
        """
        if self.check_win(tmp_state, player_ch):
            return 1

        if self.check_win(tmp_state, opponent_ch):
            return -1

        return 0

    def get_optimal_move(self, tmp_state, move_cnt, player_ch, opponent_ch):
        """
        Finds the optimal move by trying all
        available moves and comparing results
        """
        game_result = self.get_game_result(tmp_state, player_ch, opponent_ch)

        # if no more moves can be made return the result
        if move_cnt > self.side * self.side:
            return game_result, -1, -1

        # if a player has won the game
        if game_result != 0:
            return game_result, -1, -1

        next_state = tmp_state.copy()

        can_draw = False
        opt_x = -1
        opt_y = -1

        for i in range(self.side):
            for j in range(self.side):
                el = tmp_state[i][j]

                if el == self.empty_square:
                    next_state[i][j] = player_ch

                    # get the opponent's result if our next move is (i, j)
                    result = self.get_optimal_move(next_state, move_cnt + 1, opponent_ch, player_ch)

                    next_state[i][j] = self.empty_square

                    # the opponent loses from the next game state
                    # we win by making the move (i, j)
                    if result[0] == -1:
                        return 1, i, j

                    # the result is a draw
                    if result[0] == 0:
                        can_draw = True
                        opt_x = i
                        opt_y = j

        # there is no winning move,
        # and we can force a draw
        if can_draw:
            return 0, opt_x, opt_y

        # we lose from the current game state
        return -1, -1, -1
