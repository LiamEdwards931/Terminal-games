def print_leaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            print("Battleship Main Leaderboard:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Leaderboard is empty.")

