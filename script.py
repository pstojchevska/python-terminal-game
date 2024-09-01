import random

def print_board(board):
    #Prints the current state of the game board.
    for row in board:
        print(" ".join(row))

def place_ship(board):
    #Places a ship randomly on the board.
    row = random.randint(0, board_size - 1)
    col = random.randint(0, board_size - 1)
    board[row][col] = "S"
    return (row, col)

def get_player_guess():
    #Prompts the player to enter a guess for the ship's location.
    while True:
        try:
            guess_row = int(input("Guess Row (0-4): "))
            guess_col = int(input("Guess Col (0-4): "))
            if 0 <= guess_row < board_size and 0 <= guess_col < board_size:
                return (guess_row, guess_col)
            else:
                print("Out of bounds! Try again.")
        except ValueError:
            print("Invalid input! Please enter numbers only.")

def check_guess(guess, ship_location):
    #Checks if the player's guess is correct or not.
    if guess == ship_location:
        print("Congratulations! You sunk the battleship!")
        return True
    else:
        print("You missed!")
        return False

def game_intro():
    #Displays the game introduction and instructions.
    print("Welcome to Battleship!")
    print("Try to sink the battleship by guessing its location on a 5x5 grid.")
    print("You have 4 turns to find the battleship. Good luck!\n")

# Game setup
board_size = 5
board = [["O"] * board_size for _ in range(board_size)]
game_intro()
ship_location = place_ship(board)

# Game loop
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
