import Board


class TicTacToe(Board.Board):
    """
    Tic Tac Toe game class
    """

    def __init__(self, side=3):
        """
        Initialize rows
        Board side is 3 by default
        """
        super(TicTacToe, self).__init__(side)
        self.remaining_in_row = []
        self.remaining_in_column = []
        self.remaining_in_diagonal = []
        
        self.blocked_in_row = []
        self.blocked_in_column = []
        self.blocked_in_diagonal = []

    def player_make_move(self, x, y):
        """
        Make player move at
        row - x
        column - y
        player character - ch
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

    def get_winning_pos(self, ch):
        """
        Check if the player with the symbol 'ch' can win on their next turn
        """
        # check rows
        for i in range(self.side):
            flag = True
            pos = -1

            for j in range(self.side):
                el = self.rows[i][j]

                if el != ch and el != self.empty_square:
                    flag = False
                    break

                if el == self.empty_square:
                    if pos != -1:
                        flag = False
                        break
                    else:
                        pos = j

            if flag:
                # tmp player wins
                return i, pos

        # check columns:
        for i in range(self.side):
            flag = True
            pos = -1

            for j in range(self.side):
                el = self.rows[j][i]

                if el != ch and el != self.empty_square:
                    flag = False
                    break

                if el == self.empty_square:
                    if pos != -1:
                        flag = False
                        break
                    else:
                        pos = j

            if flag:
                # tmp player wins
                return pos, i

        # check main diagonal
        flag = True
        pos = -1

        for i in range(self.side):
            el = self.rows[i][i]
            if el != ch and el != self.empty_square:
                flag = False
                break

            if el == self.empty_square:
                if pos != -1:
                    flag = False
                    break
                else:
                    pos = i

        if flag:
            return pos, pos

        # check anti diagonal
        flag = True
        pos = -1

        for i in range(self.side):
            el = self.rows[i][self.side - i - 1]
            if el != ch and el != self.empty_square:
                flag = False
                break

            if el == self.empty_square:
                if pos != -1:
                    flag = False
                    break
                else:
                    pos = i

        if flag:
            return pos, self.side - pos - 1

        return -1, -1

    def precompute_remaining_rows(self, ch):
        """
        Finds the number of remaining squares to fill each row
        """
        # precompute for each row
        self.remaining_in_row = []

        for i in range(self.side):
            cnt_marked = 0
            is_blocked = False
            # print("Row: ", self.rows[i])

            for j in range(self.side):
                el = self.rows[i][j]
                if el != self.empty_square and el != ch:
                    is_blocked = True
                    break

                if el == ch:
                    cnt_marked += 1

            if is_blocked:
                self.remaining_in_row.append(-1)
            else:
                self.remaining_in_row.append(self.side - cnt_marked)

    def precompute_remaining_columns(self, ch):
        """
        Finds the number of remaining squares to fill each column
        """
        # precompute for each column
        self.remaining_in_column = []

        for i in range(self.side):
            cnt_marked = 0
            is_blocked = False

            for j in range(self.side):
                el = self.rows[j][i]
                if el != self.empty_square and el != ch:
                    is_blocked = True
                    break

                if el == ch:
                    cnt_marked += 1

            if is_blocked:
                self.remaining_in_column.append(-1)
            else:
                self.remaining_in_column.append(self.side - cnt_marked)

    def precompute_remaining_diagonals(self, ch):
        """
        Finds the number of remaining squares to fill each diagonal
        """
        self.remaining_in_diagonal = []

        # precompute the value for the main diagonal
        remaining_in_main_diagonal = self.side
        is_blocked = False

        for i in range(self.side):
            el = self.rows[i][i]
            if el != self.empty_square and el != ch:
                is_blocked = True
                break

            if el == ch:
                remaining_in_main_diagonal -= 1

        if is_blocked:
            remaining_in_main_diagonal = -1

        self.remaining_in_diagonal.append(remaining_in_main_diagonal)

        # precompute the value for the antidiagonal
        remaining_in_antidiagonal = self.side
        is_blocked = False

        for i in range(self.side):
            el = self.rows[i][self.side - i - 1]
            if el != self.empty_square and el != ch:
                is_blocked = True
                break

            if el == ch:
                remaining_in_antidiagonal -= 1

        if is_blocked:
            remaining_in_antidiagonal = -1

        self.remaining_in_diagonal.append(remaining_in_antidiagonal)

    def precompute_remaining_squares(self, ch):
        """
        Finds the remaining squares to completely fill
        a column, row or a diagonal with the symbol 'ch'
        """
        self.precompute_remaining_rows(ch)
        self.precompute_remaining_columns(ch)
        self.precompute_remaining_diagonals(ch)

    def precompute_blocked_rows(self, ch):
        """
        Finds the number of remaining squares to fill each row
        """
        # precompute for each row
        self.blocked_in_row = []

        for i in range(self.side):
            cnt_marked = 0
            is_blocked = False
            # print("Row: ", self.rows[i])

            for j in range(self.side):
                el = self.rows[i][j]
                if el == ch:
                    is_blocked = True
                    break

                if el != ch and el != self.empty_square:
                    cnt_marked += 1

            if is_blocked or cnt_marked == 0:
                self.blocked_in_row.append(-1)
            else:
                self.blocked_in_row.append(cnt_marked)

    def precompute_blocked_columns(self, ch):
        """
        Finds the number of remaining squares to fill each column
        """
        # precompute for each column
        self.blocked_in_column = []

        for i in range(self.side):
            cnt_marked = 0
            is_blocked = False

            for j in range(self.side):
                el = self.rows[j][i]
                if el == ch:
                    is_blocked = True
                    break

                if el != ch and el != self.empty_square:
                    cnt_marked += 1

            if is_blocked or cnt_marked == 0:
                self.blocked_in_column.append(-1)
            else:
                self.blocked_in_column.append(cnt_marked)

    def precompute_blocked_diagonals(self, ch):
        """
        Finds the number of remaining squares to fill each diagonal
        """
        self.blocked_in_diagonal = []

        # precompute the value for the main diagonal
        blocked_in_main_diagonal = 0
        is_blocked = False

        for i in range(self.side):
            el = self.rows[i][i]
            if el == ch:
                is_blocked = True
                break

            if el != ch and el != self.empty_square:
                blocked_in_main_diagonal += 1

        if is_blocked or blocked_in_main_diagonal == 0:
            blocked_in_main_diagonal = -1

        self.blocked_in_diagonal.append(blocked_in_main_diagonal)

        # precompute the value for the antidiagonal
        blocked_in_antidiagonal = 0
        is_blocked = False

        for i in range(self.side):
            el = self.rows[i][self.side - i - 1]
            if el == ch:
                is_blocked = True
                break

            if el != ch and el != self.empty_square:
                blocked_in_antidiagonal += 1

        if is_blocked or blocked_in_antidiagonal == 0:
            blocked_in_antidiagonal = -1

        self.blocked_in_diagonal.append(blocked_in_antidiagonal)

    def precompute_blocked_squares(self, ch):
        """
        Precomputes the number of squares player 'ch'
        is blocking if they mark given square
        """
        self.precompute_blocked_rows(ch)
        self.precompute_blocked_columns(ch)
        self.precompute_blocked_diagonals(ch)

    def find_optimal_move(self, ch):
        """
        Finds the best move for the player with symbol 'ch'
        """
        self.precompute_remaining_squares(ch)
        self.precompute_blocked_squares(ch)
        available_squares = []

        # calculate the available paths for each square
        for i in range(self.side):

            for j in range(self.side):
                if self.rows[i][j] != self.empty_square:
                    continue

                # get remaining squares
                rem_rows = self.remaining_in_row[i]
                rem_columns = self.remaining_in_column[j]
                rem_list = []

                if rem_rows != -1:
                    rem_list.append(rem_rows)

                if rem_columns != -1:
                    rem_list.append(rem_columns)

                if i == j and self.remaining_in_diagonal[0] != -1:
                    rem_list.append(self.remaining_in_diagonal[0])

                if j == self.side - i - 1 and self.remaining_in_diagonal[1] != -1:
                    rem_list.append(self.remaining_in_diagonal[1])

                # get blocked squares
                blocked_rows = self.blocked_in_row[i]
                blocked_columns = self.blocked_in_column[j]
                blocked_list = []

                if blocked_rows != -1:
                    blocked_list.append(blocked_rows)

                if blocked_columns != -1:
                    blocked_list.append(blocked_columns)

                if i == j and self.blocked_in_diagonal[0] != -1:
                    blocked_list.append(self.blocked_in_diagonal[0])

                if j == self.side - i - 1 and self.blocked_in_diagonal[1] != -1:
                    blocked_list.append(self.blocked_in_diagonal[1])

                if rem_list or blocked_list:
                    rem_list.sort()
                    blocked_list.sort(reverse=True)

                    if not rem_list:
                        rem_list.append(self.side + 1)
                    if not blocked_list:
                        blocked_list.append(-1)

                    available_squares.append({"x": i, "y": j, "rem": rem_list, "blocked": blocked_list})

        # if the computer cannot win fill the first empty square
        if not available_squares:
            for i in range(self.side):
                for j in range(self.side):
                    if self.rows[i][j] == self.empty_square:
                        return tuple([i, j])

        # sort the list of available squares
        available_squares.sort(key=lambda x: x["rem"][0])
        available_squares.sort(key=lambda x: len(x["rem"]), reverse=True)
        available_squares.sort(key=lambda x: x["blocked"][0], reverse=True)
        available_squares.sort(key=lambda x: len(x["blocked"]), reverse=True)
        #available_squares.sort(key=lambda x: len(x["blocked"]))
        #available_squares.sort(key=lambda x: x["rem"][0])
        #available_squares.sort(key=lambda x: len(x["rem"]), reverse=True)

        print("Finding optimal square: ")
        for item in available_squares:
            print(item)

        return available_squares[0]["x"], available_squares[0]["y"]

    def computer_make_move(self):
        """
        Simulates the computer move
        """
        # check if the computer can win on this turn
        computer_move = self.get_winning_pos(self.computer_ch)
        #print('Computer winning move: ', computer_move)
        if computer_move != (-1, -1):
            self.set_square(computer_move[0], computer_move[1], self.computer_ch)
            computer_move = tuple(x + 1 for x in computer_move)
            print(self.computer_move_message.format(*computer_move))
            return

        # check if the player wins on their next move
        player_move = self.get_winning_pos(self.player_ch)
        #print('Player winning move: ', player_move)
        if player_move != (-1, -1):
            self.set_square(player_move[0], player_move[1], self.computer_ch)
            print(self.computer_move_message.format(*player_move))
            return

        # find the optimal move
        computer_move = self.find_optimal_move(self.computer_ch)
        self.set_square(computer_move[0], computer_move[1], self.computer_ch)
        computer_move = tuple(x + 1 for x in computer_move)
        print(self.computer_move_message.format(*computer_move))

    def check_win(self, ch):
        """
        Check if the player with symbol 'ch' has won the game
        """
        # check rows
        for i in range(self.side):
            has_won = True
            for j in range(self.side):
                el = self.rows[i][j]
                if el != ch:
                    has_won = False
                    break

            if has_won:
                return True

        # check columns
        for i in range(self.side):
            has_won = True
            for j in range(self.side):
                el = self.rows[j][i]
                if el != ch:
                    has_won = False
                    break

            if has_won:
                return True

        # check main diagonal
        has_won = True
        for i in range(self.side):
            el = self.rows[i][i]
            if el != ch:
                has_won = False
                break

        if has_won:
            return True

        # check anti diagonal
        has_won = True
        for i in range(self.side):
            el = self.rows[i][self.side - i - 1]
            if el != ch:
                has_won = False
                break

        return has_won

    def play(self):
        """
        Simulates a game in which the user moves first
        """
        remaining_moves = self.side * self.side

        print("-- Welcome to the game! --")
        print("~" * 40)
        print('')
        self.print_board()

        while remaining_moves > 0:
            # the user makes a move
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

            remaining_moves -= 1
            self.print_board()

            has_won = self.check_win(self.player_ch)
            if has_won:
                self.print_player_wins()
                break

            if remaining_moves <= 0:
                self.print_draw()
                break

            # computer makes a move
            self.computer_make_move()
            remaining_moves -= 1
            self.print_board()

            has_won = self.check_win(self.computer_ch)
            if has_won:
                self.print_computer_wins()
                break

            if remaining_moves <= 0:
                self.print_draw()
                break

        print("Game over!")
