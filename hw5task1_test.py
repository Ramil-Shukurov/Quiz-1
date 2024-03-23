import unittest
from io import StringIO
from unittest.mock import patch
import Task_1  # Import your script here

class TestMainFunction(unittest.TestCase):
    def test_main_multiple_inputs(self):
        # Define multiple test cases with different input sentences
        test_cases = [
            ("Hello     World", "The modified string is:\nHello World\n"),
            ("  Good   morning   everyone  ", "The modified string is:\nGood morning everyone\n"),
            ("This  is  a  test", "The modified string is:\nThis is a test\n"),
            ("NoSpaces", "The modified string is:\nNoSpaces\n")
        ]

        for input_sentence, expected_output in test_cases:
            with patch('builtins.input', side_effect=[input_sentence]), \
                 patch('sys.stdout', new=StringIO()) as mock_stdout:
                Task_1.main()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
