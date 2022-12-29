from classes.board import Board
from classes.pieces import Pawn


def test_move():
    """Test correct moves"""
    board = Board()

    # pawn move
    board.move_piece((6, 3), (5, 3), True)
    # bishop move for lateral movement
    assert board.move_piece((7, 2), (5, 4), True)


def test_wrong_move():
    """Test raising errors on wrong moves"""
    board = Board()

    # wrong color turn
    assert not board.move_piece((6, 0), (5, 0), False)
    assert not board.move_piece((1, 0), (2, 0), True)

    # no piece at starting position
    assert not board.move_piece((2, 0), (3, 0), True)

    # wrong move
    assert not board.move_piece((6, 0), (7, 0), True)

    # end coordinates occupied of own piece
    assert not board.move_piece((7, 1), (6, 3), True)

    # piece in the way
    assert not board.move_piece((7, 0), (5, 0), True)

    # castling with rook moved
    for col in range(1, 4):  # delete pieces between R and K
        del board.pieces[7][col]
    board.pieces[7][0].n_moves = 1
    assert not board.move_piece((7, 4), (7, 2), True)


def test_pawn_startposition():
    """Test start positions of pieces on board: Pawn"""
    board_one = Board()
    board_two = Board()

    assert board_one.pieces.keys() == board_two.pieces.keys()
    for col in range(8):
        assert board_one.pieces[col].keys() == board_two.pieces[col].keys()
        assert board_one.pieces[1][col].name == "Pawn"
        assert board_one.pieces[1][col].color == "black"
        assert board_one.pieces[6][col].name == "Pawn"
        assert board_one.pieces[6][col].color == "white"


def test_pawn_promotion(monkeypatch):
    """Test promotion of pawns"""
    monkeypatch.setattr("builtins.input", lambda _: "Q")

    # setup board
    board = Board()
    del board.pieces[0][0]
    del board.pieces[1][0]
    board.pieces[1][0] = Pawn(coords=(1, 0), color="white", name="pawn")

    # test promotion
    board.move_piece((1, 0), (0, 0), True)
    assert board.pieces[0][0].name == "Queen"


def test_rook_startposition():
    """Test start positions of pieces on board: Rook"""
    board = Board()

    for col in [0, 7]:
        assert board.pieces[0][col].name == "Rook"
        assert board.pieces[0][col].color == "black"
        assert board.pieces[7][col].name == "Rook"
        assert board.pieces[7][col].color == "white"


def test_knight_startposition():
    """Test start positions of pieces on board: Knight"""
    board = Board()

    for col in [1, 6]:
        assert board.pieces[0][col].name == "Knight"
        assert board.pieces[0][col].color == "black"
        assert board.pieces[7][col].name == "Knight"
        assert board.pieces[7][col].color == "white"


def test_bishop_startposition():
    """Test start positions of pieces on board: Bishop"""
    board = Board()

    for col in [2, 5]:
        assert board.pieces[0][col].name == "Bishop"
        assert board.pieces[0][col].color == "black"
        assert board.pieces[7][col].name == "Bishop"
        assert board.pieces[7][col].color == "white"


def test_queen_startposition():
    """Test start positions of pieces on board: Queen"""
    board = Board()

    assert board.pieces[0][3].name == "Queen"
    assert board.pieces[0][3].color == "black"
    assert board.pieces[7][3].name == "Queen"
    assert board.pieces[7][3].color == "white"


def test_king_startposition():
    """Test start positions of pieces on board: King"""
    board = Board()

    assert board.pieces[0][4].name == "King"
    assert board.pieces[0][4].color == "black"
    assert board.pieces[7][4].name == "King"
    assert board.pieces[7][4].color == "white"


def test_castling():
    """Test castling for white and black"""
    board = Board()

    # basic opening
    board.move_piece((6, 4), (4, 4), True)
    board.move_piece((1, 4), (3, 4), False)
    board.move_piece((7, 5), (6, 4), True)
    board.move_piece((0, 5), (1, 4), False)
    board.move_piece((7, 6), (5, 5), True)
    board.move_piece((0, 6), (2, 5), False)

    # castling
    assert board.move_piece((7, 4), (7, 6), True)
    assert board.move_piece((0, 4), (0, 6), False)
