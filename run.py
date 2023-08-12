# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import battleships


def game_select():
    """
    Function to choose the game you want to play
    """
    while True:
        print("Welcome to Terminal-games\n")
        print("Please select a game you wish to play\n")
        print("0. Exit Terminal games")
        print("1. Battleships")

        choice = input("Choose your game here:")

        if choice.strip() == "":
            print("Please enter a valid option\n")
            continue

        try:
            choice = int(choice)
            if choice == 1:
                battleships.battleships()
            elif choice == 0:
                print("Thank you for using Terminal Games\n")
                break
            else:
                print("Please enter a valid option\n")
        except ValueError:
            print("Please enter a valid option\n")


game_select()
