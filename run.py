# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
def start():
    print("Welcome to Terminal-games")
    print("Please select a game you wish to play")
    print("1.Battleships\n")
    
def game_select():
    input("Choose your game here:")
    while True:
        if input == "1":
            battleships()
        else:
            print("Please enter the number of the game you wish to play")
            input("Choose your game here:")


start()
game_select()
