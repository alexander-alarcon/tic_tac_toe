from queue import Queue

from tic_tac_toe.game_type.base import BaseTicTacToe, Move
from tic_tac_toe.player.base import Player


class LimitedMemoryTicTacToe(BaseTicTacToe):
    def __init__(self, player: Player, opponent: Player) -> None:
        super().__init__(player, opponent)
        self._memory: Queue[Move] = Queue()

    def play(self) -> None:
        super().play()

    def _before_move(self, move: int) -> None:
        """
        Puts the move in the memory queue before the move is made.

        Parameters:
            move (int): The cell number where the move is made.
        """
        super()._before_move(move)
        self._memory.put(Move(player=self._current_player, cell=move))

        if self._memory.qsize() == 7:
            self._remove_first()

    def _remove_first(self) -> None:
        """
        Removes the first move from the memory queue and updates the board.
        """
        move: Move = self._memory.get()

        row = (move.cell - 1) // 3
        col = (move.cell - 1) % 3

        self.board[row][col] = None
