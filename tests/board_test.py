from classes.board import Board


def test_pawn_startposition():
    """Test start positions of pieces on board: Pawn
    """

    board_one = Board()
    board_two = Board()

    assert board_one.pieces.keys() == board_two.pieces.keys()
    for col in range(8):
        assert board_one.pieces[col].keys() == board_two.pieces[col].keys()
        assert board_one.pieces[1][col].name == 'Pawn'
        assert board_one.pieces[1][col].color == 'black'
        assert board_one.pieces[6][col].name == 'Pawn'
        assert board_one.pieces[6][col].color == 'white'


def test_rook_startposition():
    """Test start positions of pieces on board: Rook
    """
    board = Board()

    for col in [0, 7]:
        assert board.pieces[0][col].name == 'Rook'
        assert board.pieces[0][col].color == 'black'
        assert board.pieces[7][col].name == 'Rook'
        assert board.pieces[7][col].color == 'white'


def test_knight_startposition():
    """Test start positions of pieces on board: Knight
    """
    board = Board()

    for col in [1, 6]:
        assert board.pieces[0][col].name == 'Knight'
        assert board.pieces[0][col].color == 'black'
        assert board.pieces[7][col].name == 'Knight'
        assert board.pieces[7][col].color == 'white'


def test_bishop_startposition():
    """Test start positions of pieces on board: Bishop
    """
    board = Board()

    for col in [2, 5]:
        assert board.pieces[0][col].name == 'Bishop'
        assert board.pieces[0][col].color == 'black'
        assert board.pieces[7][col].name == 'Bishop'
        assert board.pieces[7][col].color == 'white'


def test_queen_startposition():
    """Test start positions of pieces on board: Queen
    """
    board = Board()

    assert board.pieces[0][3].name == 'Queen'
    assert board.pieces[0][3].color == 'black'
    assert board.pieces[7][3].name == 'Queen'
    assert board.pieces[7][3].color == 'white'


def test_king_startposition():
    """Test start positions of pieces on board: King
    """
    board = Board()

    assert board.pieces[0][4].name == 'King'
    assert board.pieces[0][4].color == 'black'
    assert board.pieces[7][4].name == 'King'
    assert board.pieces[7][4].color == 'white'
