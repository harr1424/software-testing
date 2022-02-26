import re


# Helper method to take turns
def take_turn(curr_player):
    if curr_player == 'X':
        return 'O'
    elif curr_player == 'O':
        return 'X'
    else:
        raise RuntimeError("Current player was not defined as either 'X' or 'O'")


# Helper method to print board
def print_board(board):
    print("  1 2 3")
    for i in range(3):
        print(f"{i + 1} " + "|".join(board[i]))


# Accept the current player's next move, validate it,
# and update the board's state
def next_move(curr_player, board):
    move = input(f"{curr_player}'s move, enter row and column: ")
    row, col = re.split(r"[ \t,]+", move)
    row_index, col_index = int(row) - 1, int(col) - 1

    while board[row_index][col_index] != " ":
        print("Choose an empty space!")
        print_board(board)
        move = input(f"{curr_player}'s move, enter row and column: ")
        row, col = re.split(r"[ \t,]+", move)
        row_index, col_index = int(row) - 1, int(col) - 1
        continue

    board[row_index][col_index] = curr_player


class Game:
    def __init__(self):
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
            print_board(self.board)

            # Process next move
            next_move(self.turn, self.board)

            # Check for a winner
            winner = False
            configs = [
                [(0, 0), (0, 1), (0, 2)],
                [(1, 0), (1, 1), (1, 2)],
                [(2, 0), (2, 1), (2, 2)],
                [(0, 0), (1, 0), (2, 0)],
                [(0, 1), (1, 1), (2, 1)],
                [(0, 2), (1, 2), (2, 2)],
                [(0, 0), (1, 1), (2, 2)],
                [(2, 0), (1, 1), (0, 2)],
            ]
            for config in configs:
                config_wins = True
                for row_index, col_index in config:
                    if self.board[row_index][col_index] != self.turn:
                        config_wins = False
                        break
                if config_wins:
                    winner = True
                    break
            if winner:
                print(f"Congratulations {self.turn}, you won!")
                break

            # There was no winner, so go to the next player
            self.turn = take_turn(self.turn)


def main():
    game = Game()
    game.play()


if __name__ == "__main__":
    main()
