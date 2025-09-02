import os
import unittest
from unittest.mock import patch
from game import get_number_of_guesses

class TestGame(unittest.TestCase):
    def setUp(self):
        # Set default environment variables for testing
        os.environ['MIN_GUESSES'] = '3'
        os.environ['MAX_GUESSES'] = '10'

    @patch('builtins.input', return_value='5')
    @patch('builtins.print')
    def test_valid_guess_count(self, mock_print, mock_input):
        num_guesses = get_number_of_guesses()
        self.assertEqual(num_guesses, 5)

    @patch('builtins.input', side_effect=['2', '11', '7'])
    @patch('builtins.print', return_value=None)
    def test_invalid_then_valid_guess_count(self, mock_print, mock_input):
        num_guesses = get_number_of_guesses()
        self.assertEqual(num_guesses, 7)

if __name__ == '__main__':
    unittest.main()