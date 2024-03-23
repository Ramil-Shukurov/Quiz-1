import unittest
from unittest.mock import patch
from io import StringIO
import Task_4
from random import randint

class TestApartmentBuilding(unittest.TestCase):

    @patch('builtins.input', side_effect=["3", "4", "flat"])
    def test_main_input_calls(self, mock_input):
        Task_4.main() 
        expected_calls = ["Floors (must be at least 2): ", "Width (excluding walls, must be a non-zero even integer): ", "Roof type ('flat' or 'pointy'): "]
        # Check if input was called with the expected arguments
        self.assertEqual(mock_input.call_args_list, [unittest.mock.call(arg) for arg in expected_calls])

    def test_draw_base(self):
        num = randint(1, 20)
        self.assertEqual(Task_4.draw_base(num), "="*(num+2))

    def test_draw_floor(self):
        num = randint(1, 20)
        self.assertEqual(Task_4.draw_floor(num), f"|{chr(32) * (num)}|")
        num = randint(10, 50)
        self.assertEqual(Task_4.draw_floor(num), f"|{chr(32) * (num)}|")

    def test_draw_ground_floor(self):
        self.assertEqual(Task_4.draw_ground_floor(7), "|  ||  |")
        self.assertEqual(Task_4.draw_ground_floor(8), "|   ||   |")
        self.assertEqual(Task_4.draw_ground_floor(14), "|      ||      |")
        self.assertEqual(Task_4.draw_ground_floor(21), "|         ||         |")

    def test_draw_roof_flat(self):
        self.assertEqual(Task_4.draw_roof(12, "flat"), " ____________\n")
        self.assertEqual(Task_4.draw_roof(17, "flat"), " _________________\n")

    def test_draw_roof_pointy(self):
        expected_output = "    /\\\n   /  \\\n  /    \\\n /      \\\n"
        self.assertEqual(Task_4.draw_roof(8, "pointy"), expected_output)
    
    def test_main(self):
        test_cases = [{'input':['3', '6', 'flat'], 'expected_output':"______\n|      |\n|      |\n|  ||  |\n========"},
                    {'input':['6','8','pointy'], 'expected_output': "/\\\n   /  \\\n  /    \\\n /      \\\n|        |\n|        |\n|        |\n|        |\n|        |\n|   ||   |\n=========="}
                    ]
            
        for test_case in test_cases:
            with patch('builtins.input', side_effect=test_case['input']), \
                 patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_4.main()
            self.assertEqual(mock_stdout.getvalue().strip(), test_case['expected_output'])
 
    
if __name__ == '__main__':
    unittest.main()
