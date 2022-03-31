import IBoard
import IGameLogic


class GameLogicRecursive(IGameLogic.IGameLogic):
    """
    Contains the Tic Tac Toe game logic
    """

    def __init__(self):
        """
        Initializes the class
        """
        super(GameLogicRecursive, self).__init__()

    def check_win(self, board: IBoard.IBoard, ch: str) -> bool:
        """
        Accepts a board class
        Checks if the player with symbol 'ch' has won the game
        from the current board state
        """
        # check rows
        for row in range(board.get_side()):
            has_won = True
            for col in range(board.get_side()):
                square = board.get_square(row, col)
                if square != ch:
                    has_won = False
                    break

            if has_won:
                return True

        # check columns
        for col in range(board.get_side()):
            has_won = True
            for row in range(board.get_side()):
                square = board.get_square(row, col)
                if square != ch:
                    has_won = False
                    break

            if has_won:
                return True

        # check main diagonal
        has_won = True
        for row in range(board.get_side()):
            square = board.get_square(row, row)
            if square != ch:
                has_won = False
                break

        if has_won:
            return True

        # check anti diagonal
        has_won = True
        for row in range(board.get_side()):
            square = board.get_square(row, board.get_side() - row - 1)
            if square != ch:
                has_won = False
                break

        return has_won

    def can_win_in_rows(self, board: IBoard.IBoard) -> bool:
        """
        Checks if a player can complete a row
        """
        for row in range(board.get_side()):
            player_has_marked = False
            opponent_has_marked = False
            for col in range(board.get_side()):
                square = board.get_square(row, col)
                if square == board.get_player_ch():
                    player_has_marked = True
                elif square == board.get_opponent_ch():
                    opponent_has_marked = True
                if player_has_marked and opponent_has_marked:
                    break

            if not player_has_marked or not opponent_has_marked:
                return True
        return False

    def can_win_in_cols(self, board: IBoard.IBoard) -> bool:
        """
        Checks if a player can complete a column
        """
        for col in range(board.get_side()):
            player_has_marked = False
            opponent_has_marked = False
            for row in range(board.get_side()):
                square = board.get_square(row, col)
                if square == board.get_player_ch():
                    player_has_marked = True
                elif square == board.get_opponent_ch():
                    opponent_has_marked = True
                if player_has_marked and opponent_has_marked:
                    break

            if not player_has_marked or not opponent_has_marked:
                return True
        return False

    def can_win_in_main_diag(self, board: IBoard.IBoard) -> bool:
        """
        Checks if a player can win in the main diagonal
        """
        player_has_marked = False
        opponent_has_marked = False
        for row in range(board.get_side()):
            square = board.get_square(row, row)
            if square == board.get_player_ch():
                player_has_marked = True
            elif square == board.get_opponent_ch():
                opponent_has_marked = True
            if player_has_marked and opponent_has_marked:
                return False

        if not player_has_marked or not opponent_has_marked:
            return True
        return False

    def can_win_in_anti_diag(self, board: IBoard.IBoard) -> bool:
        """
        Checks if a player can win in the anti-diagonal
        """
        player_has_marked = False
        opponent_has_marked = False
        for row in range(board.get_side()):
            square = board.get_square(row, board.get_side() - row - 1)
            if square == board.get_player_ch():
                player_has_marked = True
            elif square == board.get_opponent_ch():
                opponent_has_marked = True
            if player_has_marked and opponent_has_marked:
                return False

        if not player_has_marked or not opponent_has_marked:
            return True
        return False

    def is_winnable(self, board: IBoard.IBoard) -> bool:
        """
        Check if the game can still be one by either of the players
        """
        # check rows
        if self.can_win_in_rows(board):
            return True

        # check cols
        if self.can_win_in_cols(board):
            return True

        # check main diagonal
        if self.can_win_in_main_diag(board):
            return True

        # check anti-diagonal
        return self.can_win_in_anti_diag(board)

    def get_final_move(self, board: IBoard.IBoard) -> (int, int):
        """
        Checks if a single move remains and
        returns it's (row, col)
        """
        final_row = -1
        final_col = -1
        for row in range(board.get_side()):
            for col in range(board.get_side()):
                square = board.get_square(row, col)
                if square == board.get_empty_square():
                    if final_row == -1 and final_col == -1:
                        final_row = row
                        final_col = col
                    else:
                        return -1, -1

        return final_row, final_col

    def is_draw(self, board: IBoard.IBoard, player_ch: str) -> bool:
        """
        Checks if the game will end in a draw
        regardless of the moves made
        The player with symbol player_ch must make the next move
        """
        # check if invalid player symbol is provided
        if player_ch != board.get_player_ch() and player_ch != board.get_opponent_ch():
            return False

        # the game cannot be won by either player
        if not self.is_winnable(board):
            return True

        # check if a single move remains
        final_move = self.get_final_move(board)
        if final_move != (-1, -1):
            board.set_square(final_move[0], final_move[1], player_ch)
            # check the result after the last remaining move is made
            result = self.get_game_result(board)
            # if the result is a draw, return True
            if result == 0:
                return True

        return False

    def get_game_result(self, board: IBoard.IBoard) -> int:
        """
        Accepts a board class
        Calculates the game result given the board state
        Returns 1  - if the player has won the game,
               -1  - if the player has lost the game,
                0  - if the game is a draw, or incomplete
        """
        if self.check_win(board, board.get_player_ch()):
            return 1

        if self.check_win(board, board.get_opponent_ch()):
            return -1

        return 0

    def get_optimal_move(self, board: IBoard.IBoard, move_cnt: int) -> (int, int, int, int):
        """
        Accepts a board class and number of moves made
        Finds the optimal move by trying all available
        moves and comparing results
        Returns: result type, moves until game end, optimal row, optimal col
        """

        game_result = self.get_game_result(board)

        # if no more moves can be made return the result
        if move_cnt > board.get_side() * board.get_side():
            return game_result, move_cnt, -1, -1

        # if a player has won the game
        if game_result != 0:
            return game_result, move_cnt, -1, -1

        # find the move resulting in: the fastest win,
        # a draw, or the slowest loss
        max_move_cnt = board.get_side() * board.get_side() + 2
        can_win = False
        can_draw = False
        # minimal amount of moves until win
        min_moves = max_move_cnt
        # maximal amount of moves until loss
        max_moves = -1
        opt_row = -1
        opt_col = -1

        for row in range(board.get_side()):
            for col in range(board.get_side()):
                square = board.get_square(row, col)

                if square == board.get_empty_square():
                    board.set_square(row, col, board.get_player_ch())

                    # reverse the players
                    board.reverse_players()

                    # get the opponent's result if our next move is (row, col)
                    result = self.get_optimal_move(board, move_cnt + 1)

                    # revert changes made
                    board.reverse_players()
                    board.set_square(row, col, board.get_empty_square())

                    # the opponent loses from the next game state
                    # we win by making the move (row, col)
                    # check if this move ends the game faster
                    # than the previous fastest wining move
                    if result[0] == -1 and result[1] < min_moves:
                        can_win = True
                        min_moves = result[1]
                        opt_row = row
                        opt_col = col

                    # the result is a draw and a wining move isn't found yet
                    if result[0] == 0 and not can_win:
                        can_draw = True
                        opt_row = row
                        opt_col = col

                    # a move resulting in a win or a draw isn't found yet
                    # we want to lose in as many moves as possible
                    if result[0] == 1 and not can_win and not can_draw and max_moves < result[1]:
                        max_moves = result[1]
                        opt_row = row
                        opt_col = col

        # a winning move exists
        if can_win:
            return 1, min_moves, opt_row, opt_col

        # there is no winning move,
        # and we can force a draw
        if can_draw:
            return 0, move_cnt, opt_row, opt_col

        # we lose from the current game state
        return -1, max_moves, opt_row, opt_col
