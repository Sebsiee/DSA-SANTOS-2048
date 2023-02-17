import random

# Initialize the board and score
board = [[0 for i in range(4)] for j in range(4)]
score = 0

# Add two random tiles to the board
def add_random_tile():
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = random.choice([2, 4])

# Move tiles in the specified direction
def move(direction):
    global score
    moved = False
    for i in range(4):
        if direction == 'left':
            row = board[i]
            new_row = [cell for cell in row if cell != 0] + [0] * row.count(0)
            if new_row != row:
                moved = True
            board[i] = new_row
        elif direction == 'right':
            row = board[i]
            new_row = [0] * row.count(0) + [cell for cell in row if cell != 0]
            if new_row != row:
                moved = True
            board[i] = new_row
        elif direction == 'up':
            col = [board[j][i] for j in range(4)]
            new_col = [cell for cell in col if cell != 0] + [0] * col.count(0)
            if new_col != col:
                moved = True
            for j in range(4):
                board[j][i] = new_col[j]
        elif direction == 'down':
            col = [board[j][i] for j in range(4)]
            new_col = [0] * col.count(0) + [cell for cell in col if cell != 0]
            if new_col != col:
                moved = True
            for j in range(4):
                board[j][i] = new_col[j]
    if moved:
        add_random_tile()
    return moved

# Merge adjacent tiles with the same value
def merge():
    global score
    merged = False
    for i in range(4):
        for j in range(3):
            if board[i][j] != 0 and board[i][j] == board[i][j+1]:
                board[i][j] *= 2
                board[i][j+1] = 0
                score += board[i][j]
                merged = True
            if board[j][i] != 0 and board[j][i] == board[j+1][i]:
                board[j][i] *= 2
                board[j+1][i] = 0
                score += board[j][i]
                merged = True
    return merged

# Print the board
def print_board():
    print('\n'.join([' '.join([str(cell).rjust(4) for cell in row]) for row in board]))

# Check if the game is over
def is_game_over():
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
            if i < 3 and board[i][j] == board[i+1][j]:
                return False
            if j < 3 and board[i][j] == board[i][j+1]:
                return False
    return True

# Check if the player has won
def has_won():
    for i in range(4):
        for j in range(4):
            if board[i][j] == 2048:
                return True
    return False

# Play the game
add_random_tile()
while not is_game_over():
    print_board()
    direction = input('Enter direction: ')
    moved = move(direction)
    merged = merge()
    if moved or merged:
        add_random_tile()
    if has_won():
        print_board()
        print('Congratulations! You won!')
        break
print_board()
print('Game over! Your score is:', score)