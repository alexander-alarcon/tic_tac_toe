from enum import StrEnum
from random import choice

from tic_tac_toe.game_type.base import Board

from .base import Player, PlayerSymbol


class IALevel(StrEnum):
    EASY = 'easy'


class IA(Player):
    def __init__(self, symbol: PlayerSymbol, level: IALevel) -> None:
        super().__init__(symbol)
        self.level = level

    def make_move(self, board: Board) -> int:
        """
        Makes a move based on the IA level provided.

        Args:
            board (Board): The current state of the game board.

        Returns:
            int: The index of the cell where the move was made.
        """
        match self.level:
            case IALevel.EASY:
                return self._dumb_move(board)
            case _:
                raise ValueError

    def _dumb_move(self, board: Board) -> int:
        """
        Makes a random move by choosing an available cell on the board.

        Args:
            board (Board): The current state of the game board.

        Returns:
            int: The index of the cell where the move was made.
        """
        available_cells = self._get_available_cells(board=board)
        move = choice(available_cells)

        return move

    def _get_available_cells(self, board: Board) -> list[int]:
        """
        Get a list of available cells on the board.

        Args:
            board (Board): The current state of the game board.

        Returns:
            list[int]: A list of available cell indices,
            where each index is a number between 1 and 9.
        """
        available_cells = []

        for row in range(3):
            for col in range(3):
                if board[row][col] is None:
                    available_cells.append(row * 3 + col + 1)

        return available_cells
