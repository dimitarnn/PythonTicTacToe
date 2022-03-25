class BoardGraphic(object):
    pass


class BoardText(object):
    """
    Board class
    """

    def __init__(self, side=3, player_ch='X', opponent_ch='O'):
        """
        Initialize rows, player and opponent symbol
        Board side is 3 by default
        """
        # the player uses 'X' by default
        self.player_ch = player_ch

        # the opponent uses 'O' by default
        self.opponent_ch = opponent_ch

        # check if the players' symbols are distinct
        # give 'O' to the opponent if it isn't taken
        # give 'X' to the opponent if the player has chosen 'O'
        if self.player_ch == self.opponent_ch:
            self.opponent_ch = 'O'
            if self.player_ch == 'O':
                self.opponent_ch = 'X'

        self.empty_square = '.'
        self.side = side
        self.rows = [[self.empty_square for i in range(side)] for i in range(side)]
        self.move_message = "{0} marks square: ({1}, {2})."

    def print_board(self):
        """
        Print the given game state
        """
        print('')
        separator = '_' * (4 * self.side - 1)

        # print first row
        row = self.rows[0]
        line = " {0} ".format(row[0])
        for square in row[1:]:
            line += '| {0} '.format(square)
        print(line)
        print(separator)

        # print middle rows
        for row in self.rows[1:-1]:
            line = " {0} ".format(row[0])
            for square in row[1:]:
                line += '| {0} '.format(square)
            print(line)
            print(separator)

        # print last row
        row = self.rows[-1]
        line = " {0} ".format(row[0])
        for square in row[1:]:
            line += '| {0} '.format(square)
        print(line)
        print('')

    def reverse_players(self):
        """
        Swaps the player's and the opponent's symbols
        """
        tmp_player_ch = self.player_ch
        self.set_player_ch(self.opponent_ch)
        self.set_opponent_ch(tmp_player_ch)

    def set_player_ch(self, ch):
        """
        Sets the value of the player symbol
        """
        self.player_ch = ch

    def set_opponent_ch(self, ch):
        """
        Sets the value of the opponent symbol
        """
        self.opponent_ch = ch

    def get_square(self, row, col):
        """
        Returns the value of the square
        at position (row, col)
        row, col are between 0 and side - 1
        """
        return self.rows[row][col]

    def set_square(self, row, col, ch):
        """
        Set the square at (row, col) to ch
        row, col are between 0 and side - 1
        """
        self.rows[row][col] = '{0}'.format(ch)

    def print_player_wins(self):
        """
        Prints a message that the player has won
        """
        print("You have won!!!")

    def print_opponent_wins(self):
        """
        Prints a message that the opponent has won
        """
        print("You lose!")

    def print_draw(self):
        """
        Prints a message that the game is a draw
        """
        print("Draw!")
