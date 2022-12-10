from classes.pieces import *


def test_king():
    """Test the king class
    """
    king = King(color='white', position=[2, 2] , name='king')
    
    assert king.get_color() == 'white'
    assert king.get_position() == [2, 2]
    
    assert king.move([0, 1]) == False
    assert king.move([2, 2]) == False
    assert king.move([2, 3]) == True
    assert king.move([3, 3]) == True
    
    assert king.get_position() == [3, 3]


def test_queen():
    """Test the queen class
    """
    queen = Queen(color='black', position=[2, 2], name='queen')
    
    assert queen.get_color() == 'black'
    assert queen.get_position() == [2, 2]
    
    assert queen.move([0, 1]) == False
    assert queen.move([2, 2]) == False
    assert queen.move([2, 7]) == True
    assert queen.move([7, 7]) == True
    assert queen.move([3, 3]) == True
    
    assert queen.get_position() == [3, 3]


def test_rook():
    """Test the rook class
    """
    rook = Rook(color='white', position=[2, 2], name='rook')
    
    assert rook.get_color() == 'white'
    assert rook.get_position() == [2, 2]
    
    assert rook.move([0, 1]) == False
    assert rook.move([2, 2]) == False
    assert rook.move([2, 7]) == True
    assert rook.move([7, 7]) == True
    assert rook.move([3, 3]) == False
    
    assert rook.get_position() == [7, 7]


def test_bishop():
    """Test the bishop class
    """
    # test black bishop
    bishop_w = Bishop(color='white', position=[2, 2], name='bishop')
    
    assert bishop_w.get_color() == 'white'
    assert bishop_w.get_position() == [2, 2]
    
    assert bishop_w.move([0, 1]) == False
    assert bishop_w.move([2, 2]) == False
    assert bishop_w.move([2, 7]) == False
    assert bishop_w.move([6, 6]) == True
    assert bishop_w.move([7, 5]) == True
    assert bishop_w.move([3, 3]) == False
    
    assert bishop_w.get_position() == [7, 5]
    
    # test white bishop
    bishop_b = Bishop(color='black', position=[3, 2], name='bishop')
    
    assert bishop_b.get_color() == 'black'
    assert bishop_b.get_position() == [3, 2]
    
    assert bishop_b.move([0, 1]) == False
    assert bishop_b.move([3, 2]) == False
    assert bishop_b.move([7, 6]) == True
    assert bishop_b.move([6, 7]) == True
    assert bishop_b.move([3, 3]) == False
    
    assert bishop_b.get_position() == [6, 7]


def test_knight():
    """Test the knight class
    """
    knight = Knight(color='white', position=[2, 2], name='knight')
    
    assert knight.get_color() == 'white'
    assert knight.get_position() == [2, 2]
    
    assert knight.move([0, 1]) == True
    assert knight.move([2, 2]) == True
    assert knight.move([2, 7]) == False
    assert knight.move([3, 4]) == True
    assert knight.move([5, 5]) == True
    assert knight.move([3, 3]) == False
    
    assert knight.get_position() == [5, 5]


def test_pawn():
    """Test the pawn class
    """
    # test black pawn
    pawn_w = Pawn(color='black', position=[2, 2], name='pawn')
    
    assert pawn_w.get_color() == 'black'
    assert pawn_w.get_position() == [2, 2]
    
    assert pawn_w.move([0, 1]) == False
    assert pawn_w.move([2, 2]) == False
    assert pawn_w.move([3, 2]) == True
    assert pawn_w.move([4, 2]) == True
    assert pawn_w.move([4, 3]) == False
    
    assert pawn_w.get_position() == [4, 2]
    
    # test white pawn
    pawn_b = Pawn(color='white', position=[6, 6], name='pawn')
    
    assert pawn_b.get_color() == 'white'
    assert pawn_b.get_position() == [6, 6]
    
    assert pawn_b.move([0, 1]) == False
    assert pawn_b.move([6, 6]) == False
    assert pawn_b.move([5, 6]) == True
    assert pawn_b.move([4, 6]) == True
    assert pawn_b.move([4, 5]) == False
    assert pawn_b.move([3, 6]) == True
    
    assert pawn_b.get_position() == [3, 6]
