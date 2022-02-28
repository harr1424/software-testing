import pytest

import tictactoe


def test_print_board(capfd):
    test_game = tictactoe.Game(tictactoe.Helper)
    test_helper = tictactoe.Helper()
    test_helper.print_board(test_game.board)
    out, err = capfd.readouterr()
    assert out == "  1 2 3\n1  | | \n2  | | \n3  | | \n"


def test_print_board_one_turn(monkeypatch,capfd):
    """
     Simulates one cycle through the while loop contained in Game.play
     The initial board output has been omitted as this test is concerned
     with the board printed after one 'turn' has been taken.
    """
    test_game = tictactoe.Game(tictactoe.Helper)
    test_helper = tictactoe.Helper()
    monkeypatch.setattr('builtins.input', lambda _: "2,2")
    test_helper.next_move('X', test_game.board)
    test_helper.winner_check('X', test_game.board)
    test_helper.take_turn('X')
    test_helper.print_board(test_game.board)
    out, err = capfd.readouterr()
    assert out == "  1 2 3\n1  | | \n2  |X| \n3  | | \n"


def test_print_board_three_turns(monkeypatch,capfd):
    """
     Simulates three cycles through the while loop contained in Game.play
     The initial board output and the board output at the beginning of each turn
     have been omitted as this test is concerned only with the final board state.
    """
    test_game = tictactoe.Game(tictactoe.Helper)
    test_helper = tictactoe.Helper()
    responses = iter(['2,2', '1,1', '3,3'])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    test_helper.next_move('X', test_game.board)
    test_helper.winner_check('X', test_game.board)
    test_helper.take_turn('X')
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    test_helper.next_move('O', test_game.board)
    test_helper.winner_check('O', test_game.board)
    test_helper.take_turn('O')
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    test_helper.next_move('X', test_game.board)
    test_helper.winner_check('X', test_game.board)
    test_helper.take_turn('X')
    test_helper.print_board(test_game.board)
    out, err = capfd.readouterr()
    assert out == "  1 2 3\n1 O| | \n2  |X| \n3  | |X\n"


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

def test_next_move_three_turns(monkeypatch):
    test_game = tictactoe.Game(tictactoe.Helper)
    test_helper = tictactoe.Helper()
    responses = iter(['2,2', '1,1', '3,3'])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    test_helper.next_move("X", test_game.board)
    test_helper.winner_check('X', test_game.board)
    test_helper.take_turn('X')
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    test_helper.next_move('O', test_game.board)
    test_helper.winner_check('O', test_game.board)
    test_helper.take_turn('O')
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    test_helper.next_move('X', test_game.board)
    test_helper.winner_check('X', test_game.board)
    test_helper.take_turn('X')
    assert test_game.board == [
            ["O", " ", " "],
            [" ", "X", " "],
            [" ", " ", "X"],
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


def test_winner_check_diagonal():
    with pytest.raises(SystemExit) as e:
        test_board = [
                ["X", " ", " "],
                [" ", "X", " "],
                [" ", " ", "X"],
            ]
        test_game = tictactoe.Game(tictactoe.Helper)
        test_helper = tictactoe.Helper()
        test_helper.winner_check('X', test_board)
        assert e.type == SystemExit
        assert e.value.code == 0


def test_winner_check_row():
    with pytest.raises(SystemExit) as e:
        test_board = [
                ["X", "X", "X"],
                [" ", " ", " "],
                [" ", " ", " "],
            ]
        test_game = tictactoe.Game(tictactoe.Helper)
        test_helper = tictactoe.Helper()
        test_helper.winner_check('X', test_board)
        assert e.type == SystemExit
        assert e.value.code == 0


def test_winner_check_col():
    with pytest.raises(SystemExit) as e:
        test_board = [
                ["O", " ", " "],
                ["O", " ", " "],
                ["O", " ", " "],
            ]
        test_game = tictactoe.Game(tictactoe.Helper)
        test_helper = tictactoe.Helper()
        test_helper.winner_check('O', test_board)
        assert e.type == SystemExit
        assert e.value.code == 0


def test_winner_check_fails_position_marked_by_other_player(capfd):
    test_board = [
            ["O", " ", " "],
            ["O", " ", " "],
            ["O", " ", " "],
        ]
    test_game = tictactoe.Game(tictactoe.Helper)
    test_helper = tictactoe.Helper()
    test_helper.winner_check('X', test_board)
    out, err = capfd.readouterr()
    assert out == ""


def test_winner_check_fails_incomplete_sequence(capfd):
    # This board configuration can't actually occur, but it is a decent example of a corner case
    test_board = [
            ["O", "X", "O"],
            ["X", "X", "O"],
            ["O", "O", "X"],
        ]
    test_game = tictactoe.Game(tictactoe.Helper)
    test_helper = tictactoe.Helper()
    test_helper.winner_check('X', test_board)
    out, err = capfd.readouterr()
    assert out == ""
