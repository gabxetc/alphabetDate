import unittest
from io import StringIO
from unittest.mock import patch
import source
import dates
import programme
import source.chronological_dates as chron
import dates.date_sorter as dating

answer = "You have chosen a "


# These tests are for the chronological aspect of the application
class MyChronTestCase(unittest.TestCase):
    # This method ensures that a file that is not empty exists
    def test_not_empty(self):
        with open("dates/app_dates.txt", "r") as file:
            self.assertIsNotNone(file)
    
    #This method tests selecting the first date from the app list of dates
    @patch("sys.stdin", StringIO("APP\nyes\nyes"))
    def test_select_app_list(self):
        self.assertEquals(chron.select_list(), answer + (dating.sort_app_dates())[0])

    #This method tests selecting the second date from the app list of dates
    @patch("sys.stdin", StringIO("APP\nno\nyes\nyes"))
    def test_select_second_date_app_list(self):
        self.assertEquals(chron.select_list(), answer + (dating.sort_app_dates())[1])
    
    #This method tests selecting the first date from your list of dates
    @patch("sys.stdin", StringIO("mY\nyes\nyes"))
    def test_select_my_list(self):
        self.assertEquals(chron.select_list(), answer + (dating.sort_my_dates())[0])

    #This method tests selecting the first date from all lists of dates
    @patch("sys.stdin", StringIO("all\nyes\nyes"))
    def test_select_all_list(self):
        self.assertEquals(chron.select_list(), answer + (dating.sort_all_dates())[0])

    #This method tests selecting the incorrect input of choosing a list then the correct input
    @patch("sys.stdin", StringIO("jgbsdg\nall\nyes\nyes"))
    def test_select_all_list(self):
        self.assertEquals(chron.select_list(), answer + (dating.sort_all_dates())[0])

    # This method ensures that a date is chosen chronologically from the app_dates.txt
    @unittest.skip("demonstrating skipping")
    def test_chron_app_dates(self):
        pass

    # This method ensures that a date is chosen chronologically from the my_dates.txt
    @unittest.skip("demonstrating skipping")
    def test_chron_my_dates(self):
        pass

    # This method ensures that a date is chosen chronologically from a combo of built in dates and homemade dates
    @unittest.skip("demonstrating skipping")
    def test_chron_all_dates(self):
        pass

    # def test_correct_date(self):
    #     with open("tests/test_app_dates.txt", 'r') as file:
    #         app_dates = file.readlines()
    #         for date in app_dates:
    #             self.assertEqual(date[0], 'Cookie date')

    #    def test_step1(self):
    #     words = hangman.read_file('tests/test_list.txt')
    #     self.assertEqual(2, len(words))
    #     self.assertEqual('abc\n', words[0])
    #     self.assertEqual('def', words[1])


if __name__ == "__main__":
    unittest.main()
