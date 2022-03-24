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
        Finds the optimal move by trying all available
        moves and comparing results
        Returns: result type, moves until victory, optimal row, optimal col
        """
        # print('')
        # for row in board.rows:
        #     print(row)
        # print('')

        game_result = self.get_game_result(board)

        # if no more moves can be made return the result
        if move_cnt > board.side * board.side:
            # print('state: ', game_result, move_cnt, -1, -1)
            return game_result, move_cnt, -1, -1

        # if a player has won the game
        if game_result != 0:
            # print('state: ', game_result, move_cnt, -1, -1)
            return game_result, move_cnt, -1, -1

        max_move_cnt = board.side * board.side + 2
        min_moves = max_move_cnt
        max_moves = -1
        can_draw = False
        opt_row = -1
        opt_col = -1

        for row in range(board.side):
            for col in range(board.side):
                square = board.get_square(row, col)

                if square == board.empty_square:
                    board.set_square(row, col, board.player_ch)

                    # reverse the players
                    board.reverse_players()

                    # get the opponent's result if our next move is (row, col)
                    result = self.get_optimal_move(board, move_cnt + 1)

                    # revert changes made
                    board.reverse_players()
                    board.set_square(row, col, board.empty_square)

                    # the opponent loses from the next game state
                    # we win by making the move (row, col)
                    # check if this move ends the game faster
                    # than the previous fastest wining move
                    if result[0] == -1 and result[1] < min_moves:
                        # print('loss found', result[1], row, col)
                        # return 1, min_moves, row, col
                        min_moves = result[1]
                        opt_row = row
                        opt_col = col

                    # the result is a draw and a wining move isn't found yet
                    if result[0] == 0 and min_moves == max_move_cnt:
                        can_draw = True
                        opt_row = row
                        opt_col = col

                    if result[0] == 1 and min_moves == max_move_cnt and max_moves < result[1] and not can_draw:
                        max_moves = result[1]
                        opt_row = row
                        opt_col = col
        # a winning move exists
        if min_moves != max_move_cnt:
            # print('state: 1', min_moves, opt_row, opt_col)
            return 1, min_moves, opt_row, opt_col

        # there is no winning move,
        # and we can force a draw
        if can_draw:
            # print('state: 0', move_cnt, opt_row, opt_col)
            return 0, move_cnt, opt_row, opt_col

        # we lose from the current game state
        # print('state: -1', max_moves, opt_row, opt_col)
        return -1, max_moves, opt_row, opt_col
