class GameLogic:
    """
    Contains the Tic Tac Toe game logic
    """
    def __init__(self):
        """
        Initializes the class
        """

    @staticmethod
    def check_win(board, ch):
        """
        Accepts a board class
        Check if the player with symbol 'ch' has won the game
        from the current board state
        """
        # check rows
        for row in range(board.side):
            has_won = True
            for col in range(board.side):
                square = board.rows[row][col]
                if square != ch:
                    has_won = False
                    break

            if has_won:
                return True

        # check columns
        for col in range(board.side):
            has_won = True
            for row in range(board.side):
                square = board.rows[row][col]
                if square != ch:
                    has_won = False
                    break

            if has_won:
                return True

        # check main diagonal
        has_won = True
        for row in range(board.side):
            square = board.rows[row][row]
            if square != ch:
                has_won = False
                break

        if has_won:
            return True

        # check anti diagonal
        has_won = True
        for row in range(board.side):
            square = board.rows[row][board.side - row - 1]
            if square != ch:
                has_won = False
                break

        return has_won

    def get_game_result(self, board):
        """
        Accepts a board class
        Calculates the game result given the board state
        Returns 1  - if the player has won the game,
               -1  - if the player has lost the game,
                0  - if the game is a draw, or incomplete
        """
        if self.check_win(board, board.player_ch):
            return 1

        if self.check_win(board, board.opponent_ch):
            return -1

        return 0

    def get_optimal_move(self, board, move_cnt):
        """
        Accepts a board class and number of moves made
        Finds the optimal move by trying all
        available moves and comparing results
        """
        # print('')
        # for row in board.rows:
        #     print(row)
        # print('')

        game_result = self.get_game_result(board)

        # if no more moves can be made return the result
        if move_cnt > board.side * board.side:
            return game_result, -1, -1

        # if a player has won the game
        if game_result != 0:
            return game_result, -1, -1

        #next_state = board.rows[:]

        can_draw = False
        opt_x = -1
        opt_y = -1

        for row in range(board.side):
            for col in range(board.side):
                #square = tmp_state[row][col]
                square = board.get_square(row, col)

                if square == board.empty_square:
                    #next_state[row][col] = board.player_ch
                    board.set_square(row, col, board.player_ch)

                    # reverse the players
                    board.reverse_players()

                    # get the opponent's result if our next move is (row, col)
                    result = self.get_optimal_move(board, move_cnt + 1)

                    # revert changes made
                    board.reverse_players()
                    board.set_square(row, col, board.empty_square)
                    # next_state[row][col] = self.board.empty_square

                    # the opponent loses from the next game state
                    # we win by making the move (row, col)
                    if result[0] == -1:
                        return 1, row, col

                    # the result is a draw
                    if result[0] == 0:
                        can_draw = True
                        opt_x = row
                        opt_y = col

        # there is no winning move,
        # and we can force a draw
        if can_draw:
            return 0, opt_x, opt_y

        # we lose from the current game state
        return -1, -1, -1
