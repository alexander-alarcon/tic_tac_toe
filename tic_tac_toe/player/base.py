from abc import ABC, abstractmethod
from enum import StrEnum

type PlayerOrNone = Player | None
type Board = list[list[PlayerOrNone]]
type BoardOrNone = Board | None


class PlayerSymbol(StrEnum):
    X = 'X'
    O = 'O'


class Player(ABC):
    def __init__(self, symbol: PlayerSymbol) -> None:
        """
        Initializes a new instance of the class.

        Args:
            symbol (PlayerSymbol): The symbol associated with the player.
        """
        self.symbol = symbol

    def __str__(self) -> str:
        return f'{self.symbol.value}'

    def __repr__(self) -> str:
        return f'Player(symbol={self.symbol.value!r})'

    @abstractmethod
    def make_move(self, board: BoardOrNone) -> int:
        """
        Makes player move.

        Args:
            board (BoardOrNone): The current state of the board.

        Returns:
            int: The index of the cell where the move was made.
        """
        raise NotImplementedError('Player.make_move() not implemented')
