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

        print("\n Computer's Board:")
        print_board(computer_board)

    # Players turn
        while True:
            try:
                column_guess = str(input("Guess a column (A-H): ")).strip().upper()
                row_guess_input = input("Guess a Row (1-8): ").strip()
            
                if not column_guess or not row_guess_input:
                    print("Please enter both column and row.\n")
                    continue
            
                row_guess = int(row_guess_input) - 1
                
                col_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
                if column_guess not in col_dict:
                    print("That is not a valid column. Try again\n")
                    continue

                if row_guess < 0 or row_guess >= BOARD_SIZE:
                    print("Invalid row. Try again.\n")
                    continue

                if computer_board[row_guess][col_dict[column_guess]] == SHIP:
                    print("HIT! You successfully hit a ship\n")
                    computer_board[row_guess][col_dict[column_guess]] = HIT
                elif computer_board[row_guess][col_dict[column_guess]] == HIT or computer_board[row_guess][col_dict[column_guess]] == MISS:
                    print("This position has already been fired at! Try again\n")
                else:
                    print("MISS! You missed a ship\n")
                    computer_board[row_guess][col_dict[column_guess]] = MISS
                break  # Exit the loop if all checks pass
            except ValueError:
                print("Invalid input. Please enter valid inputs.\n")

    def restart_game():
        battleships()

    print("\nYour Final Board:")
    print_board(player_board)
    if all(SHIP not in row for row in computer_board):
        print("You Win! Congratulations\n")
    else:
        print("Computer Wins! Better luck next time\n")
    print("Would you like to play again?")
    option = input("Type in yes to play again or any key to quit: ").lower()
    if option == "yes":
        restart_game()
    else:
        return


