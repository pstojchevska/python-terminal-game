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

def check_guess(guess, ship_location):
    if guess == ship_location:
        print("Congratulations! You sunk the battleship!")
        return True
    else:
        print("You missed!")
        return False

if not check_guess(player_guess, ship_location):
    board[player_guess[0]][player_guess[1]] = "X"


max_turns = 4

for turn in range(max_turns):
    print(f"Turn {turn + 1}")
    print_board(board)
    player_guess = get_player_guess()

    if check_guess(player_guess, ship_location):
        break
    else:
        board[player_guess[0]][player_guess[1]] = "X"

    if turn == max_turns - 1:
        print("Game Over! The battleship was at", ship_location)