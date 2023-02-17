import random
import keyboard

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
def move_left():
    global score
    moved = False
    for i in range(4):
        row = board[i]
        new_row = [cell for cell in row if cell != 0] + [0] * row.count(0)
        if new_row != row:
            moved = True
        board[i] = new_row
    if moved:
        add_random_tile()
    return moved

def move_right():
    global score
    moved = False
    for i in range(4):
        row = board[i]
        new_row = [0] * row.count(0) + [cell for cell in row if cell != 0]
        if new_row != row:
            moved = True
        board[i] = new_row
    if moved:
        add_random_tile()
    return moved

def move_up():
    global score
    moved = False
    for i in range(4):
        col = [board[j][i] for j in range(4)]
        new_col = [cell for cell in col if cell != 0] + [0] * col.count(0)
        if new_col != col:
            moved = True
        for j in range(4):
            board[j][i] = new_col[j]
    if moved:
        add_random_tile()
    return moved

def move_down():
    global score
    moved = False
    for i in range(4):
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
    # merge horizontally
    for i in range(4):
        for j in range(3):
            if board[i][j] != 0 and board[i][j] == board[i][j+1]:
                board[i][j] *= 2
                board[i][j+1] = 0
                score += board[i][j]
                merged = True
    # merge vertically
    for i in range(4):
        for j in range(3):
            if board[j][i] != 0 and board[j][i] == board[j+1][i]:
                board[j][i] *= 2
                board[j+1][i] = 0
                score += board[j][i]
                merged = True
    return merged

# Print the board
def print_board(board):
    print('┌─────┬─────┬─────┬─────┐')
    for row in board:
        row_str = '│'
        for cell in row:
            if cell == 0:
                row_str += '     '
            else:
                row_str += '{:^5}'.format(cell)
            row_str += '│'
        print(row_str)
        print('├─────┼─────┼─────┼─────┤')
    print('│ Score: {:<5}          │'.format(score))
    print('└─────┴─────┴─────┴─────┘')

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

def move_tiles(key):
    moved = False
    if key.name == 'left':
        moved = move_left()
    elif key.name == 'right':
        moved = move_right()
    elif key.name == 'up':
        moved = move_up()
    elif key.name == 'down':
        moved = move_down()
    if moved:
        merge()
        print_board(board)

# Play the game
add_random_tile()
print_board(board)
while not is_game_over():
    try:
        keyboard.on_press_key('left', move_tiles)
        keyboard.on_press_key('right', move_tiles)
        keyboard.on_press_key('up', move_tiles)
        keyboard.on_press_key('down', move_tiles)
        keyboard.wait()
    except KeyboardInterrupt:
        break

print('Game over! Your score is:', score)