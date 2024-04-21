from tic_tac_toe.game_type.base import BaseTicTacToe
from tic_tac_toe.setup.game import GameSetup
from tic_tac_toe.setup.players import PlayersSetup


def play_game() -> None:
    player, opponent = PlayersSetup().initialize_players()
    game: BaseTicTacToe = GameSetup(
        player=player,
        opponent=opponent,
    ).initialize_game()

    while not game.game_over:
        game.play()
    game.print_results()


def main():
    try:
        play_game()
    except KeyboardInterrupt:
        print('\nBye!')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        print('Thanks for playing!')


if __name__ == '__main__':
    main()
