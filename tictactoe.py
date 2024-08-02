import numpy as np

# Initialize the game board
board = np.full((3, 3), '-')

# Function to print the game board
def print_board():
    print(" {} | {} | {}".format(board[0, 0], board[0, 1], board[0, 2]))
    print("---+---+---")
    print(" {} | {} | {}".format(board[1, 0], board[1, 1], board[1, 2]))
    print("---+---+---")
    print(" {} | {} | {}".format(board[2, 0], board[2, 1], board[2, 2]))

# Function to check for a win
def check_win(player):
    # Check rows
    for i in range(3):
        if np.all(board[i, :] == player):
            return True
    # Check columns
    for i in range(3):
        if np.all(board[:, i] == player):
            return True
    # Check diagonals
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True
    return False

# Main game loop
while True:
    print_board()
    move = input("Enter your move (row and column, e.g. '1 2'): ")
    row, col = map(int, move.split())
    row -= 1
    col -= 1
    if board[row, col] != '-':
        print("Invalid move, try again.")
        continue
    board[row, col] = 'X'
    if check_win('X'):
        print_board()
        print("X wins!")
        break
    # Computer's turn
    for i in range(3):
        for j in range(3):
            if board[i, j] == '-':
                board[i, j] = 'O'
                if check_win('O'):
                    print_board()
                    print("O wins!")
                    exit()
                board[i, j] = '-'
    # If no winning move is found, place O in a random empty space
    empty_spaces = np.argwhere(board == '-')
    move = empty_spaces[np.random.choice(empty_spaces.shape[0])]
    board[move[0], move[1]] = 'O'