class Board(object):
    """
    Board class
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
