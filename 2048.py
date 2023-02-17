import random

# Initialize the board
board = [[0 for i in range(4)] for j in range(4)]

# Add two random tiles to the board
def add_random_tile():
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = random.choice([2, 4])

# Move tiles in the specified direction
def move(direction):
    moved = False
    for i in range(4):
        row = board[i]
        if direction == 'left':
            row = [cell for cell in row if cell != 0] + [0] * row.count(0)
        elif direction == 'right':
            row = [0] * row.count(0) + [cell for cell in row if cell != 0][::-1]
        elif direction == 'up':
            col = [board[j][i] for j in range(4)]
            col = [cell for cell in col if cell != 0] + [0] * col.count(0)
            for j in range(4):
                board[j][i] = col[j]
        elif direction == 'down':
            col = [board[j][i] for j in range(4)][::-1]
            col = [cell for cell in col if cell != 0] + [0] * col.count(0)
            for j in range(4):
                board[j][i] = col[3-j]
        if row != board[i]:
            moved = True
            board[i] = row
    return moved

# Merge adjacent tiles with the same value
def merge():
    merged = False
    for i in range(4):
        for j in range(3):
            if board[i][j] != 0 and board[i][j] == board[i][j+1]:
                board[i][j] *= 2
                board[i][j+1] = 0
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

# Play the game
add_random_tile()
while not is_game_over():
    print_board()
    direction = input('Enter direction: ')
    moved = move(direction)
    merged = merge()
    if moved or merged:
        add_random_tile()
print_board()
print('Game over!')