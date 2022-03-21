import GameLogic


class TicTacToe(GameLogic.GameLogic):
    """
    Tic Tac Toe game class
    """

    def __init__(self, side=3):
        """
        Initialize rows
        Board side is 3 by default
        """
        super(TicTacToe, self).__init__(side)

    def player_make_move(self, x, y):
        """
        Make player move at (x, y)
        returns true if the move is valid
        """
        try:
            if x < 1 or y < 1 or x > self.side or y > self.side:
                raise IndexError

            tmp_square = self.rows[x - 1][y - 1]

            if tmp_square != self.empty_square:
                print('Invalid input!')
                print('Target square is already taken!')
                return False

            # print('Square:' + tmp_square)
            self.set_square(x - 1, y - 1, self.player_ch)
            return True

        except IndexError:
            print('Invalid input!')
            print('Row and column indexes must be between 1 and {0}'.format(self.side))
            return False

    def play(self):
        """
        Simulates a game in which the user moves first
        """
        print("-- Welcome to the game! --")
        print("~" * 40)
        print('')
        self.print_board()
        move_cnt = 0

        while move_cnt < self.side * self.side:
            # the player makes a move
            is_valid = False
            while not is_valid:
                print('Your turn!')

                try:
                    x = int(input("Enter a row: "))
                    y = int(input("Enter a column: "))
                    is_valid = self.player_make_move(x, y)
                except SyntaxError:
                    print('Invalid input')
                except ValueError:
                    print('Invalid input!')
                    print('Enter a number for row and column!')

            move_cnt += 1
            self.print_board()

            # check if the player has won
            has_won = self.check_win(self.rows, self.player_ch)
            if has_won:
                self.print_player_wins()
                break

            # check if the board is completed
            if move_cnt >= self.side * self.side:
                self.print_draw()
                break

            # find the computer's move
            optimal_move = self.get_optimal_move(self.rows, move_cnt + 1, self.computer_ch, self.player_ch)
            result = optimal_move[0]
            computer_x = optimal_move[1]
            computer_y = optimal_move[2]
            move_cnt += 1

            if result == -1:
                self.print_player_wins()
                break
            elif result == 0:
                self.set_square(computer_x, computer_y, self.computer_ch)
                print(self.computer_move_message.format(*(computer_x, computer_y)))
            else:
                self.set_square(computer_x, computer_y, self.computer_ch)
                print(self.computer_move_message.format(*(computer_x + 1, computer_y + 1)))

            self.print_board()

            # check if the computer wins
            has_won = self.check_win(self.rows, self.computer_ch)
            if has_won:
                self.print_computer_wins()
                break

            # check if the board is filled
            if move_cnt >= self.side * self.side:
                self.print_draw()
                break

        print("Game over!")
