import unittest
from unittest.mock import patch
import os
from dotenv import load_dotenv
from game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        # Load environment variables for testing
        load_dotenv()
        self.game = Game()

    @patch('builtins.input', side_effect=['5'])
    @patch('builtins.print')
    def test_valid_attempts_selection(self, mock_print, mock_input):
        self.game.start_game()  # This will call get_number_of_guesses internally
        self.assertEqual(self.game.max_attempts_selected, 5)

    @patch('builtins.input', side_effect=['0', '11', '5'])
    @patch('builtins.print')
    def test_invalid_attempts_selection(self, mock_print, mock_input):
        # First two inputs are invalid (out of range), third is valid
        self.game.start_game()
        self.assertEqual(self.game.max_attempts_selected, 5)
        # Check that the validation message was printed for invalid inputs
        print_calls = [call[0][0] for call in mock_print.call_args_list]
        self.assertTrue(any('Please enter a number between' in msg for msg in print_calls[:2]))

    @patch('builtins.input', side_effect=['abc', '5'])
    @patch('builtins.print')
    def test_non_numeric_attempts_selection(self, mock_print, mock_input):
        # First input is non-numeric, second is valid
        self.game.start_game()
        self.assertEqual(self.game.max_attempts_selected, 5)
        # Check that the validation message for invalid input was printed
        print_calls = [call[0][0] for call in mock_print.call_args_list]
        self.assertTrue(any('Invalid input' in msg for msg in print_calls[:1]))

if __name__ == '__main__':
    unittest.main()