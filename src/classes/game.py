from classes.board import Board


class Game:
    """Game state class"""

    def __init__(self, board: Board):
        """Initialize a game

        Args:
            board (Board): board status
        """
        self.n_turns = 0
        self.turn_white = True
        self.board = board

        board.draw()

    def toggle_turn(self) -> None:
        """Toggle turn"""
        self.turn_white = not self.turn_white
        self.n_turns += 1
