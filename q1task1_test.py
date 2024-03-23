import unittest
from io import StringIO
from unittest.mock import patch
import Task_1

class TestCalculateSavings(unittest.TestCase):
    @patch('builtins.input', side_effect=['1','A','10','3','2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_input_output_calls(self, mock_stdout, mock_input):
        Task_1.main()
        expected_output = (f'Choose an action:\n1.Save more money.\n2.End.\n\n'
                           f'In one week, A costs 30.00 euros.\n'
                           f'In one month, A costs 130.35 euros.\nIn one year, A costs 1564.20 euros.\n'
                           f'\nChoose an action:\n1.Save more money.\n2.End.\n\nProgram ends.\n'
                           )       
        
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_calculate_savings(self):
        test_cases = [
                    (['Product A', '10', '3'], "In one week, Product A costs 30.00 euros.\nIn one month, Product A costs 130.35 euros.\nIn one year, Product A costs 1564.20 euros.\n"),
                    (['Product B', '5', '2'],  "In one week, Product B costs 10.00 euros.\nIn one month, Product B costs 43.45 euros.\nIn one year, Product B costs 521.40 euros.\n"),
                    (['Product C', '15', '1'], "In one week, Product C costs 15.00 euros.\nIn one month, Product C costs 65.17 euros.\nIn one year, Product C costs 782.10 euros.\n")
                    ]

        for test in test_cases:
            with patch('builtins.input', side_effect = test[0]), \
                patch('sys.stdout', new=StringIO()) as mock_stdout:
                Task_1.calculate_savings()
        expected_output = test[1]
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
