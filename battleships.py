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
        ship_row = random.randint(0, BOARD_SIZE, -1)
        # Ship column variable
        ship_col = random.randint(0, BOARD_SIZE, -1)
        # Creates a loop to ensure that the ships do not overlap when placing them on the tiles.
        while board[ship_row][ship_col] == SHIP:
            ship_row = random.randint(0, BOARD_SIZE, -1)
            ship_col = random.randint(0, BOARD_SIZE, -1)
        board[ship_row][ship_col] == SHIP
