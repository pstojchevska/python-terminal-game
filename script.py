import random

def print_board(board):
    for row in board:
        print(" ".join(row))

# Initialize game board
board_size = 5
board = [["O"] * board_size for _ in range(board_size)]

print_board(board)

def place_ship(board):
    row = random.randint(0, board_size - 1)
    col = random.randint(0, board_size - 1)
    board[row][col] = "S"
    return (row, col)

ship_location = place_ship(board)


def get_player_guess():
    guess_row = int(input("Guess Row (0-4): "))
    guesS_col = int(input("Guess Col (0-4): "))
    return (guess_row, guesS_col)

player_guess = get_player_guess()
