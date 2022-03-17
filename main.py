import TicTacToe as game


if __name__ == '__main__':
    tmp_game = game.TicTacToe()

    tmp_game.print_board()
    tmp_game.player_make_move(1, 2)
    tmp_game.print_board()
    tmp_game.computer_make_move()
    tmp_game.print_board()


