from classes.board import Board
from classes.game import Game


def main():
    print('Hello Chess!')
    print('Enter moves in the format: e2:e4, a6:b5, f5:f1, etc.')
    print('<StartcolStartrow>:<EndcolEndrow>')
    print('Enter "exit" to quit')
    
    board = Board()
    game = Game(board=board)
    
    while True:
        move = input('Enter move: ').lower()
        if move == 'exit':
            print('Goodbye Chess!')
            break


if __name__ == '__main__':
    main()
