import random
import keyboard

arrow_keys = ''

# Initialize the board and score
board = [[0 for i in range(4)] for j in range(4)]
score = 0
min_tiles = 8

# Add two random tiles to the board
def add_random_tile():
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = random.choice([2, 4])
        # add an extra tile if the board has fewer than min_tiles tiles
        if len(empty_cells) > 1 and len(empty_cells) < min_tiles:
            row, col = random.choice(empty_cells)
            board[row][col] = random.choice([2, 4])

def no_possible_moves_left():
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
            if i < 3 and board[i][j] == board[i+1][j]:
                return False
            if j < 3 and board[i][j] == board[i][j+1]:
                return False
    return True

# Move tiles in the specified direction
def move_left():
    global score, arrow_keys
    arrow_keys = ''
    if keyboard.is_pressed('left'):
        arrow_keys += 'Pressed Key: ←'
    moved = False
    for i in range(4):
        row = board[i]
        new_row = [cell for cell in row if cell != 0] + [0] * row.count(0)
        if new_row != row:
            moved = True
        for j in range(3):
            if new_row[j] != 0 and new_row[j] == new_row[j+1]:
                new_row[j] *= 2
                new_row[j+1] = 0
                score += new_row[j]
                moved = True
        new_row = [cell for cell in new_row if cell != 0] + [0] * new_row.count(0)
        board[i] = new_row
    if moved:
        add_random_tile()
    if no_possible_moves_left():
        print('Game over! Your score is:', score)
    return moved

def move_right():
    global score, arrow_keys
    arrow_keys = ''
    if keyboard.is_pressed('right'):
        arrow_keys += 'Pressed Key: →'
    moved = False
    for i in range(4):
        row = board[i]
        new_row = [0] * row.count(0) + [cell for cell in row if cell != 0]
        if new_row != row:
            moved = True
        for j in range(3, 0, -1):
            if new_row[j] != 0 and new_row[j] == new_row[j-1]:
                new_row[j] *= 2
                new_row[j-1] = 0
                score += new_row[j]
                moved = True
        new_row = [0] * new_row.count(0) + [cell for cell in new_row if cell != 0]
        board[i] = new_row
    if moved:
        add_random_tile()
    if no_possible_moves_left():
        print('Game over! Your score is:', score)
    return moved

def move_up():
    global score, arrow_keys
    arrow_keys = ''
    if keyboard.is_pressed('up'):
        arrow_keys += 'Pressed Key: ↑'
    moved = False
    for j in range(4):
        column = [board[i][j] for i in range(4)]
        new_column = [cell for cell in column if cell != 0] + [0] * column.count(0)
        if new_column != column:
            moved = True
        for i in range(3):
            if new_column[i] != 0 and new_column[i] == new_column[i+1]:
                new_column[i] *= 2
                new_column[i+1] = 0
                score += new_column[i]
                moved = True
        new_column = [cell for cell in new_column if cell != 0] + [0] * new_column.count(0)
        for i in range(4):
            board[i][j] = new_column[i]
    if moved:
        add_random_tile()
    if no_possible_moves_left():
        print('Game over! Your score is:', score)
    return moved

def move_down():
    global score, arrow_keys
    arrow_keys = ''
    if keyboard.is_pressed('down'):
        arrow_keys += 'Pressed Key: ↓'
    moved = False
    for j in range(4):
        column = [board[i][j] for i in range(3, -1, -1)]
        new_column = [0] * column.count(0) + [cell for cell in column if cell != 0]
        if new_column != column:
            moved = True
        for i in range(len(new_column) - 1, 0, -1):
            if new_column[i] != 0 and new_column[i] == new_column[i-1]:
                new_column[i] *= 2
                new_column[i-1] = 0
                score += new_column[i]
                moved = True
        new_column = [0] * new_column.count(0) + [cell for cell in new_column if cell != 0]
        new_column = [0] * (4 - len(new_column)) + new_column
        for i in range(4):
            board[3-i][j] = new_column[3-i]
    if moved:
        add_random_tile()
    if no_possible_moves_left():
        print('Game over! Your score is:', score)
    return moved
# Print the board
def print_board(board):
    print('\033[2J')
    print('\033[1;1H')
    arrow_row = ''.join(['{:^2}'.format(key) for key in arrow_keys])
    if arrow_row.strip() != '':
        print(arrow_row)
    print('\033[1m' + '┌─────┬─────┬─────┬─────┐' + '\033[0m')
    for row in board:
        row_str = '\033[1m' + '│' + '\033[0m'
        for cell in row:
            if cell == 0:
                row_str += '     '
            else:
                color = 30 + len(str(cell)) % 7
                row_str += '\033[{}m'.format(color) + '{:^5}'.format(cell) + '\033[0m'
            row_str += '\033[1m' + '│' + '\033[0m'
        print(row_str)
        print('\033[1m' + '├─────┼─────┼─────┼─────┤' + '\033[0m')
    print('\033[1m' + '│ Score: {:<5}          │'.format(score) + '\033[0m')
    print('\033[1m' + '└─────┴─────┴─────┴─────┘' + '\033[0m')

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