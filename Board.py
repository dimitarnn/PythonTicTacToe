from abc import abstractmethod


class IBoard(object):
    """
    Board Interface
    """

    def __init__(self):
        pass
    
    @abstractmethod
    def get_side(self):
        pass
    
    @abstractmethod
    def get_player_move(self):
        pass

    @abstractmethod
    def show_message(self, message):
        pass

    @abstractmethod
    def show_move_message(self, player_name, row, col):
        pass

    @abstractmethod
    def display_board(self):
        pass

    @abstractmethod
    def reverse_players(self):
        pass
    
    @abstractmethod
    def get_player_ch(self):
        pass
    
    @abstractmethod
    def set_player_ch(self, ch):
        pass
    
    @abstractmethod
    def get_opponent_ch(self):
        pass
    
    @abstractmethod
    def set_opponent_ch(self, ch):
        pass

    @abstractmethod
    def get_square(self, row, col):
        pass

    @abstractmethod
    def set_square(self, row, col, ch):
        pass

    @abstractmethod
    def display_player_wins(self):
        pass

    @abstractmethod
    def display_opponent_wins(self):
        pass

    @abstractmethod
    def display_game_is_draw(self):
        pass


class BoardGraphic(IBoard):
    def get_side(self):
        pass
    
    def get_player_ch(self):
        pass

    def get_opponent_ch(self):
        pass

    def show_message(self, message):
        pass

    def show_move_message(self, player_name, row, col):
        pass

    def display_board(self):
        pass

    def reverse_players(self):
        pass

    def set_player_ch(self, ch):
        pass

    def set_opponent_ch(self, ch):
        pass

    def get_square(self, row, col):
        pass

    def set_square(self, row, col, ch):
        pass

    def display_player_wins(self):
        pass

    def display_opponent_wins(self):
        pass

    def display_game_is_draw(self):
        pass

    def get_player_move(self):
        pass


class BoardText(IBoard):
    """
    Board class
    """

    def __init__(self, side=3, player_ch='X', opponent_ch='O'):
        """
        Initialize rows, player and opponent symbol
        Board side is 3 by default
        """
        super(BoardText, self).__init__()

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
        self.rows = [[self.empty_square for _ in range(side)] for _ in range(side)]
        self.move_message = "{0} marks square: ({1}, {2})."
    
    def get_side(self):
        """
        Returns the board side
        """
        return self.side
    
    def get_player_move(self):
        """
        Reads and returns the player move from input
        """
        result = -1, -1
        try:
            row = int(input("Enter a row: "))
            col = int(input("Enter a column: "))
            result = row, col

        except Exception:
            result = -1, -1

        finally:
            return result

    def show_message(self, message):
        """
        Shows a message to the user
        """
        print(message)

    def show_move_message(self, player_name, row, col):
        """
        Shows a message describing the player's move
        """
        self.show_message(self.move_message.format(player_name, row, col))

    def display_board(self):
        """
        Display the given game state
        """
        self.show_message('')
        separator = '_' * (4 * self.side - 1)

        # display the first row
        row = self.rows[0]
        line = " {0} ".format(row[0])
        for square in row[1:]:
            line += '| {0} '.format(square)
        self.show_message(line)
        self.show_message(separator)

        # display middle rows
        for row in self.rows[1:-1]:
            line = " {0} ".format(row[0])
            for square in row[1:]:
                line += '| {0} '.format(square)
            self.show_message(line)
            self.show_message(separator)

        # display the last row
        row = self.rows[-1]
        line = " {0} ".format(row[0])
        for square in row[1:]:
            line += '| {0} '.format(square)
        self.show_message(line)
        self.show_message('')

    def reverse_players(self):
        """
        Swaps the player's and the opponent's symbols
        """
        tmp_player_ch = self.player_ch
        self.set_player_ch(self.opponent_ch)
        self.set_opponent_ch(tmp_player_ch)
    
    def get_player_ch(self):
        """
        Returns the player's symbol
        """
        return self.player_ch
    
    def set_player_ch(self, ch):
        """
        Sets the value of the player symbol
        """
        self.player_ch = ch
    
    def get_opponent_ch(self):
        """
        Returns the opponent's symbol
        """
        return self.opponent_ch
    
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

    def display_player_wins(self):
        """
        Displays a victory message
        """
        self.show_message("You have won!!!")

    def display_opponent_wins(self):
        """
        Displays a defeat message
        """
        self.show_message("You lose!")

    def display_game_is_draw(self):
        """
        Displays a draw message
        """
        self.show_message("Draw!")
