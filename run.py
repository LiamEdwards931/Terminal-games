import battleships
import battleshipsmain
import battleshipsleaderboard
import os


def game_select():
    """
    Function to choose the game you want to play
    """
    while True:
        print("Welcome to Terminal-games\n")
        print("Please select a game you wish to play\n")
        print("0. Exit Terminal games")
        print("1. Battleships'Test version'")
        print("2. Battleships Main Game")
        print("3. Battleships Leaderboard")

        choice = input("Choose the number of the game you wish to play:")

        if choice.strip() == "":
            print("Please enter a valid option\n")
            continue

        try:
            choice = int(choice)
            if choice == 0:
                print("Thank you for using Terminal Games\n")
                break
            elif choice == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                battleships.battleships()
            elif choice == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                battleshipsmain.battleships()
            elif choice == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                battleshipsleaderboard.print_leaderboard()
            else:
                print("Please enter a valid option\n")
        except ValueError:
            print("Please enter a valid option\n")


game_select()
