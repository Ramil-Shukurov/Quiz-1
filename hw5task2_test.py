import unittest
from unittest.mock import patch
from io import StringIO
import Task_2

class TestParityBit(unittest.TestCase):
    
    def test_parity_bit_even(self):
        expected_output = "The parity bit should be 0"
        test_cases = [["11011110", "end"], ["10011010", "end"], ["11111111", "end"], ["01011111", "end"], ["00011000", "end"]]

        for test_case in test_cases:
            with patch('builtins.input', side_effect=test_case), \
                 patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_2.main()
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
    
    def test_parity_bit_odd(self):
        expected_output = "The parity bit should be 1"
        test_cases = [["11111110", "end"], ["10011110", "end"], ["01111111", "end"], ["01011011", "end"], ["00011001", "end"]]

        for test_case in test_cases:
            with patch('builtins.input', side_effect=test_case), \
                 patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_2.main()
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
    
    def test_invalid_input(self):
        expected_output = "That was not 8 bits ... Try again"
        test_cases = [["1111110", "end"], ["111110", "end"], ["011111111", "end"], ["0011", "end"], ["00101", "end"]]

        for test_case in test_cases:
            with patch('builtins.input', side_effect=test_case), \
                 patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_2.main()
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

if __name__ == "__main__":
    unittest.main()
