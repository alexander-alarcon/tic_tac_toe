from tic_tac_toe.game_type.base import BaseTicTacToe, Move
from tic_tac_toe.player.base import Player


class BlindTicTacToe(BaseTicTacToe):
    def __init__(
        self,
        player: Player,
        opponent: Player,
    ) -> None:
        """
        Initializes a new instance of the BlindTicTacToe class.

        Args:
            player (Player): The player.
            opponent (Player): The opponent.
        """
        super().__init__(player, opponent)
        self._firsts_moves: list[Move] = []

    def display_board(self) -> None:
        """
        Display the board but only the first two moves.
        """
        board = [['-' for _ in range(3)] for _ in range(3)]

        for move in self._firsts_moves:
            row, col = divmod(move.cell - 1, 3)
            board[row][col] = move.player

        for row in range(3):
            for col in range(3):
                print(f'{board[row][col] or "-"}', end=' ')

            print()

    def play(self) -> None:
        print(f'Current player: {self._current_player}')

        move = -1

        while True:
            move = self._current_player.make_move(
                board=self.board,
                hide_move=True,
            )
            if not self.is_valid_move(move):
                print(
                    'Invalid move',
                    f'{self._current_player} has lost the turn.',
                )
            break

        self._before_move(move)
        self._set_move(move)
        self.display_board()
        self._after_move(move)

    def print_results(self) -> None:
        if BaseTicTacToe.check_tie(board=self.board):
            print("It's a tie!")

        if self.winner is not None:
            print(f'Player {self.winner} won!')

        super().display_board()

    def _before_move(self, move: int) -> None:
        """
        Saves the first move of each player.

        Parameters:
            move (int): The cell number where the move is made.
        """
        super()._before_move(move)

        if len(self._firsts_moves) < 2:
            self._firsts_moves.append(
                Move(
                    player=self._current_player,
                    cell=move,
                )
            )
