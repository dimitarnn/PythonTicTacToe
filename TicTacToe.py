class TicTacToe(object):
    """
    Tic Tac Toe game class
    """

    def __init__(self, game_logic, game_gui):
        """
        Initialize helper classes
        with board side and player symbol
        Board side is 3 by default
        """
        # super(TicTacToe, self).__init__(side)
        self.board = game_gui
        self.game_logic = game_logic

    def player_make_move(self, row, col):
        """
        Make player move at (row, col)
        returns true if the move is valid
        """
        try:
            if row < 1 or col < 1 or row > self.board.side or col > self.board.side:
                raise IndexError

            tmp_square = self.board.get_square(row - 1, col - 1)

            if tmp_square != self.board.empty_square:
                self.board.show_message('Invalid input!')
                self.board.show_message('Target square is already taken!')
                return False

            self.board.set_square(row - 1, col - 1, self.board.player_ch)
            return True

        except IndexError:
            self.board.show_message('Invalid input!')
            self.board.show_message('Row and column indexes must be between 1 and {0}'.format(self.board.side))
            return False

    def play(self):
        """
        Simulates a game in which the user moves first
        """
        self.board.show_message("-- Welcome to the game! --")
        self.board.show_message("~" * 40)
        self.board.show_message('')
        self.board.display_board()
        move_cnt = 0
        row = 0
        col = 0

        while move_cnt < self.board.side * self.board.side:
            # the player makes a move
            is_valid = False
            while not is_valid:
                self.board.show_message('Your turn!')

                try:
                    row, col = self.board.get_player_move()
                    is_valid = self.player_make_move(row, col)
                except SyntaxError:
                    self.board.show_message('Invalid input')
                except ValueError:
                    self.board.show_message('Invalid input!')
                    self.board.show_message('Enter a number for row and column!')

            move_cnt += 1

            # TODO: Simplify and do not use the attribute directly
            self.board.show_message(self.board.move_message.format("Player", row, col))
            self.board.display_board()

            # check if the player has won
            has_won = self.game_logic.check_win(self.board, self.board.player_ch)
            if has_won:
                self.board.display_player_wins()
                break

            # check if the board is completed
            if move_cnt >= self.board.side * self.board.side:
                self.board.display_game_is_draw()
                break

            # check if the game inevitably results in a draw
            if self.game_logic.is_draw(self.board, self.board.opponent_ch):
                self.board.display_game_is_draw()
                break

            # find the computer's move
            # reverse the players' symbols => it's the opponent's turn
            self.board.reverse_players()
            optimal_move = self.game_logic.get_optimal_move(self.board, move_cnt + 1)
            result = optimal_move[0]
            computer_row = optimal_move[2]
            computer_col = optimal_move[3]
            move_cnt += 1

            # revert changes
            self.board.reverse_players()

            if result == -1:
                self.board.display_player_wins()
                break
            elif result == 0:

                self.board.set_square(computer_row, computer_col, self.board.opponent_ch)

                # TODO: Simplify and do not use the attribute directly
                self.board.show_message(self.board.move_message.format("The Computer", computer_row + 1, computer_col + 1))
            else:
                self.board.set_square(computer_row, computer_col, self.board.opponent_ch)

                # TODO: Simplify and do not use the attribute directly
                self.board.show_message(self.board.move_message.format("The Computer", computer_row + 1, computer_col + 1))

            self.board.display_board()

            # check if the computer wins
            has_won = self.game_logic.check_win(self.board, self.board.opponent_ch)
            if has_won:
                self.board.display_opponent_wins()
                break

            # check if the board is filled
            if move_cnt >= self.board.side * self.board.side:
                self.board.display_game_is_draw()
                break

            # check if the game inevitably results in a draw
            if self.game_logic.is_draw(self.board, self.board.player_ch):
                self.board.display_game_is_draw()
                break

        self.board.show_message("Game over!")
