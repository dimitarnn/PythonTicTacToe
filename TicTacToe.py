import os


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
        self.empty_square = ' . '
        self.side = side
        self.rows = [[self.empty_square for i in range(side)] for i in range(side)]

    def print_board(self):
        """
        Print the current game state
        """
        print('')
        separator = '_' * (4 * self.side - 1)

        # print first row
        row = self.rows[0]
        line = row[0]
        for el in row[1:]:
            line += '|{0}'.format(el)
        print(line)
        print(separator)

        # print middle rows
        for row in self.rows[1:-1]:
            line = row[0]
            for el in row[1:]:
                line += '|{0}'.format(el)
            print(line)
            print(separator)

        # print last row
        row = self.rows[-1]
        line = row[0]
        for el in row[1:]:
            line += '|{0}'.format(el)
        print(line)
        print('')

    def set_square(self, x, y, ch):
        """
        Set the square at (x, y) to ch
        x, y are between 0 and side - 1
        """
        self.rows[x][y] = ' {0} '.format(ch)

    def player_make_move(self, x, y):
        """
        Make player move at
        row - x
        column - y
        player character - ch
        """
        try:
            if x < 1 or y < 1 or x > self.side or y > self.side:
                raise IndexError

            tmp_square = self.rows[x - 1][y - 1]

            if tmp_square != self.empty_square:
                print('Invalid input!')
                print('Target square is already taken!')
                return

            # print('Square:' + tmp_square)
            self.set_square(x - 1, y - 1, self.player_ch)

        except IndexError:
            print('Invalid input!')
            print('Row and column indexes must be between 1 and {0}'.format(self.side))

    def check_win(self, ch):
        """
        Check if the player with 'ch' can win on their next turn
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

        return -1, -1

    def computer_make_move(self):
        """
        Simulates the computer move
        """
        # check if the computer can win on this turn
        computer_move = self.check_win(self.computer_ch)
        print('Computer move: ', computer_move)
        if computer_move != (-1, -1):
            self.set_square(computer_move[0], computer_move[1], self.computer_ch)

        # check if the player wins on their next move
        player_move = self.check_win(self.player_ch)
        print('Player move: ', player_move)
        if player_move != (-1, -1):
            self.set_square(player_move[0], player_move[1], self.computer_ch)





