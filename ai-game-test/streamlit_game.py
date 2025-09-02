import streamlit as st
import random
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
min_attempts = int(os.getenv('MIN_ATTEMPTS', 1))
max_attempts = int(os.getenv('MAX_ATTEMPTS', 10))

class Game:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.game_over = False
        self.target_number = None
        self.max_attempts_selected = min_attempts

    def new_level(self):
        """Start a new level with a new target number"""
        self.target_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.guesses = []
        st.session_state.game_message = f"Level {self.level}: Guess the number between 1 and 100"

    def check_guess(self, guess):
        """Check if the guess is correct and update game state"""
        st.session_state.attempts += 1

        if guess < self.target_number:
            st.session_state.game_message = "Too low! Try again."
        elif guess > self.target_number:
            st.session_state.game_message = "Too high! Try again."
        else:
            st.session_state.game_message = f"Correct! You've guessed the number {self.target_number}."
            self.score += (self.max_attempts_selected - st.session_state.attempts + 1) * 10
            self.level += 1
            return True

        if st.session_state.attempts >= self.max_attempts_selected:
            st.session_state.game_message = f"Out of attempts! The number was {self.target_number}."
            return False

        return None

# Initialize game state in session state
if 'game' not in st.session_state:
    st.session_state.game = Game()
    st.session_state.game.new_level()

if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
    st.session_state.guesses = []
    st.session_state.game_message = ""

# Streamlit UI
st.title("Number Guessing Game")

# Select number of attempts per level
max_attempts_selected = st.slider(
    "Select number of guesses per level",
    min_value=min_attempts,
    max_value=max_attempts,
    value=st.session_state.game.max_attempts_selected
)
st.session_state.game.max_attempts_selected = max_attempts_selected

# Display current game state
st.write(st.session_state.game_message)

# Get user guess
guess = st.number_input(
    "Enter your guess (between 1 and 100):",
    min_value=1,
    max_value=100,
    value=None,
    key="guess_input"
)

if st.button("Submit Guess"):
    if guess is None:
        st.error("Please enter a valid number")
    else:
        result = st.session_state.game.check_guess(guess)
        st.session_state.guesses.append(guess)

        if result is True:
            # Move to next level
            st.session_state.game.new_level()
        elif result is False:
            # End game or ask to continue
            if st.button("Next Level"):
                st.session_state.game.new_level()

# Display game stats
st.sidebar.header("Game Stats")
st.sidebar.write(f"Current Score: {st.session_state.game.score}")
st.sidebar.write(f"Level: {st.session_state.game.level}")
st.sidebar.write(f"Attempts this level: {st.session_state.attempts}/{max_attempts_selected}")
st.sidebar.write("Previous guesses:")
for i, g in enumerate(st.session_state.guesses):
    st.sidebar.write(f"{i+1}. {g}")

# End game option
if st.button("End Game"):
    st.session_state.game.game_over = True
    st.write(f"Game Over! Final Score: {st.session_state.game.score}")