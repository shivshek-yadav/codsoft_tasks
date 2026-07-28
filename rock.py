import random

continue_game = True

while continue_game:
    # Get user input
    user_choice = int(input("\n0 for Rock\n1 for Paper\n2 for Scissors\nEnter your choice: "))

    # Check for invalid input
    if user_choice < 0 or user_choice >= 3:
        print("Invalid choice, please choose 0, 1, or 2.")
        continue  # Restart the loop for a valid input

    # Print user's choice
    print(f"You chose {user_choice}: ", end="")
    if user_choice == 0:
        print("Rock")
    elif user_choice == 1:
        print("Paper")
    elif user_choice == 2:
        print("Scissors")

    # Generate computer's choice
    computer_choice = random.randint(0, 2)
    print("Computer chose: ", end="")
    if computer_choice == 0:
        print("Rock")
    elif computer_choice == 1:
        print("Paper")
    elif computer_choice == 2:
        print("Scissors")

    # Determine the result
    if computer_choice == user_choice:
        print("It's a draw.")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose.")

    # Ask to continue or stop the game
    x = input("Continue the game (yes/no)? ").strip().lower()
    if x == "no":
        continue_game = False

print("Thanks for playing!")