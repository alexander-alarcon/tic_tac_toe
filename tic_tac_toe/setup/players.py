from enum import Enum

from tic_tac_toe.player.base import Player, PlayerOrNone, PlayerSymbol
from tic_tac_toe.player.human import Human


class SymbolChoice(Enum):
    QUIT = 0
    X = 1
    O = 2


class OpponentChoice(Enum):
    QUIT = 0
    HUMAN_OPPONENT = 1


class PlayersSetup:
    def __init__(self) -> None:
        self.player: PlayerOrNone = None
        self.opponent: PlayerOrNone = None

    def initialize_players(self) -> tuple[Player, Player]:
        self._choose_symbol()
        self._choose_opponent()

        return self.player, self.opponent

    def _choose_symbol(self) -> None:
        while True:
            try:
                print('\nChoose your symbol')
                print('1. X')
                print('2. O')
                print('0. Quit')

                symbol_choice = int(input('Enter your choice: '))

                match symbol_choice:
                    case SymbolChoice.X.value:
                        self.player = Human(symbol=PlayerSymbol.X)
                        break
                    case SymbolChoice.O.value:
                        self.player = Human(symbol=PlayerSymbol.O)
                        break
                    case SymbolChoice.QUIT.value:
                        raise SystemExit
                    case _:
                        raise ValueError
            except ValueError:
                print('Invalid input. Please enter a number between 0 and 2.')

    def _choose_opponent(self) -> None:
        opponent_symbol = (
            PlayerSymbol.X
            if self.player.symbol == PlayerSymbol.O
            else PlayerSymbol.O
        )
        self.opponent = Human(symbol=opponent_symbol)
