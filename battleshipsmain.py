import random
import time


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
    leaderboard = []
    print("Welcome to Battleships\n")
    print("Guess a grid location to sink your opponents 4 ships\n")
    input("Press Enter to begin: ")

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

    def print_board(board, show_ships=True):
        """
        prints the game board 
        this code has a new argument so you can see the ships on your own board 
        but not on computer board
        """
        print('   A B C D E F G H')
        print('  ----------------')
        row_num = 1
        for row in board:
            if show_ships:
                print("%d |%s|" % (row_num, "|".join(row)))
            else:
                print("%d |%s|" % (row_num, "|".join([cell if cell != SHIP else EMPTY for cell in row])))
            row_num += 1
        print('  ----------------')

    player_board = initialize_board()
    computer_board = initialize_board()
    create_ships(player_board)
    create_ships(computer_board)

    time_begin = time.time()

    while any(SHIP in row for row in computer_board):
        print("\n Your Board:")
        print_board(player_board)

        print("\n Computer's Board:")
        print_board(computer_board, show_ships=False)

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
                break  
            except ValueError:
                print("Invalid input. Please enter valid inputs.\n")

        computer_guess_row = random.randint(0, BOARD_SIZE - 1)
        computer_guess_col = random.randint(0, BOARD_SIZE - 1)

        print("\nComputer's Turn:")
        if player_board[computer_guess_row][computer_guess_col] == SHIP:
            print("Computer HIT your ship!")
            player_board[computer_guess_row][computer_guess_col] = HIT
        else:
            print("Computer MISSED!")
            player_board[computer_guess_row][computer_guess_col] = MISS

    end_time = time.time()
    time_taken = end_time - time_begin
    print("\nYour Final Board:")
    print_board(player_board)
    if all(SHIP not in row for row in computer_board):
        print("You Win! Congratulations")
        print(f"You won in {time_taken:.2f} seconds\n")
        player = input("Enter your name: ")
        leaderboard.append((player, time_taken))
        leaderboard = sorted(leaderboard, key=lambda x: x[1])
    
        # Write leaderboard data to the file
        with open("leaderboard.txt", "a") as file:
            for player, time_taken in leaderboard:
                file.write(f"{player}: {time_taken:.2f} seconds\n")
        
    else:
        print("Computer Wins! Better luck next time\n")
    
    while True:
        print("Would you like to play again?")
        option = input("Type in 'yes' to play again or 'no' to go back to the home screen: ").lower()
        if option == "yes":
            battleships()
            break
        elif option == "no":
            print("Thank you for playing Battleships!")
            return
        else:
            print("Please choose a valid option.")

