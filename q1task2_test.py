import unittest
from io import StringIO
from unittest.mock import patch
import Task_2

class TestCleaningDays(unittest.TestCase):
    
    def test_cleaning_days_output_another_range(self):
        test_cases = [
                    (['7', '13'], "Cleaning days between 7. - 13.:\n7\n8\nToilet cleaning day (Tenant 1)\nKitchen cleaning day (Tenant 2)\n11\nToilet cleaning day (Tenant 3)\n13\n"),
                    (['1', '5'],  "Cleaning days between 1. - 5.:\n1\n2\nToilet cleaning day (Tenant 1)\n4\nKitchen cleaning day (Tenant 2)\n"),
                    (['25', '34'], "Cleaning days between 25. - 34.:\nKitchen cleaning day (Tenant 1)\n26\nToilet cleaning day (Tenant 2)\n28\n29\nHOUSE CLEANING! Everyone\n31\n32\nToilet cleaning day (Tenant 3)\n34\n")
                    ]
        for test in test_cases:
            with patch('builtins.input', side_effect = test[0]), \
                patch('sys.stdout', new=StringIO()) as mock_stdout:
                Task_2.main()
            expected_output = test[1]
            self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
