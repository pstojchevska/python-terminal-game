def print_board(board):
    for row in board:
        print(" ".join(row))

# Initialize game board
board_size = 5
board = [["O"] * board_size for _ in range(board_size)]

print_board(board)