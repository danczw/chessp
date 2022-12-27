import utils
from classes.board import Board
from classes.game import Game


def main():
    print("Hello Chess!")
    print("Enter moves in the format: e2:e4, a6:b5, f5:f1, etc.")
    print("(Format: <StartcolStartrow>:<EndcolEndrow>)")
    print('Enter "exit" to quit.\n')

    board = Board()
    game = Game(board=board)

    while True:
        move = input("Enter move: ").lower()
        if move == "exit":
            print("Goodbye Chess!")
            break

        move_coords = utils.validate_move_input_format(move)
        if move_coords[0][0] == -1:
            print("Invalid move format. Try again.")
            continue

        move_success = game.board.move_piece(
            move_coords[0], move_coords[1], game.turn_white
        )
        if move_success:
            game.toggle_turn()


if __name__ == "__main__":
    main()
