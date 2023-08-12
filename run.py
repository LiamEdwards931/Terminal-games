# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def start():
    print("Welcome to Terminal-games")
    print("Please select a game you wish to play")
    print("0.Exit Terminal Games")
    print("1.Battleships\n")
    
    game_select()
    

def game_select():
    """
    Function to choose the game you want to play
    """
    while True:
        print("Welcome to Terminal-games")
        print("Please select a game you wish to play")
        print("1. Battleships")
        print("0. Exit")

        choice = int(input("Choose your game here:"))

        if choice == 1:
            from battleships import battleships
        elif choice == 0:
            print("Thank you for using Terminal Games")
            break
        else:
            print("Please enter a valid option")

game_select()

         


start()





