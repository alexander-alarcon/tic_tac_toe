from tic_tac_toe.game_type.base import BaseTicTacToe
from tic_tac_toe.player.base import Player


class ClassicTicTacToe(BaseTicTacToe):
    def __init__(self, player: Player, opponent: Player) -> None:
        super().__init__(player, opponent)

    def play(self) -> None:
        super().play()
