from abc import (
    ABC,
    abstractmethod
)

import IBoard


class IGameLogic(ABC):
    """
    Game Logic Interface
    """
    def __init__(self):
        pass

    @abstractmethod
    def check_win(self, board: IBoard.IBoard, ch: str) -> bool:
        pass

    @abstractmethod
    def can_win_in_rows(self, board: IBoard.IBoard) -> bool:
        pass

    @abstractmethod
    def can_win_in_cols(self, board: IBoard.IBoard) -> bool:
        pass

    @abstractmethod
    def can_win_in_main_diag(self, board: IBoard.IBoard) -> bool:
        pass

    @abstractmethod
    def can_win_in_anti_diag(self, board: IBoard.IBoard) -> bool:
        pass

    @abstractmethod
    def is_winnable(self, board: IBoard.IBoard) -> bool:
        pass

    @abstractmethod
    def get_final_move(self, board: IBoard.IBoard) -> (int, int):
        pass

    @abstractmethod
    def is_draw(self, board: IBoard.IBoard, player_ch: str) -> bool:
        pass

    @abstractmethod
    def get_game_result(self, board: IBoard.IBoard) -> int:
        pass

    @abstractmethod
    def get_optimal_move(self, board: IBoard.IBoard, move_cnt: int) -> (int, int, int, int):
        pass
