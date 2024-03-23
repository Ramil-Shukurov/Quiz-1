import unittest
from unittest.mock import patch
import io
import Task_3

class TestInflationCalculation(unittest.TestCase):

    @patch('builtins.input', side_effect=["100", "2022", "5", "200", "200", "-101"])
    def test_main_input_calls(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            Task_3.main()
            expected_calls = [
                "Enter the initial sum of money: ",
                "Enter the initial year for the first inflation rate: ",
                f"Enter the inflation rate for 2022 (or enter a number equal to or below -100 to stop): ",
                f"Enter the inflation rate for 2023 (or enter a number equal to or below -100 to stop): ",
                f"Enter the inflation rate for 2024 (or enter a number equal to or below -100 to stop): ",
                f"Enter the inflation rate for 2025 (or enter a number equal to or below -100 to stop): "
            ]
            actual_calls = [call[0][0] for call in mock_input.call_args_list]
            self.assertEqual(actual_calls, expected_calls)

    def test_main_output(self):
        test_cases = [
                    (["100", "2022", "5", "-200"], "The value of 100.00 euros in 2022 is 95.24 euros in 2023.\n"),
                    (['1498.65', '2023', '-2','4','1.5','-100'],  "The inflation rate has gone up since the previous year.\nThe inflation rate has gone down since the previous year.\nThe value of 1498.65 euros in 2023 is 1448.69 euros in 2026.\n"),
                    (['150.3', '2020','-100'], "The value of 150.30 euros in 2020 is 150.30 euros in 2020.\n"),
                    (['1234', '1995','-2.5','-2.5','-2.7','30.1','0.05','-165'], "The inflation rate is the same as in the previous year.\nThe inflation rate has gone down since the previous year.\nThe inflation rate has gone up since the previous year.\nThe inflation rate has gone down since the previous year.\nThe value of 1234.00 euros in 1995 is 1024.94 euros in 2000.\n")
                    ]
        for test in test_cases:
            with patch('builtins.input', side_effect = test[0]), \
                patch('sys.stdout', new=io.StringIO()) as mock_stdout:
                Task_3.main()
            expected_output = test[1]
            self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
