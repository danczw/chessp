from classes.board import Board
from classes.game import Game


def test_game():
    """Test game initialization and moves"""

    board = Board()
    game = Game(board=board)

    assert game.n_turns == 0
    assert game.turn_white
    assert isinstance(game.board, Board)

    game.toggle_turn()

    assert game.n_turns == 1
    assert not game.turn_white
