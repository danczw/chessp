from pieces import *


class Board():
    """Chess board class
    """
    def __init__(self):
        pass

    def draw(self):
        print('*' * 33)
        for row in range(8):
            print('|', end='')
            for coloumn in range(7):
                print(' P', end='')
                print(' |', end='')
            print(' P', end='')
            print(' |')
        print('*' * 33)


board = Board()

board.draw()
