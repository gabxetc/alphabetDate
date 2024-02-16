import unittest
from unittest import mock
import source
import dates
import programme
from unittest.mock import patch
from io import StringIO
import os
import source.homemade_dates as homemade
import dates.date_sorter as sort
class MyChronTestCase(unittest.TestCase):
    #This function ensures that the input is correctly converted to "title"
    @patch("sys.stdin", StringIO("Bounce dAte\nshopping date\nCOSTUME DATE\nice-cream Date"))
    def test_input_correction(self):
        self.assertEqual(homemade.ask_for_date(), "Bounce date")
        self.assertEqual(homemade.ask_for_date(), "Shopping date")
        self.assertEqual(homemade.ask_for_date(), "Costume date")
        self.assertEqual(homemade.ask_for_date(), "Ice cream date")

    #This method ensures that if a non alpha input is given, the correct response is given
    @patch("sys.stdin", StringIO("1\n@\n"))
    def test_incorrect_input(self):
        self.assertEqual(homemade.ask_for_date(), "Please enter a valid date idea.")
        self.assertEqual(homemade.ask_for_date(), "Please enter a valid date idea.")

    #This method ensures that add_my_dates correctly writes a homemade date to the my_dates.txt file
    # Try implement setUp and tearDown testing method
    #@unittest.skip('Work in progress')
    @patch("sys.stdin", StringIO("zoo date\nBounce dAte\nshopping date\nCOSTUME DATE\nice-cream Date"))
    def test_write_to_txt(self):
        self.assertIn(homemade.ask_for_date(),homemade.get_new_file())
        self.assertIn(homemade.ask_for_date(),homemade.get_new_file())
        self.assertIn(homemade.ask_for_date(),homemade.get_new_file())
        self.assertIn(homemade.ask_for_date(),homemade.get_new_file())
        self.assertIn(homemade.ask_for_date(),homemade.get_new_file())

if __name__ == "__main__":
    unittest.main()