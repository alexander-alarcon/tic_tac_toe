from tic_tac_toe.player.base import Player, PlayerSymbol


type PlayerOrNone = Player | None
type Board = list[list[PlayerOrNone]]
type BoardOrNone = Board | None


class Human(Player):
    def __init__(self, symbol: PlayerSymbol) -> None:
        super().__init__(symbol)

    def make_move(self, board: BoardOrNone = None) -> int:
        """
        Prompts the human player to make a move.

        Parameters:
            board (Board): The current state of the game board.

        Returns:
            int: The index of the cell where the move was made.
        """
        while True:
            try:
                move = int(input('Enter your move (1-9): '))
                if 1 <= move <= 9:
                    return move
                else:
                    print(
                        'Invalid move. Please enter a number between 1 and 9.'
                    )
            except ValueError:
                print('Invalid input. Please enter a number.')
