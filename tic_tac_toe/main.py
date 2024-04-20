from tic_tac_toe.player.base import PlayerSymbol
from tic_tac_toe.player.human import Human


def main():
    try:
        print('Welcome to tic-tac-toe')

        player_x = Human(PlayerSymbol.X)
        player_o = Human(PlayerSymbol.O)

        print("Let's play!")
        print(player_x, 'vs', player_o)
        player_x_move = player_x.make_move()
        player_o_move = player_o.make_move()

        print(f'Player {player_x.symbol} moves: {player_x_move}')
        print(f'Player {player_o.symbol} moves: {player_o_move}')

    except KeyboardInterrupt:
        print('\nBye!')
    except Exception as e:
        print(e.with_traceback())
        print(f'Error: {e}')
    finally:
        print('Thanks for playing!')


if __name__ == '__main__':
    main()
