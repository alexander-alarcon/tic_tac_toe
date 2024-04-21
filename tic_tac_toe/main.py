from enum import Enum

from tic_tac_toe.game_type.base import BaseTicTacToe
from tic_tac_toe.game_type.classic import ClassicTicTacToe
from tic_tac_toe.game_type.limited import LimitedMemoryTicTacToe
from tic_tac_toe.player.base import Player, PlayerSymbol
from tic_tac_toe.player.human import Human


class GameChoice(Enum):
    QUIT = 0
    CLASSIC = 1
    LIMITED = 2


def initialize_players() -> tuple[Player, Player]:
    player_x = Human(PlayerSymbol.X)
    player_o = Human(PlayerSymbol.O)

    return player_x, player_o


def initialize_game(
    game_type: GameChoice, player_x: Player, player_o: Player
) -> BaseTicTacToe:
    match game_type:
        case GameChoice.CLASSIC:
            return ClassicTicTacToe(player_x, player_o)
        case GameChoice.LIMITED:
            return LimitedMemoryTicTacToe(player_x, player_o)
        case GameChoice.QUIT:
            raise KeyboardInterrupt

    raise ValueError(f'Invalid game type: {game_type}')


def chose_game_type() -> GameChoice:
    while True:
        try:
            print('\nWhich kind of play do you want?')
            print('1. Classic')
            print('2. Limited memory')
            print('0. Quit')

            game_choice = int(input('Enter your choice: '))

            if game_choice == GameChoice.CLASSIC.value:
                return GameChoice.CLASSIC

            if game_choice == GameChoice.LIMITED.value:
                return GameChoice.LIMITED

            if game_choice == GameChoice.QUIT.value:
                raise KeyboardInterrupt

            print('Invalid choice. Please enter a number between 1 and 3.')
        except ValueError:
            print('Invalid input. Please enter a number.')
        except KeyboardInterrupt:
            return GameChoice.QUIT
        except Exception as e:
            print(e.with_traceback())
            print(f'Error: {e}')


def play_game(game: BaseTicTacToe) -> None:
    print("\nLet's play!")
    while not game.game_over:
        game.play()
    game.print_results()


def main():
    try:
        print('Welcome to tic-tac-toe')

        player_x, player_o = initialize_players()
        game_choice: GameChoice = chose_game_type()
        game: BaseTicTacToe = initialize_game(game_choice, player_x, player_o)

        play_game(game)
    except KeyboardInterrupt:
        print('\nBye!')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        print('Thanks for playing!')


if __name__ == '__main__':
    main()
