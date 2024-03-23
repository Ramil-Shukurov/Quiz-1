import unittest
import Task_3
from io import StringIO
from unittest.mock import patch

class TestPigLatin(unittest.TestCase):
    
    def test_main_with_vowel(self):
        test_cases = {'hello': 'Translated text: ellohay', 'awesome': 'Translated text: awesomeway', 'pass': 'Translated text: asspay', 'spaces': 'Translated text: acesspay', 'python': 'Translated text: onpythay', 'attribute': 'Translated text: attributeway', 'terminal': 'Translated text: erminaltay', 'failure': 'Translated text: ailurefay', 'selection': 'Translated text: electionsay', ' practices and problems': 'Translated text: acticespray andway oblemspray', 'cloudy': 'Translated text: oudyclay', 'zodiac': 'Translated text: odiaczay', 'remember thinker': 'Translated text: ememberray inkerthay'}
        for key, val in test_cases.items():
            with patch('builtins.input', return_value=key), \
                 patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_3.main()
            self.assertEqual(mock_stdout.getvalue().strip(), val)
    def test_main_without_vowel(self):
        test_cases = {'by fry': 'Translated text: byay fryay', 'fly': 'Translated text: flyay', 'myc': 'Translated text: mycay', 'hmm shy spy': 'Translated text: hmmay shyay spyay', 'why gyms': 'Translated text: whyay gymsay', 'shhh': 'Translated text: shhhay', 'lynx': 'Translated text: lynxay', 'try': 'Translated text: tryay', 'dry': 'Translated text: dryay', 'gym': 'Translated text: gymay', 'cry': 'Translated text: cryay'}
        for key, val in test_cases.items():
            with patch('builtins.input', return_value=key), \
                 patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_3.main()
            self.assertEqual(mock_stdout.getvalue().strip(), val)

if __name__ == "__main__":
    unittest.main()
