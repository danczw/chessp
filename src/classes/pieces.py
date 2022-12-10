from abc import ABC, abstractmethod


class Piece():
    """Chess piece class
    """
    def __init__(self, position: list, color: str):
        """Initialize a chess piece

        Args:
            position (list): list of piece board position, e.g. [0, 1]
                for the first row and second column as a2
            color (str): color of the piece, either 'white' or 'black'
        """
        self.position = position
        self.color = color
    
    def get_color(self) -> str:
        """Getter for piece color

        Returns:
            str: color of the piece
        """
        return self.color
    
    def get_position(self) -> list:
        """Getter for piece position

        Returns:
            list: position of the piece as a list, e.g. [0, 1] for a2
        """
        return self.position
    
    @abstractmethod
    def _check_legal_move(self, new_position: list) -> bool:
        """Check if a move is legal

        Args:
            new_position (list): new position of the piece

        Returns:
            bool: if the move is legal
        """
        pass

        
    def move(self, new_position: list) -> bool:
        """Move the piece to a new position

        Args:
            new_position (list): new position of the piece

        Returns:
            bool: if the move was successful
        """
        if self._check_legal_move(new_position) \
            and new_position != self.position \
            and new_position[0] >= 0 and new_position[0] <= 7 \
            and new_position[1] >= 0 and new_position[1] <= 7:
                self.position = new_position
                return True
        else:
            return False


class King(Piece):
    """Chess king class
    """
    def _check_legal_move(self, new_position: list) -> bool:
        """Check if a move is legal
        new position must be one field away from current position

        Args:
            new_position (list): new position of the piece

        Returns:
            bool: if the move is legal
        """
        return abs(new_position[0]-self.position[0]) <= 1 \
            and abs(new_position[1]-self.position[1]) <= 1


class Queen(Piece):
    """Chess queen class
    """
    def _check_legal_move(self, new_position: list) -> bool:
        """Check if a move is legal
        new position must be in the same row or column as current position
        or in the same diagonal as current position, calculated by the same
        change in row and column

        Args:
            new_position (list): new position of the piece

        Returns:
            bool: if the move is legal
        """
        return (new_position[0] == self.position[0] \
                or new_position[1] == self.position[1]) \
            or (abs(new_position[0]-self.position[0]) \
                == abs(new_position[1]-self.position[1]))


class Rook(Piece):
    """Chess rook class
    """
    def _check_legal_move(self, new_position: list) -> bool:
        """Check if a move is legal
        new position must be in the same row or column as current position

        Args:
            new_position (list): new position of the piece

        Returns:
            bool: if the move is legal
        """
        return new_position[0] == self.position[0] \
            or new_position[1] == self.position[1]


class Bishop(Piece):
    """Chess bishop class
    """
    def _check_legal_move(self, new_position: list) -> bool:
        """Check if a move is legal
        new position must be in the same diagonal as current position,
        calculated by the same change in row and column

        Args:
            new_position (list): new position of the piece

        Returns:
            bool: if the move is legal
        """
        return abs(new_position[0]-self.position[0]) \
            == abs(new_position[1]-self.position[1])


class Knight(Piece):
    """Chess knight class
    """
    def _check_legal_move(self, new_position: list) -> bool:
        """Check if a move is legal
        new position must be two fields away from current position in
        either row or column and one field away in the other direction

        Args:
            new_position (list): new position of the piece

        Returns:
            bool: if the move is legal
        """
        return (abs(new_position[0]-self.position[0]) == 2 \
                and abs(new_position[1]-self.position[1]) == 1) \
            or (abs(new_position[0]-self.position[0]) == 1 \
                and abs(new_position[1]-self.position[1]) == 2)


class Pawn(Piece):
    """Chess pawn class
    """
    def _check_legal_move(self, new_position: list) -> bool:
        """Check if a move is legal
        new position must be one field away from current position in the
        same column

        Args:
            new_position (list): new position of the piece

        Returns:
            bool: if the move is legal
        """
        if self.color == 'white':
            # white pawns move up
            return new_position[1]-self.position[1] == 1 \
                and new_position[0] == self.position[0]
        elif self.color == 'black':
            # black pawns move down
            return new_position[1]-self.position[1] == -1 \
                and new_position[0] == self.position[0]
        else:
            raise ValueError('Invalid color')