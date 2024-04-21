from enum import Enum

from tic_tac_toe.game_type.base import BaseTicTacToe
from tic_tac_toe.game_type.classic import ClassicTicTacToe
from tic_tac_toe.game_type.limited import LimitedMemoryTicTacToe
from tic_tac_toe.player.base import Player


class GameChoice(Enum):
    QUIT = 0
    CLASSIC = 1
    LIMITED = 2


class GameSetup:
    def __init__(self, player: Player, opponent: Player) -> None:
        self.player = player
        self.opponent = opponent

    def initialize_game(self) -> BaseTicTacToe:
        while True:
            try:
                print('\nWhich kind of play do you want?')
                print('1. Classic')
                print('2. Limited memory')
                print('0. Quit')

                game_choice: int = int(input('Enter your choice: '))

                match game_choice:
                    case GameChoice.CLASSIC.value:
                        return ClassicTicTacToe(
                            player=self.player, opponent=self.opponent
                        )
                    case GameChoice.LIMITED.value:
                        return LimitedMemoryTicTacToe(
                            player=self.player,
                            opponent=self.opponent,
                        )
                    case GameChoice.QUIT.value:
                        raise SystemExit
                    case _:
                        raise ValueError

            except ValueError:
                print('Invalid input. Please enter a number between 0 and 2.')
