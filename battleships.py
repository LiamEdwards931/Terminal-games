import random

def battleships():
    # Variables For The Game To Run - Caps as they are global in the game function.
    EMPTY = ' '
    SHIP = 'S'
    HIT = 'X'
    MISS = 'O'
    BOARD_SIZE = 8
    NUM_SHIPS = 4

    # Initializes the board
    board = [[EMPTY] * BOARD_SIZE for _ in range(BOARD_SIZE)]

    #Creates and places the ships in random intervals on the board
    for _ in range(NUM_SHIPS):
        # Ship row variable
        ship_row = random.randint(0, BOARD_SIZE -1)
        # Ship column variable
        ship_col = random.randint(0, BOARD_SIZE -1)
        # Creates a loop to ensure that the ships do not overlap when placing them on the tiles.
        while board[ship_row][ship_col] == SHIP:
            ship_row = random.randint(0, BOARD_SIZE -1)
            ship_col = random.randint(0, BOARD_SIZE -1)
        board[ship_row][ship_col] == SHIP

    # Displays the Game Board - Appends new rows in the print function to make the game board clean.
    def print_board(board):
        print('   A B C D E F G H')
        print('  ----------------')
        row_num = 1
        for row in board:
            print("%d |%s|" % (row_num, "|".join(row)))
            row_num += 1
        print('  ----------------')

    # Main loop that runs the game
    while any(SHIP in row for row in board):
        print("\n Your Board:")
        print_board(board)

    # Players turn - prints column guess and row guess on two seperate lines for easier guessing in the terminal
    column_guess = input("Guess a column (A-H): ").upper()
    row_guess = int(input("Guess a Row (1-8): ")) -1

    #Dictionary rows and columns
    col_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
    # Guess validation for columns
    if column_guess not in col_dict:
            print("That is not a valid column. Try again\n")
            continue
    column_guess = col_dict[column_guess]
    # Guess Validation for rows
    if guess_row < 0 or guess_row >= BOARD_SIZE:
            print("Invalid row. Try again.\n")
            continue
    

    

