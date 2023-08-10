
def start():
    print("Welcome to Terminal-games")
    print("Please select a game you wish to play")
    print("1.Battleships\n")
    game_select()
    
def game_select():
    choice = input("Choose your game here:")
    while True:
        if choice == "1":
            battleships()
        else:
            print("Please enter the number of the game you wish to play")
            input("Choose your game here:")


