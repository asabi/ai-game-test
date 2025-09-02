import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_number_of_guesses():
    """
    Prompts the user to select the number of guesses for the game.
    Validates that the selected number is within an acceptable range,
    which is defined by MIN_GUESSES and MAX_GUESSES environment variables.
    """
    min_guesses = int(os.getenv('MIN_GUESSES', 3))
    max_guesses = int(os.getenv('MAX_GUESSES', 10))

    while True:
        try:
            num_guesses = int(input(f"Select number of guesses ({min_guesses}-{max_guesses}): "))
            if min_guesses <= num_guesses <= max_guesses:
                return num_guesses
            else:
                print(f"Please enter a number between {min_guesses} and {max_guesses}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def play_game():
    """
    Main game function that initializes the game with user-selected number of guesses
    and enforces this limit throughout the gameplay.
    """
    num_guesses = get_number_of_guesses()
    print(f"You have selected {num_guesses} guesses.")

    # Game logic here (not shown for brevity)
    # ...

if __name__ == "__main__":
    play_game()