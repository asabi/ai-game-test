import unittest
from unittest.mock import patch
import os
from game import get_number_of_guesses

class TestGame(unittest.TestCase):
    def setUp(self):
        # Set default values for testing
        os.environ['MIN_ATTEMPTS'] = '1'
        os.environ['MAX_ATTEMPTS'] = '10'

    @patch('builtins.input', return_value='5')
    @patch('builtins.print')
    def test_valid_input(self, mock_print, mock_input):
        result = get_number_of_guesses()
        self.assertEqual(result, 5)

    @patch('builtins.input', side_effect=['0', '11', '5'])
    @patch('builtins.print')
    def test_invalid_input(self, mock_print, mock_input):
        # First two inputs are invalid (out of range), third is valid
        result = get_number_of_guesses()
        self.assertEqual(result, 5)
        # Check that the validation message was printed twice for invalid inputs
        self.assertTrue(any('Please enter a number between' in call[0][0] for call in mock_print.call_args_list[:2]))

    @patch('builtins.input', side_effect=['abc', '5'])
    @patch('builtins.print')
    def test_non_numeric_input(self, mock_print, mock_input):
        # First input is non-numeric, second is valid
        result = get_number_of_guesses()
        self.assertEqual(result, 5)
        # Check that the validation message for invalid input was printed
        self.assertTrue(any('Invalid input' in call[0][0] for call in mock_print.call_args_list[:1]))

if __name__ == '__main__':
    unittest.main()