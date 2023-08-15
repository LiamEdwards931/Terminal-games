def print_leaderboard():
    print("Battleships Main")
    try:
        with open("leaderboard.txt", "r") as file:
            print("Leaderboard:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Leaderboard is empty.")

