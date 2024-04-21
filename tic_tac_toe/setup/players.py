from enum import Enum

from tic_tac_toe.player.base import Player, PlayerOrNone, PlayerSymbol
from tic_tac_toe.player.human import Human
from tic_tac_toe.player.ia import IA, IALevel


class SymbolChoice(Enum):
    QUIT = 0
    X = 1
    O = 2


class OpponentChoice(Enum):
    QUIT = 0
    HUMAN_OPPONENT = 1
    IA_OPPONENT = 2


class IALevelChoice(Enum):
    QUIT = 0
    EASY = 1


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

        while True:
            try:
                print('\nChoose your opponent')
                print('1. Human')
                print('2. IA')
                print('0. Quit')

                opponent_choice = int(input('Enter your choice: '))

                match opponent_choice:
                    case OpponentChoice.HUMAN_OPPONENT.value:
                        self.opponent = Human(symbol=opponent_symbol)
                        break
                    case OpponentChoice.IA_OPPONENT.value:
                        level: IALevel = self._choose_ia_level()
                        self.opponent = IA(symbol=opponent_symbol, level=level)
                        break
                    case OpponentChoice.QUIT.value:
                        raise SystemExit
                    case _:
                        raise ValueError
            except ValueError:
                print('Invalid input. Please enter a number between 0 and 2.')

    def _choose_ia_level(self) -> IALevel:
        while True:
            try:
                print('\nChoose your IA level')
                print('1. Easy')

                print('0. Quit')

                opponent_choice = int(input('Enter your choice: '))

                match opponent_choice:
                    case IALevelChoice.EASY.value:
                        return IALevel.EASY
                    case IALevelChoice.QUIT.value:
                        raise SystemExit
                    case _:
                        raise ValueError
            except ValueError:
                min_num = min(IALevelChoice)
                max_num = max(IALevelChoice)
                message = (
                    f'Please enter a number between {min_num} and {max_num}.'
                )
                print('Invalid input.', message)
