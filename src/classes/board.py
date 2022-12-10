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

    
    def move_piece(self, startcoords:tuple, endcoords:tuple) -> None:
        """Move a piece on the board as per user input

        Args:
            startcoords (tuple): starting coords of the piece
            endcoords (tuple): ending coords of the piece
        """
        # check if there is a piece at start coords
        try:
            moved_piece = self.pieces[startcoords[0]][startcoords[1]]
        except KeyError:
            print('No piece at start position')
            return
        
        # check if move is valid for piece
        if moved_piece.move(endcoords) != (-1, -1):        
            del self.pieces[startcoords[0]][startcoords[1]]
            self.pieces[endcoords[0]][endcoords[1]] = moved_piece
            self.draw()
        else:
            print('Invalid move')
    

    def draw(self) -> None:
        """Print current board status
        """
        print('*' * 33)

        for row in range(0, 8):
            print('|', end='')

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

        print('*' * 33)
