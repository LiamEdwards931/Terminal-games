def print_leaderboard():
    """
    Prints the data from the battleships leaderboard
    """
    print("Battleships Main Leaderboard")
    try:
        with open("leaderboard.txt", "r") as file:
            print("Leaderboard:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Leaderboard is empty.")

