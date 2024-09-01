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

