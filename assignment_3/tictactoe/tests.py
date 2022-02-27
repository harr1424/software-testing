import pytest

import tictactoe


def test_print_board(capfd):
    test_game = tictactoe.Game(tictactoe.Helper)
    test_helper = tictactoe.Helper()
    test_helper.print_board(test_game.board)
    out, err = capfd.readouterr()
    assert out == "  1 2 3\n1  | | \n2  | | \n3  | | \n"


def test_next_move(monkeypatch):
    test_game = tictactoe.Game(tictactoe.Helper)
    test_helper = tictactoe.Helper()
    monkeypatch.setattr('builtins.input', lambda _: "2,2")
    test_helper.next_move("X", test_game.board)
    assert test_game.board == [
            [" ", " ", " "],
            [" ", "X", " "],
            [" ", " ", " "],
        ]


def test_next_move_invalid_int(monkeypatch):
    with pytest.raises(IndexError):
        test_game = tictactoe.Game(tictactoe.Helper)
        test_helper = tictactoe.Helper()
        monkeypatch.setattr('builtins.input', lambda _: "9,9")
        test_helper.next_move("X", test_game.board)


def test_next_move_invalid_input(monkeypatch):
    with pytest.raises(ValueError):
        test_game = tictactoe.Game(tictactoe.Helper)
        test_helper = tictactoe.Helper()
        monkeypatch.setattr('builtins.input', lambda _: "'one', 'two'")
        test_helper.next_move("X", test_game.board)


def test_winner_check_diagonal(capfd):
    test_board = [
            ["X", " ", " "],
            [" ", "X", " "],
            [" ", " ", " "],
        ]
    test_game = tictactoe.Game(tictactoe.Helper)
    test_helper = tictactoe.Helper()
    test_helper.winner_check(2, 2, 'X', test_board)
    out, err = capfd.readouterr()
    assert out == "Congratulations X, you won!"

