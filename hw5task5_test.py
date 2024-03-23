import unittest
from unittest.mock import patch
import Task_5
from io import StringIO

class TestUsernameValidation(unittest.TestCase):
    
    def test_is_neighbor_numbers_true(self):
        self.assertTrue(Task_5.is_neighbor_numbers("ab333de"))
    
    def test_is_neighbor_numbers_false(self):
        self.assertFalse(Task_5.is_neighbor_numbers("abcde"))
    
    def test_is_letter_exist_true(self):
        self.assertTrue(Task_5.is_letter_exist("abcde123"))
    
    def test_is_letter_exist_false(self):
        self.assertFalse(Task_5.is_letter_exist("123456"))
    
    def test_is_number_exist_true(self):
        self.assertTrue(Task_5.is_number_exist("abcde123"))
    
    def test_is_number_exist_false(self):
        self.assertFalse(Task_5.is_number_exist("abcde"))
    
    def test_is_neighbor_letters_true(self):
        self.assertTrue(Task_5.is_neighbor_letters("abc"))
    
    def test_is_neighbor_letters_false(self):
        self.assertFalse(Task_5.is_neighbor_letters("a2b3c1d"))
    
    def test_is_space_exist_true(self):
        self.assertTrue(Task_5.is_space_exist("a b c"))
    
    def test_is_space_exist_false(self):
        self.assertFalse(Task_5.is_space_exist("abc"))
    
    def test_is_beginning_digit_true(self):
        self.assertTrue(Task_5.is_beginning_digit("123ac"))
    
    def test_is_beginning_digit_false(self):
        self.assertFalse(Task_5.is_beginning_digit("abc123"))
    
    """    def test_main_input(self):
        with patch('builtins.input', side_effect=["username123"]), \
             patch('sys.stdout', new=StringIO()) as mock_stdout:
            Task_5.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Correct username!")
    """
    def test_main_wrong_input(self):
        expected_output = f'Wrong! The same 3 numbers cannot be neighbor numbers!\nWrong! There cannot be an empty space!\nWrong! It cannot start with a digit!'
                
        with patch('builtins.input', side_effect=["12us555na me"]), \
             patch('sys.stdout', new=StringIO()) as mock_stdout:
            Task_5.main()
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

if __name__ == "__main__":
    unittest.main()
