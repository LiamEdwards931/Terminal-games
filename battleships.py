import random

def battleships():
    EMPTY = ' '
    SHIP = 'S'
    HIT = 'X'
    MISS = 'O'
    BOARD_SIZE = 8
    NUM_SHIPS = 4
    print("Welcome to Battleships\n")
    print("The aim is to sink your opponent's ships by guessing a grid and column number\n")
    
    def initialize_board():
        return [[EMPTY] * BOARD_SIZE for _ in range(BOARD_SIZE)]

    def create_ships(board):
        """
        Creates the ships
        """
        for _ in range(NUM_SHIPS):
            ship_row = random.randint(0, BOARD_SIZE - 1)
            ship_col = random.randint(0, BOARD_SIZE - 1)
            while board[ship_row][ship_col] == SHIP:
                ship_row = random.randint(0, BOARD_SIZE - 1)
                ship_col = random.randint(0, BOARD_SIZE - 1)
            board[ship_row][ship_col] = SHIP
    
    def print_board(board):
        """
        prints the game board
        """
        print('   A B C D E F G H')
        print('  ----------------')
        row_num = 1
        for row in board:
            print("%d |%s|" % (row_num, "|".join(row)))
            row_num += 1
        print('  ----------------')

    player_board = initialize_board()
    computer_board = initialize_board()
    create_ships(player_board)
    create_ships(computer_board)

    while any(SHIP in row for row in computer_board):
        print("\n Your Board:")
        print_board(player_board)

        # Players turn
        column_guess = input("Guess a column (A-H): \n").upper()
        row_guess = int(input("Guess a Row (1-8): \n")) - 1
        
        col_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        if column_guess not in col_dict:
            print("That is not a valid column. Try again\n")
            continue
        column_guess = col_dict[column_guess]

        if row_guess < 0 or row_guess >= BOARD_SIZE:
            print("Invalid row. Try again.\n")
            continue

        if computer_board[row_guess][column_guess] == SHIP:
            print("HIT! You successfully hit a ship\n")
            computer_board[row_guess][column_guess] = HIT
        elif computer_board[row_guess][column_guess] == HIT or computer_board[row_guess][column_guess] == MISS:
            print("This position has already been fired at! Try again\n")
        else:
            print("MISS! You missed a ship\n")
            computer_board[row_guess][column_guess] = MISS

        # Computer's turn
        computer_guess_row = random.randint(0, BOARD_SIZE - 1)
        computer_guess_col = random.randint(0, BOARD_SIZE - 1)

        print("\nComputer's Turn:")
        if player_board[computer_guess_row][computer_guess_col] == SHIP:
            print("Computer HIT your ship!")
            player_board[computer_guess_row][computer_guess_col] = HIT
        else:
            print("Computer MISSED!")
            player_board[computer_guess_row][computer_guess_col] = MISS

    def restart_game():
        battleships()

    print("\nYour Final Board:")
    print_board(player_board)
    if all(SHIP not in row for row in player_board):
            print("You Win! Congratulations\n")
    else:
        print("Computer Wins! Better luck next time\n")
        print("Would you like to play again?")
        option = input("yes or no?: ").lower()
        while True:
            if option == "yes":
                restart_game()
            elif option == "no":
                print("Thank you for playing battleships")
                break
            else:
                print("Please enter a valid input!")



