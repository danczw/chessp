from classes.pieces import Bishop, King, Knight, Pawn, Piece, Queen, Rook


def prCyan_on_line(text):
    """Print in cyan wihtout newline

    Args:
        text (str): text to print in cyan
    """
    print(f'\033[96m {text}\033[00m', end='')


class Board():
    """Chess board class
    """
    def __init__(self):
        self.pieces = self._starting_positions()

    def _starting_positions(self) -> dict[int, dict[int, Piece]]:
        """Initialize pieces at starting position

        Returns:
            dict: dict of namedtuple(row, col): piece
        """
        pieces = {
            0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {},
        }

        # initialize pawns
        for row in [1, 6]:
            for col in range(8):
                if row == 1:
                    pieces[row][col] = Pawn((row, col), 'black', 'pawn')
                else:
                    pieces[row][col] = Pawn((row, col), 'white', 'pawn')

        # initialize rooks
        for col in [0, 7]:
            pieces[0][col] = Rook((0, col), 'black', 'rook')
            pieces[7][col] = Rook((7, col), 'white', 'rook')

        # initialize knights
        for col in [1, 6]:
            pieces[0][col] = Knight((0, col), 'black', 'knight')
            pieces[7][col] = Knight((7, col), 'white', 'knight')

        # initialize bishops
        for col in [2, 5]:
            pieces[0][col] = Bishop((0, col), 'black', 'bishop')
            pieces[7][col] = Bishop((7, col), 'white', 'bishop')

        # initialize queens
        pieces[0][3] = Queen((0, 3), 'black', 'queen')
        pieces[7][3] = Queen((7, 3), 'white', 'queen')

        # initialize kings
        pieces[0][4] = King((0, 4), 'black', 'king')
        pieces[7][4] = King((7, 4), 'white', 'king')

        return pieces

    def move_piece(
        self,
        startcoords: tuple,
        endcoords: tuple,
        white_turn: bool
            ) -> bool:
        """Move a piece on the board as per user input

        Args:
            startcoords (tuple): starting coords of the piece
            endcoords (tuple): ending coords of the piece
            white_turn (bool): if it is white's turn

        Returns:
            bool: True if move is successful, False otherwise
        """
        # check if there is a piece at start coords
        try:
            moved_piece = self.pieces[startcoords[0]][startcoords[1]]
        except KeyError:
            print('No piece at start position')
            return False

        # check if piece is of the same color as current turn
        if (moved_piece.color == 'white' and not white_turn) \
                or (moved_piece.color == 'black' and white_turn):
            print('Not your turn')
            return False

        # check if move is valid for piece
        if moved_piece.move(endcoords) == (-1, -1):
            print('Invalid move')
            return False

        # check if end coords is occupied...
        try:
            end_piece = self.pieces[endcoords[0]][endcoords[1]]
        except KeyError:
            end_piece = None
        # ...and if it is of the same color
        if end_piece and end_piece.color == moved_piece.color:
            print('Cannot capture own piece')
            return False

        # get all coords between start and end
        all_coords = self._get_coords_between(startcoords, endcoords)
        # check if any piece is in the way
        for coords in all_coords:
            if self.pieces[coords[0]].get(coords[1]):
                print('Piece in the way')
                return False
        # if no piece is in the way, remove piece from start coords
        del self.pieces[startcoords[0]][startcoords[1]]

        # check for castling and move rook
        if moved_piece.name_short == 'K' \
                and abs(startcoords[1] - endcoords[1]) == 2:
            castle_check = self._castling(startcoords, endcoords)

            if not castle_check:
                return False

        # move piece to end coords
        self.pieces[endcoords[0]][endcoords[1]] = moved_piece
        self.draw()

        return True

    def _get_coords_between(
        self,
        startcoords: tuple,
        endcoords: tuple
            ) -> list[tuple]:
        """Get all coords between start and end

        Args:
            startcoords (tuple): starting coords
            endcoords (tuple): ending coords

        Returns:
            list[tuple]: list of coords between start and end
        """
        coords_between = []
        row_coords = sorted([startcoords[0], endcoords[0]])
        col_coords = sorted([startcoords[1], endcoords[1]])

        # horizontal move
        if startcoords[0] == endcoords[0]:
            for col in range(col_coords[0] + 1, col_coords[1]):
                coords_between.append((startcoords[0], col))
        # vertical move
        elif startcoords[1] == endcoords[1]:
            for row in range(row_coords[0] + 1, row_coords[1]):
                coords_between.append((row, startcoords[1]))
        # diagonal move
        elif abs(startcoords[0] - endcoords[0]) \
                == abs(startcoords[1] - endcoords[1]):
            # board downwards
            if startcoords[0] < endcoords[0]:
                row_start = startcoords[0] + 1
                row_end = endcoords[0]
            # board upwards
            else:
                row_start = endcoords[0] + 1
                row_end = startcoords[0]

            # board rightwards
            if startcoords[1] < endcoords[1]:
                col_start = startcoords[1] + 1
                col_end = endcoords[1]
            # board leftwards
            else:
                col_start = endcoords[1] + 1
                col_end = startcoords[1]

            for row, col in zip(range(row_start, row_end),
                                range(col_start, col_end)):
                coords_between.append((row, col))

        return coords_between

    def _castling(
        self,
        startcoords: tuple[int, int],
        endcoords: tuple[int, int]
    ) -> bool:
        # get rook
        if startcoords[1] < endcoords[1]:
            rook_startcoords = (startcoords[0], 7)
            rook_endcoords = (startcoords[0], 5)
        else:
            rook_startcoords = (startcoords[0], 0)
            rook_endcoords = (startcoords[0], 3)
        moved_rook = self.pieces[rook_startcoords[0]][rook_startcoords[1]]

        # check if rook has moved
        if moved_rook.n_moves != 0:
            print('Cannot castle, rook has moved')
            return False

        # check if rook move is valid
        if moved_rook.move(rook_endcoords) == (-1, -1):
            print('Invalid castling')
            return False

        # get all coords between start and end
        all_coords = self._get_coords_between(rook_startcoords, rook_endcoords)
        # check if any piece is in the way
        for coords in all_coords:
            if self.pieces[coords[0]].get(coords[1]):
                print('Piece in the way')
                return False

        del self.pieces[rook_startcoords[0]][rook_startcoords[1]]
        self.pieces[rook_endcoords[0]][rook_endcoords[1]] = moved_rook
        return True

    def draw(self) -> None:
        """Print current board status
        """
        print('    a   b   c   d   e   f   g   h')
        print('  ' + '*' * 33)

        for row in range(0, 8):
            print(f'{8 - row} |', end='')

            for col in range(0, 8):
                if self.pieces[row].get(col):
                    if self.pieces[row][col].color == 'black':
                        prCyan_on_line(f'{self.pieces[row][col].name_short}')
                    else:
                        print(f' {self.pieces[row][col].name_short}', end='')
                else:
                    print('  ', end='')
                print(' |', end='')

            print(' ')

        print('  ' + '*' * 33)
