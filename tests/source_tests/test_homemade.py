import unittest
from unittest import mock
import Source
import Dates
import Programme
from unittest.mock import patch
from io import StringIO
import os
from io import StringIO  
import Source.homemade_dates as homemade

class MyChronTestCase(unittest.TestCase):
    #This function ensures that the input is correctly converted to "title"
    @patch("sys.stdin", StringIO("Bounce dAte\nshopping date\nCOSTUME DATE\nice-cream Date"))
    def test_input_correction(self):
        self.assertEqual(homemade.ask_for_date(), "Bounce Date")
        self.assertEqual(homemade.ask_for_date(), "Shopping Date")
        self.assertEqual(homemade.ask_for_date(), "Costume Date")
        self.assertEqual(homemade.ask_for_date(), "Ice Cream Date")

    #This method ensures that if a non alpha input is given, the correct response is given
    @patch("sys.stdin", StringIO("1\n@\n"))
    def test_incorrect_input(self):
        self.assertEqual(homemade.ask_for_date(), "Please enter a valid date idea.")
        self.assertEqual(homemade.ask_for_date(), "Please enter a valid date idea.")

    #This method ensures that add_my_dates correctly writes a homemade date to the my_dates.txt file
    #@unittest.skip('Work in progress')
    def test_write_to_txt(self):
        pass

if __name__ == "__main__":
    unittest.main()