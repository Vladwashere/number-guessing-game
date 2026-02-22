import random
import sys


def play_game():
    # Step 1 : Ask for difficulty until the user enters a valid input
    difficulty = ""
    while difficulty not in ["easy", "medium", "hard"]:
        difficulty = input(
            "Choose a difficulty level (easy, medium, hard): ").lower()
        if difficulty not in ["easy", "medium", "hard"]:
            print("Invalid input! Please enter 'easy', 'medium', or 'hard'.")

    # Step 2: Assign values based on difficulty
    if difficulty == "easy":
        max_number = 50
        max_attempts = 15
    elif difficulty == "hard":
        max_number = 500
        max_attempts = 10
    else:  # medium
        max_number = 100
        max_attempts = 10
    # Step 3: Generate a random number
    number = random.randint(1, max_number)
    print(f"\nYou chose {difficulty} difficulty.")
    print(
        f"You have {max_attempts} attempts to guess the number (1-{max_number}).\n")
    attempts = 0
    # Step 4: Game loop
    while attempts < max_attempts:
        try:
            guess = int(input(f"Enter your guess (1-{max_number}): "))
            if not (1 <= guess <= max_number):
                print("Number out of range! Try again.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        attempts += 1

        if guess < number:
            print("Number is too low!")
        elif guess > number:
            print("Number is too high!")
        else:
            print(
                f"Congratulations! You guessed the number in {attempts} attempts!")
            return  # Exit the function properly

        if attempts == max_attempts // 2:
            print("Hint:", "even" if number % 2 == 0 else "odd")
    print(f"Game Over! The number was {number}.")


def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again in ["yes", "y"]:
            continue
        elif play_again in ["no", "n"]:
            print("Thanks for playing! Goodbye!")
            sys.exit()
        else:
            print("Type yes or no.")


if __name__ == "__main__":
    main()
