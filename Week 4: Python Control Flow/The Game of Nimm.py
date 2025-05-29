def main():
    stones = 20                   # Start with 20 stones
    player = 1                    # Player 1 starts

    while stones > 0:
        print(f"There are {stones} stones left.")
        print(f"Player {player} would you like to remove 1 or 2 stones?", end=" ")

        # Get valid input (Milestone 3)
        stones_to_remove = int(input())
        while stones_to_remove not in [1, 2]:
            stones_to_remove = int(input("Please enter 1 or 2: "))

        # If player tries to remove more stones than available, limit it
        if stones_to_remove > stones:
            stones_to_remove = stones

        stones -= stones_to_remove
        print()

        if stones == 0:
            # Game over, current player loses, other wins
            winner = 2 if player == 1 else 1
            print(f"Player {winner} wins!")
            break

        # Alternate player (Milestone 2)
        player = 2 if player == 1 else 1

if __name__ == "__main__":
    main()
