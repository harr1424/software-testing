import re

"""
John Harrington
Software Reliability and Testing, Spring, 2022
Assignment Three: Dependency Injection
"""


class Helper:
    """
    This class contains helper methods that can be injected into the Game class
    """

    def __init__(self):
        # Store configs for winner_check() method
        self.configs = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(2, 0), (1, 1), (0, 2)],
        ]

    def take_turn(self, curr_player):
        """
        Helper function to allow the program to take turns between two users:
        An 'X' user, and an 'O' user.
        >>> Helper.take_turn(Helper(), 'X')
        'O'
        >>> Helper.take_turn(Helper(), 'O')
        'X'
        >>> Helper.take_turn(Helper(), '0')
        Traceback (most recent call last):
        ...
        RuntimeError: Current player was not defined as either 'X' or 'O'

        :param curr_player:
        :return:
        """
        if curr_player == 'X':
            return 'O'
        elif curr_player == 'O':
            return 'X'
        else:
            raise RuntimeError("Current player was not defined as either 'X' or 'O'")

    def print_board(self, board):
        """
        Helper method to print the game board.
        See tests.py for unit testing using a mock object.
        :param board:
        :return:
        """
        print("  1 2 3")
        for i in range(3):
            print(f"{i + 1} " + "|".join(board[i]))

    def next_move(self, curr_player, board):
        """
        Accept the current player's next move, validate it,and update the board's state.
        See tests.py for unit testing using a mock object.
        :param curr_player:
        :param board:
        :return:
        """
        # Get next move from user
        move = input(f"{curr_player}'s move, enter row and column: ")
        row, col = re.split(r"[ \t,]+", move)
        row_index, col_index = int(row) - 1, int(col) - 1

        # Validate the move
        while board[row_index][col_index] != " ":
            print("Choose an empty space!")
            self.print_board(board)
            move = input(f"{curr_player}'s move, enter row and column: ")
            row, col = re.split(r"[ \t,]+", move)
            row_index, col_index = int(row) - 1, int(col) - 1
            continue

        # Update the board object
        board[row_index][col_index] = curr_player

    def winner_check(self, curr_player, board):
        """
        Inspects most recent update to game board (last player's turn)
        to determine if either player has won.
        See tests.py for unit testing using a mock object.
        :param curr_player:
        :param board:
        :return:
        """
        winner = False

        for config in self.configs:
            config_wins = True
            for row_index, col_index in config:
                if board[row_index][col_index] != curr_player:
                    config_wins = False
                    break
            if config_wins:
                winner = True
                break
        if winner:
            print(f"Congratulations {curr_player}, you won!")
            exit(0)


class Game:
    def __init__(self, helper_methods):
        self.helper = helper_methods
        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]
        self.turn = "X"
        self.row_index = -1
        self.col_index = -1

    def play(self):
        while True:
            # Print the current board state
            self.helper.print_board(self.board)

            # Process next move
            self.helper.next_move(self.turn, self.board)

            # Check for a winner
            self.helper.winner_check(self.turn, self.board)

            # There was no winner, so go to the next player
            self.turn = self.helper.take_turn(self.turn)


def main():
    helper = Helper()
    game = Game(helper)
    game.play()


if __name__ == "__main__":
    main()
