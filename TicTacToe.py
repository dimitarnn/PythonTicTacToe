class TicTacToe(object):
    """
    Tic Tac Toe game class
    """

    def __init__(self, side=3):
        """
        Initialize rows
        Board side is 3 by default
        """
        self.player_ch = '0'
        self.computer_ch = 'X'
        self.empty_square = '.'
        self.side = side
        self.rows = [[self.empty_square for i in range(side)] for i in range(side)]
        self.remaining_squares_in_row = []
        self.remaining_squares_in_column = []
        self.remaining_in_diagonals = []
        self.computer_move_message = "The Computer marks square: ({0}, {1})."

    def print_board(self):
        """
        Print the current game state
        """
        print('')
        separator = '_' * (4 * self.side - 1)

        # print first row
        row = self.rows[0]
        line = " {0} ".format(row[0])
        for el in row[1:]:
            line += '| {0} '.format(el)
        print(line)
        print(separator)

        # print middle rows
        for row in self.rows[1:-1]:
            line = " {0} ".format(row[0])
            for el in row[1:]:
                line += '| {0} '.format(el)
            print(line)
            print(separator)

        # print last row
        row = self.rows[-1]
        line = " {0} ".format(row[0])
        for el in row[1:]:
            line += '| {0} '.format(el)
        print(line)
        print('')

    def set_square(self, x, y, ch):
        """
        Set the square at (x, y) to ch
        x, y are between 0 and side - 1
        """
        self.rows[x][y] = '{0}'.format(ch)

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

    def precompute_remaining_squares(self, ch):
        """
        Finds the remaining squares to completely fill
        a column, row or a diagonal with the symbol 'ch'
        """
        self.remaining_squares_in_row = []
        self.remaining_squares_in_column = []
        self.remaining_in_diagonals = []

        print("Precomputing remaining squares: ")

        # precompute for each row
        for i in range(self.side):
            cnt_marked = 0
            is_blocked = False
            print("Row: ", self.rows[i])

            for j in range(self.side):
                el = self.rows[i][j]
                if el != self.empty_square and el != ch:
                    is_blocked = True
                    break

                if el == ch:
                    cnt_marked += 1

            if is_blocked:
                self.remaining_squares_in_row.append(-1)
            else:
                self.remaining_squares_in_row.append(self.side - cnt_marked)

        print("Precomputed rows: ", self.remaining_squares_in_row)

        # precompute for each column
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
                self.remaining_squares_in_column.append(-1)
            else:
                self.remaining_squares_in_column.append(self.side - cnt_marked)

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

        self.remaining_in_diagonals.append(remaining_in_main_diagonal)

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

        self.remaining_in_diagonals.append(remaining_in_antidiagonal)

    def find_optimal_move(self, ch):
        """
        Finds the best move for the player with symbol 'ch'
        """
        self.precompute_remaining_squares(ch)
        available_squares = []

        # calculate the available paths for each square
        for i in range(self.side):
            #print("Row: {0}".format(i))
            #print(self.remaining_squares_in_row)

            for j in range(self.side):
                if self.rows[i][j] != self.empty_square:
                    continue

                rem_rows = self.remaining_squares_in_row[i]
                rem_columns = self.remaining_squares_in_column[j]
                tmp_list = []

                # print("Row: {0}, Col: {1}".format(i, j))
                # print("Rem rows: {0}".format(rem_rows))
                # print("Rem cols: {0}".format(rem_columns))

                if rem_rows != -1:
                    tmp_list.append(rem_rows)

                if rem_columns != -1:
                    tmp_list.append(rem_columns)

                if i == j and self.remaining_in_diagonals[0] != -1:
                    tmp_list.append(self.remaining_in_diagonals[0])

                if i == self.side - i and self.remaining_in_diagonals[1] != -1:
                    tmp_list.append(self.remaining_in_diagonals[1])

                if tmp_list:
                    tmp_list.sort(reverse=True)
                    available_squares.append({"x": i, "y": j, "list": tmp_list})

        # if the computer cannot win fill the first empty square
        if not available_squares:
            for i in range(self.side):
                for j in range(self.side):
                    if self.rows[i][j] == self.empty_square:
                        return tuple([i, j])

        # sort the list of available squares
        available_squares.sort(key=lambda x: x["list"][0], reverse=True)
        available_squares.sort(key=lambda x: len(x["list"]), reverse=True)

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
        print('Computer winning move: ', computer_move)
        if computer_move != (-1, -1):
            self.set_square(computer_move[0], computer_move[1], self.computer_ch)
            computer_move = tuple(x + 1 for x in computer_move)
            print(self.computer_move_message.format(*computer_move))
            return

        # check if the player wins on their next move
        player_move = self.get_winning_pos(self.player_ch)
        print('Player winning move: ', player_move)
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
            print(i, self.side - i)
            el = self.rows[i][self.side - i - 1]
            if el != ch:
                has_won = False
                break

        return has_won

    def print_player_wins(self):
        """
        Prints a message that the player has won
        """
        print("You have won!!!")

    def print_computer_wins(self):
        """
        Prints a message that the computer has won
        """
        print("You lose!")

    def print_draw(self):
        """
        Prints a message that the game is a draw
        """
        print("Draw!")

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
                    remaining_moves -= 1
                except SyntaxError:
                    print('Invalid input')

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
