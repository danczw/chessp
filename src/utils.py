import re


def validate_move_input_format(move: str) -> tuple[tuple, tuple]:
    """Validates if move input is in the correct format.

    Args:
        move (str): move input by user

    Returns:
        tuple: coordinates of the move: ((startrow, startcol), (endrow, endcol))
            or ((-1, -1), (-1, -1)) if move is not in the correct format
    """
    result = re.match(r'[a-h][1-8]:[a-h][1-8]', move)
    if result and len(move) == 5:
        return move_str_to_coords(move)
    
    return((-1, -1), (-1, -1))


def move_str_to_coords(move: str) -> tuple[tuple, tuple]:
    """_summary_

    Args:
        move (str): move input by user

    Returns:
        tuple: coordinates of the move: ((startrow, startcol), (endrow, endcol))
            or ((-1, -1), (-1, -1)) if move is not in the correct format
    """
    startrow = abs(int(move[1]) - 8)
    startcol = ord(move[0]) - 97
    endrow = abs(int(move[4]) - 8)
    endcol = ord(move[3]) - 97

    return ((startrow, startcol), (endrow, endcol))
