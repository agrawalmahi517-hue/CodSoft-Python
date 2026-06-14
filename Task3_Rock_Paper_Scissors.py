import random

# Initialize scores
user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

print("===== Rock Paper Scissors Game =====")

while True:
    # User input
    user_choice = input("\nEnter rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        continue

    # Computer choice
    computer_choice = random.choice(choices)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    # Game logic
    if user_choice == computer_choice:
        print("It's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Congratulations! You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    # Display scores
    print("\nCurrent Score:")
    print("You:", user_score)
    print("Computer:", computer_score)

    # Play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nFinal Score:")
        print("You:", user_score)
        print("Computer:", computer_score)
        print("Thank you for playing!")
        break
