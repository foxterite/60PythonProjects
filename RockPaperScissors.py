import random

# Define the available choices for the game
choices = ["Rock", "Paper", "Scissors"]

# Randomly choose an option for the computer
computer = random.choice(choices)

# Initialize variables for player, computer scores
player = False
cpu_score = 0
player_score = 0

# Start the game loop
while True:
    # Prompt the player to enter their choice (Rock, Paper, or Scissors)
    player = input("Rock, Paper, or Scissors?").capitalize()

    # Conditions for the Rock, Paper, Scissors game
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            cpu_score += 1
        else:
            print("You win!", player, "smashes", computer)
            player_score += 1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            cpu_score += 1
        else:
            print("You win!", player, "covers", computer)
            player_score += 1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            cpu_score += 1
        else:
            print("You win!", player, "cut", computer)
            player_score += 1
    elif player == 'End':
        # Print the final scores and break the loop
        print("Final Scores:")
        print(f"CPU: {cpu_score}")
        print(f"Player: {player_score}")
        break
