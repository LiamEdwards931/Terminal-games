import random
from run import start

def battleships():
    # Variables For The Game To Run - Caps as they are global in the game function.
    EMPTY = ' '
    SHIP = 'S'
    HIT = 'X'
    MISS = 'O'
    BOARD_SIZE = 8
    NUM_SHIPS = 4
    print("Welcome to Battleships\n")
    print("The aim is to sink your opponents ships by guess a grid and column number\n")
    
    # Initializes the board
    board = [[EMPTY] * BOARD_SIZE for _ in range(BOARD_SIZE)]

    # Creates and places the ships in random intervals on the board
    for _ in range(NUM_SHIPS):
        # Ship row variable
        ship_row = random.randint(0, BOARD_SIZE -1)
        # Ship column variable
        ship_col = random.randint(0, BOARD_SIZE -1)
        # Creates a loop to ensure that the ships do not overlap when placing them on the tiles.
        while board[ship_row][ship_col] == SHIP:
            ship_row = random.randint(0, BOARD_SIZE -1)
            ship_col = random.randint(0, BOARD_SIZE -1)
        board[ship_row][ship_col] = SHIP

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

        # Players turn - prints column guess and row guess on two separate lines for easier guessing in the terminal
        column_guess = input("Guess a column (A-H): \n").upper()
        row_guess = int(input("Guess a Row (1-8): \n")) - 1
        
        # Dictionary rows and columns
        col_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

        # Guess validation for columns
        if column_guess not in col_dict:
            print("That is not a valid column. Try again\n")
            continue
    
        column_guess = col_dict[column_guess]

        # Guess Validation for rows
        if row_guess < 0 or row_guess >= BOARD_SIZE:
            print("Invalid row. Try again.\n")
            continue

        # Checks if you have hit a ship
        if board[row_guess][column_guess] == SHIP:
            print("HIT! You successfully hit a ship\n")
            board[row_guess][column_guess] = HIT
        elif board[row_guess][column_guess] == HIT or board[row_guess][column_guess] == MISS:
            print("This position has already been fired at! Try again\n")
        else:
            print("MISS! You missed a ship\n")
            board[row_guess][column_guess] = MISS

    
    #Restart Game function
    def restart_game():
        battleships()

    # Game over
    print("\nYour Final Board:")
    print_board(board)
    print("You Win! Congratulations\n")
    Print("Would you like to play again?")
    option = input("yes or no?: ").lower()
    if option == "yes":
        restart_game()
    elif option == "no":
        print("Thank you for playing battleships")
        start()
    else:
        print("Please enter a valid input!")


    

