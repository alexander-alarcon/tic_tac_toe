from tic_tac_toe.game.base import BaseTicTacToe
from tic_tac_toe.player.base import Player


class ClassicTicTacToe(BaseTicTacToe):
    def __init__(self, player_x: Player, player_o: Player) -> None:
        super().__init__(player_x, player_o)

    def play(self) -> None:
        super().play()
