import TicTacToe as game
import Board
import GameLogic

if __name__ == '__main__':

    board = Board.BoardText()
    logic = GameLogic.GameLogicRecursive()

    tmp_game = game.TicTacToe(game_logic=logic, game_gui=board)
    tmp_game.play()
