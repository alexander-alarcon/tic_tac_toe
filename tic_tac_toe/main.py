from tic_tac_toe.game.classic import ClassicTicTacToe
from tic_tac_toe.player.base import PlayerSymbol
from tic_tac_toe.player.human import Human


def main():
    try:
        print('Welcome to tic-tac-toe')

        player_x = Human(PlayerSymbol.X)
        player_o = Human(PlayerSymbol.O)

        print("Let's play!")
        print(player_x, 'vs', player_o)

        game = ClassicTicTacToe(
            player_x=player_x,
            player_o=player_o,
        )

        while game.game_over is False:
            game.play()

        game.print_results()

    except KeyboardInterrupt:
        print('\nBye!')
    except Exception as e:
        print(e.with_traceback())
        print(f'Error: {e}')
    finally:
        print('Thanks for playing!')


if __name__ == '__main__':
    main()
