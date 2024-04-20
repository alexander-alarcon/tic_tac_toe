from abc import abstractmethod
from queue import Queue
from random import choice
from typing import NamedTuple

from tic_tac_toe.player.base import Player


class Move(NamedTuple):
    player: Player
    cell: int


type PlayerOrNone = Player | None
type Board = list[list[PlayerOrNone]]


class BaseTicTacToe:
    """Base class for a Tic Tac Toe game."""

    def __init__(self, player_x: Player, player_o: Player) -> None:
        """
        Initializes a new instance of the BaseTicTacToeGame class.

        Args:
            player_x (Player): The player who represents 'X' on the game board.
            player_o (Player): The player who represents 'O' on the game board.
        """

        self.player_x: Player = player_x
        self.player_o: Player = player_o

        self.board: Board = [[None] * 3 for _ in range(3)]
        self._current_player: Player = choice([self.player_x, self.player_o])
        self._winner: PlayerOrNone = None
        self._move_history: Queue[Move] = Queue()

    @property
    def winner(self) -> PlayerOrNone:
        """
        Get the winner of the game.

        Returns:
            Player | None: The winner of the game, or None if there is no winner
        """
        return self._winner

    @property
    def game_over(self) -> bool:
        """
        Check if the game is over.

        Returns:
            bool: True if the game is over
                  (either there is a winner or it's a tie), False otherwise.
        """
        return self.winner is not None or self.check_tie()

    @property
    def current_player(self) -> Player:
        """
        Get the current player.

        Returns:
            Player: The current player.
        """
        return self._current_player

    def display_board(self) -> None:
        """
        Display the current state of the game board.
        """
        for row in range(3):
            for col in range(3):
                print(f'{self.board[row][col] or "-"}', end=' ')

            print()

    def check_win(self, current_player: PlayerOrNone = None) -> bool:
        """
        Check if there's a winner in the current game state.

        Returns:
            bool: True if there's a winner, False otherwise.
        """
        if current_player is None:
            current_player = self.current_player

        # Check rows and columns
        for row_index in range(3):
            if (
                self.board[row_index][0]
                == self.board[row_index][1]
                == self.board[row_index][2]
                is current_player
                or self.board[0][row_index]
                == self.board[1][row_index]
                == self.board[2][row_index]
                is current_player
            ):
                return True

        # Check diagonals
        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2] is not None
            or self.board[0][2]
            == self.board[1][1]
            == self.board[2][0]
            is current_player
        ):
            return True

        return False

    def check_tie(self) -> bool:
        """
        Check if the game is a tie.

        Returns:
            bool: True if the game is a tie, False otherwise.
        """
        return all(
            self.board[row][col] is not None
            for row in range(3)
            for col in range(3)
        )

    def print_results(self) -> None:
        """
        Print the results of the game.
        """
        if self.check_tie():
            print("It's a tie!")

        if self.winner is not None:
            print(f'Player {self.winner} won!')

    def is_valid_move(self, cell: int) -> bool:
        """
        Check if a move is valid.

        Args:
            cell (int): The cell number where the move is to be made.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        if cell < 1 or cell > 9:
            return False

        cell -= 1

        row = cell // 3
        col = cell % 3

        return self.board[row][col] is None

    @abstractmethod
    def play(self) -> None:
        """
        Method that represents the main gameplay logic.
        """
        print(f'Current player: {self._current_player}')

        move = -1

        while True:
            move = self._current_player.make_move(board=self.board)
            if self.is_valid_move(move):
                break

            print('Invalid move')

        self._before_move(move)
        self._set_move(move)
        self.display_board()
        self._after_move(move)

    @abstractmethod
    def _before_move(self, move: int) -> None:
        """
        Perform any necessary operations before a move is made.
        """
        self._move_history.put((self._current_player, move))

    @abstractmethod
    def _after_move(self, _move: int) -> None:
        """
        Perform any necessary operations after a move is made.

        Parameters:
            _move (int): The move that was made.
        """
        if self.check_win():
            self._winner = self._current_player

        elif self.check_tie():
            self._winner = None

        self._current_player = (
            self.player_x
            if self._current_player == self.player_o
            else self.player_o
        )

    def _set_move(self, cell: int) -> None:
        """
        Set the move made by a player on the board.

        Args:
            cell (int): The cell number where the move is made.
            player (Player): The player making the move.
        """
        cell -= 1

        row = cell // 3
        col = cell % 3
        self.board[row][col] = self._current_player

    def __repr__(self) -> str:
        """
        Get a string representation of the game object.

        Returns:
            str: String representation of the game object.
        """
        attributes = ',\n\t'.join(
            f'{attr}={getattr(self, attr)!s}' for attr in self.__dict__
        )
        return f'TicTacToe(\n\t{attributes}\n)'
