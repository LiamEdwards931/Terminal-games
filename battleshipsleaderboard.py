def print_leaderboard():
    """
    Prints the data from the battleships leaderboard
    """
    print("Battleships Main Leaderboard")
    try:
        with open("leaderboard.txt", "r") as file:
            leaderboard = [line.strip().split(": ") for line in file.readlines()]
            leaderboard = [(player, float(time)) for player, time in leaderboard]
            leaderboard = sorted(leaderboard, key=lambda x: x[1])
            
            if leaderboard:
                print("Leaderboard:")
                for rank, (player, time_taken) in enumerate(leaderboard, start=1):
                    print(f"{rank}. {player}: {time_taken:.2f} seconds")
            else:
                print("Leaderboard is empty.")
    except FileNotFoundError:
        print("Leaderboard is empty.")


