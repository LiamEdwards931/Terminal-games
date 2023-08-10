import random

def battleships():
    # Variables For The Game To Run 
    EMPTY = ' '
    SHIP = 'S'
    HIT = 'X'
    MISS = 'O'
    BOARD_SIZE = 8
    NUM_SHIPS = 4

    # Initializes the board
    board = [[EMPTY] * BOARD_SIZE for _ in range(BOARD_SIZE)]

    #Creates and places the ships in random intervals on the board
    
