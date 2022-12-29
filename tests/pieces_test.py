import pytest

from classes.pieces import Bishop, King, Knight, Pawn, Queen, Rook


def test_king():
    """Test the king class"""
    king = King(color="white", coords=(2, 2), name="king")

    assert king.color == "white"
    assert king.n_moves == 0
    assert king.coords == (2, 2)

    assert king.move((0, 1)) == (-1, -1)
    assert king.move((2, 2)) == (-1, -1)
    assert king.move((2, 3)) == (2, 3)
    assert king.move((3, 3)) == (3, 3)

    assert king.n_moves == 2
    assert king.coords == (3, 3)


def test_king_castle():
    """Test the castle move of king class"""
    for end_col in [2, 6]:
        # valid castle move for white
        king_w = King(color="white", coords=(7, 4), name="king")
        assert king_w.move((7, end_col)) == (7, end_col)
        del king_w

        # invalid castle move for white
        king_w = King(color="white", coords=(7, 4), name="king")
        king_w.n_moves = 1
        assert king_w.move((7, end_col)) == (-1, -1)

        # valid castle move for black
        king_b = King(color="black", coords=(0, 4), name="king")
        assert king_b.move((0, end_col)) == (0, end_col)
        del king_b

        # invalid castle move for black
        king_b = King(color="black", coords=(0, 4), name="king")
        king_b.n_moves = 1
        assert king_b.move((0, end_col)) == (-1, -1)


def test_queen():
    """Test the queen class"""
    queen = Queen(color="black", coords=(2, 2), name="queen")

    assert queen.color == "black"
    assert queen.n_moves == 0
    assert queen.coords == (2, 2)

    assert queen.move((0, 1)) == (-1, -1)
    assert queen.move((2, 2)) == (-1, -1)
    assert queen.move((2, 7)) == (2, 7)
    assert queen.move((7, 7)) == (7, 7)
    assert queen.move((3, 3)) == (3, 3)

    assert queen.n_moves == 3
    assert queen.coords == (3, 3)


def test_rook():
    """Test the rook class"""
    rook = Rook(color="white", coords=(2, 2), name="rook")

    assert rook.color == "white"
    assert rook.n_moves == 0
    assert rook.coords == (2, 2)

    assert rook.move((0, 1)) == (-1, -1)
    assert rook.move((2, 2)) == (-1, -1)
    assert rook.move((2, 7)) == (2, 7)
    assert rook.move((7, 7)) == (7, 7)
    assert rook.move((3, 3)) == (-1, -1)

    assert rook.n_moves == 2
    assert rook.coords == (7, 7)


def test_bishop():
    """Test the bishop class"""
    # test black bishop
    bishop_w = Bishop(color="white", coords=(2, 2), name="bishop")

    assert bishop_w.color == "white"
    assert bishop_w.n_moves == 0
    assert bishop_w.coords == (2, 2)

    assert bishop_w.move((0, 1)) == (-1, -1)
    assert bishop_w.move((2, 2)) == (-1, -1)
    assert bishop_w.move((2, 7)) == (-1, -1)
    assert bishop_w.move((6, 6)) == (6, 6)
    assert bishop_w.move((7, 5)) == (7, 5)
    assert bishop_w.move((3, 3)) == (-1, -1)

    assert bishop_w.n_moves == 2
    assert bishop_w.coords == (7, 5)

    # test white bishop
    bishop_b = Bishop(color="black", coords=(3, 2), name="bishop")

    assert bishop_b.color == "black"
    assert bishop_b.n_moves == 0
    assert bishop_b.coords == (3, 2)

    assert bishop_b.move((0, 1)) == (-1, -1)
    assert bishop_b.move((3, 2)) == (-1, -1)
    assert bishop_b.move((7, 6)) == (7, 6)
    assert bishop_b.move((6, 7)) == (6, 7)
    assert bishop_b.move((3, 3)) == (-1, -1)

    assert bishop_b.n_moves == 2
    assert bishop_b.coords == (6, 7)


def test_knight():
    """Test the knight class"""
    knight = Knight(color="white", coords=(2, 2), name="knight")

    assert knight.color == "white"
    assert knight.n_moves == 0
    assert knight.coords == (2, 2)

    assert knight.move((2, 2)) == (-1, -1)
    assert knight.move((0, 1)) == (0, 1)
    assert knight.move((2, 7)) == (-1, -1)
    assert knight.move((1, 3)) == (1, 3)
    assert knight.move((3, 4)) == (3, 4)

    assert knight.n_moves == 3
    assert knight.coords == (3, 4)


def test_pawn():
    """Test the pawn class"""
    # test black pawn
    pawn_b = Pawn(color="black", coords=(2, 2), name="pawn")

    assert pawn_b.color == "black"
    assert pawn_b.n_moves == 0
    assert pawn_b.coords == (2, 2)

    assert pawn_b.move((0, 1)) == (-1, -1)
    assert pawn_b.move((2, 2)) == (-1, -1)
    assert pawn_b.move((3, 2)) == (3, 2)
    assert pawn_b.move((4, 2)) == (4, 2)
    assert pawn_b.move((4, 3)) == (-1, -1)

    assert pawn_b.n_moves == 2
    assert pawn_b.coords == (4, 2)

    # test white pawn
    pawn_w = Pawn(color="white", coords=(6, 6), name="pawn")

    assert pawn_w.color == "white"
    assert pawn_w.n_moves == 0
    assert pawn_w.coords == (6, 6)

    assert pawn_w.move((0, 1)) == (-1, -1)
    assert pawn_w.move((6, 6)) == (-1, -1)
    assert pawn_w.move((5, 6)) == (5, 6)
    assert pawn_w.move((4, 6)) == (4, 6)
    assert pawn_w.move((4, 5)) == (-1, -1)
    assert pawn_w.move((3, 6)) == (3, 6)

    assert pawn_w.n_moves == 3
    assert pawn_w.coords == (3, 6)

    # test wrong color
    pawn_y = Pawn(color="yellow", coords=(6, 6), name="pawn")

    assert pawn_y.color == "yellow"
    assert pawn_y.n_moves == 0
    assert pawn_y.coords == (6, 6)

    with pytest.raises(ValueError):
        assert pawn_y.move((0, 1)) == ValueError
