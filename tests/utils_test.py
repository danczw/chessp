import utils


def test_val_move_format_pos():
    """Test the validate_move_input_format function with positive cases"""
    assert utils.validate_move_input_format("a1:a2") == ((7, 0), (6, 0))
    assert utils.validate_move_input_format("a1:a8") == ((7, 0), (0, 0))
    assert utils.validate_move_input_format("c3:g8") == ((5, 2), (0, 6))
    assert utils.validate_move_input_format("d2:d8") == ((6, 3), (0, 3))
    assert utils.validate_move_input_format("c7:a2") == ((1, 2), (6, 0))
    assert utils.validate_move_input_format("h1:e5") == ((7, 7), (3, 4))
    assert utils.validate_move_input_format("f7:d3") == ((1, 5), (5, 3))
    assert utils.validate_move_input_format("c7:g4") == ((1, 2), (4, 6))


def test_val_move_format_neg():
    """Test the validate_move_input_format function with negative cases"""
    assert utils.validate_move_input_format("a1:b19") == ((-1, -1), (-1, -1))
    assert utils.validate_move_input_format("a1:k5") == ((-1, -1), (-1, -1))
    assert utils.validate_move_input_format("a1:o9") == ((-1, -1), (-1, -1))
    assert utils.validate_move_input_format("c10:b5") == ((-1, -1), (-1, -1))
    assert utils.validate_move_input_format("j7:b5") == ((-1, -1), (-1, -1))
    assert utils.validate_move_input_format("l18:b5") == ((-1, -1), (-1, -1))
    assert utils.validate_move_input_format("d15:d9") == ((-1, -1), (-1, -1))
    assert utils.validate_move_input_format("k7:m1") == ((-1, -1), (-1, -1))
    assert utils.validate_move_input_format("k15:m9") == ((-1, -1), (-1, -1))
