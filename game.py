import os
import sys

def get_number_of_guesses():
    """Prompt user to select number of guesses with validation."""
    min_attempts = int(os.getenv('MIN_ATTEMPTS', 1))
    max_attempts = int(os.getenv('MAX_ATTEMPTS', 10))

    while True:
        try:
            num_guesses = input(f"Please enter the number of guesses (between {min_attempts} and {max_attempts}): ")
            num_guesses = int(num_guesses)

            if min_attempts <= num_guesses <= max_attempts:
                return num_guesses
            else:
                print(f"Please enter a number between {min_attempts} and {max_attempts}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    """Main game loop."""
    num_guesses = get_number_of_guesses()
    print(f"You have selected {num_guesses} guesses.")

    # Game logic would go here
    # ...

if __name__ == "__main__":
    main()