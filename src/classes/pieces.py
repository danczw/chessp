from abc import abstractmethod


class Piece():
    """Chess piece class
    """
    def __init__(self, coords: tuple, color: str, name: str):
        """Initialize a chess piece

        Args:
            coords (tuple): tuple of (reverse) piece board coords, e.g.
                [0, 1] for the first row and second column starting from
                top left: b8
            color (str): color of the piece, either 'white' or 'black'
            name (str): name of the piece, e.g. 'king'
            name_short (str): short name of the piece, e.g. 'K'
        """
        self.coords = coords
        self.color = color
        self.n_moves = 0
        self.name = name.title()
        self.name_short = name[0].upper() if self.name != 'Knight' else 'N'

    def __str__(self) -> str:
        """String representation of the piece

        Returns:
            str: string representation of the piece
        """
        return f'{self.color} {self.name} at {self.coords}'

    @abstractmethod
    def _check_legal_move(self, new_coords: tuple) -> bool:
        """Check if a move is legal

        Args:
            new_coords (tuple): new coords of the piece

        Returns:
            bool: if the move is legal
        """
        pass

    def move(self, new_coords: tuple[int, int], ) -> tuple[int, int]:
        """Move the piece to a new coords

        Args:
            new_coords (tuple): new coords of the piece

        Returns:
            bool: if the move was successful
        """
        if self._check_legal_move(new_coords) \
            and new_coords != self.coords \
            and new_coords[0] >= 0 and new_coords[0] <= 7 \
                and new_coords[1] >= 0 and new_coords[1] <= 7:

            self.coords = new_coords
            self.n_moves += 1
            return new_coords
        else:
            return (-1, -1)


class King(Piece):
    """Chess king class
    """
    def _check_legal_move(self, new_coords: tuple) -> bool:
        """Check if a move is legal
        new coords must be one field away from current coords

        Args:
            new_coords (tuple): new coords of the piece

        Returns:
            bool: if the move is legal
        """
        return abs(new_coords[0]-self.coords[0]) <= 1 \
            and abs(new_coords[1]-self.coords[1]) <= 1

        # TODO: add castling


class Queen(Piece):
    """Chess queen class
    """
    def _check_legal_move(self, new_coords: tuple) -> bool:
        """Check if a move is legal
        new coords must be in the same row or column as current coords
        or in the same diagonal as current coords, calculated by the same
        change in row and column

        Args:
            new_coords (tuple): new coords of the piece

        Returns:
            bool: if the move is legal
        """
        return (new_coords[0] == self.coords[0]
                or new_coords[1] == self.coords[1]) \
            or (abs(new_coords[0]-self.coords[0])
                == abs(new_coords[1]-self.coords[1]))


class Rook(Piece):
    """Chess rook class
    """
    def _check_legal_move(self, new_coords: tuple) -> bool:
        """Check if a move is legal
        new coords must be in the same row or column as current coords

        Args:
            new_coords (tuple): new coords of the piece

        Returns:
            bool: if the move is legal
        """
        return new_coords[0] == self.coords[0] \
            or new_coords[1] == self.coords[1]


class Bishop(Piece):
    """Chess bishop class
    """
    def _check_legal_move(self, new_coords: tuple) -> bool:
        """Check if a move is legal
        new coords must be in the same diagonal as current coords,
        calculated by the same change in row and column

        Args:
            new_coords (tuple): new coords of the piece

        Returns:
            bool: if the move is legal
        """
        return abs(new_coords[0]-self.coords[0]) \
            == abs(new_coords[1]-self.coords[1])


class Knight(Piece):
    """Chess knight class
    """
    def _check_legal_move(self, new_coords: tuple) -> bool:
        """Check if a move is legal
        new coords must be two fields away from current coords in
        either row or column and one field away in the other direction

        Args:
            new_coords (tuple): new coords of the piece

        Returns:
            bool: if the move is legal
        """
        return (abs(new_coords[0]-self.coords[0]) == 2
                and abs(new_coords[1]-self.coords[1]) == 1) \
            or (abs(new_coords[0]-self.coords[0]) == 1
                and abs(new_coords[1]-self.coords[1]) == 2)


class Pawn(Piece):
    """Chess pawn class
    """
    def _check_legal_move(self, new_coords: tuple) -> bool:
        """Check if a move is legal
        new coords must be one field away from current coords in the
        same column

        Args:
            new_coords (tuple): new coords of the piece

        Returns:
            bool: if the move is legal
        """
        if self.color == 'white':
            diff = (-2, -1) if self.n_moves == 0 else (-1,)
            return new_coords[0]-self.coords[0] in diff \
                and new_coords[1] == self.coords[1]
        elif self.color == 'black':
            diff = (2, 1) if self.n_moves == 0 else (1,)
            return new_coords[0]-self.coords[0] in diff \
                and new_coords[1] == self.coords[1]
        else:
            raise ValueError('Invalid color')

        # TODO: add en passant
        # TODO: add promotion
        # TODO: add capture
