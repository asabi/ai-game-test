# Guessing Game

This is a simple guessing game where players can select the number of guesses at the beginning of the game. The game now has a Streamlit interface for better user experience.

## Setup

1. Clone the repository:
   ```
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your desired minimum and maximum attempts:
   ```
   MIN_ATTEMPTS=1
   MAX_ATTEMPTS=10
   ```

4. Run the Streamlit game interface:
   ```
   streamlit run streamlit_game.py
   ```

## Configuration

You can configure the minimum and maximum number of guesses by modifying the `.env` file.

## Testing

To test the game, simply run it with different values in the `.env` file.