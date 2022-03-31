from abc import (
    ABC,
    abstractmethod
)


class IBoard(ABC):
    """
    Board Interface
    """

    def __init__(self):
        pass

    @abstractmethod
    def get_side(self) -> int:
        pass

    @abstractmethod
    def get_empty_square(self) -> str:
        pass

    @abstractmethod
    def get_player_move(self) -> tuple[int, int]:
        pass

    @abstractmethod
    def show_message(self, message: str) -> None:
        pass

    @abstractmethod
    def show_move_message(self, player_name: str, row: int, col: int) -> None:
        pass

    @abstractmethod
    def display_board(self) -> None:
        pass

    @abstractmethod
    def reverse_players(self) -> None:
        pass

    @abstractmethod
    def get_player_ch(self) -> str:
        pass

    @abstractmethod
    def set_player_ch(self, ch: str) -> None:
        pass

    @abstractmethod
    def get_opponent_ch(self) -> str:
        pass

    @abstractmethod
    def set_opponent_ch(self, ch: str) -> None:
        pass

    @abstractmethod
    def get_square(self, row: int, col: int) -> str:
        pass

    @abstractmethod
    def set_square(self, row: int, col: int, ch: str) -> None:
        pass

    @abstractmethod
    def display_player_wins(self) -> None:
        pass

    @abstractmethod
    def display_opponent_wins(self) -> None:
        pass

    @abstractmethod
    def display_game_is_draw(self) -> None:
        pass
