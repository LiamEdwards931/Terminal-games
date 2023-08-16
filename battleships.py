import random
import os
import time

"""
For testing, the ships are marked
This is intentional
"""


def battleships():
    """
    function to run the entire code.
    """
    EMPTY = ' '
    SHIP = 'S'
    HIT = 'X'
    MISS = 'O'
    BOARD_SIZE = 8
    NUM_SHIPS = 4
    print("Welcome to Battleships\n")
    print("The aim is to sink your opponent's 4 ships by guessing a grid and column number\n")
    input("Press Enter to Begin: ")

    def initialize_board():
        """
        Initializes the game boards
        """
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
        time.sleep(0.5)

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
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("HIT! You successfully hit a ship\n")
                    computer_board[row_guess][col_dict[column_guess]] = HIT
                elif computer_board[row_guess][col_dict[column_guess]] == HIT or computer_board[row_guess][col_dict[column_guess]] == MISS:
                    print("This position has already been fired at! Try again\n")
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("MISS! You missed a ship\n")
                    computer_board[row_guess][col_dict[column_guess]] = MISS
                break  # Exit the loop if all checks pass
            except ValueError:
                print("Invalid input. Please enter valid inputs.\n")

        computer_guess_row = random.randint(0, BOARD_SIZE - 1)
        computer_guess_col = random.randint(0, BOARD_SIZE - 1)

        print("\nComputer's Turn:")
        if player_board[computer_guess_row][computer_guess_col] == SHIP:
            print("Computer HIT your ship!\n")
            player_board[computer_guess_row][computer_guess_col] = HIT
        else:
            print("Computer MISSED!\n")
            player_board[computer_guess_row][computer_guess_col] = MISS
            print("Updating Board...")
            time.sleep(1.5)

 
    print("\nYour Final Board:")
    print_board(player_board)
    if all(SHIP not in row for row in computer_board):
        print("You Win! Congratulations\n")
    else:
        print("Computer Wins! Better luck next time\n")

    while True:
        print("Would you like to play again?")
        option = input("Type in 'yes' to play again or 'no' to go back to the home screen: ").lower()
        if option == "yes":
            os.system('cls' if os.name == 'nt' else 'clear')
            battleships()
            break
        elif option == "no":
            print("Thank you for playing Battleships!")
            os.system('cls' if os.name == 'nt' else 'clear')
            return
        else:
            print("Please choose a valid option.")
