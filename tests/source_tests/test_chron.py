import unittest
from io import StringIO
from unittest.mock import patch
import source
import dates
import programme
import source.chronological_dates as chron

#These tests are for the chronological aspect of the application
class MyChronTestCase(unittest.TestCase):

    #This method ensures that a file that is not empty exists
    def test_not_empty(self):
        with open("Dates/app_dates.txt", 'r') as file:
            self.assertIsNotNone(file)
    
    @patch("sys.stdin", StringIO("APP\nPicnic Date\nyes\nyes"))
    def test_select_list(self):
        self.assertEqual(chron.select_list(), chron.chron_app_dates())


    #This method ensures that a date is chosen chronologically from the app_dates.txt
    @unittest.skip("demonstrating skipping")
    def test_chron_app_dates(self):
        
        pass

    #This method ensures that a date is chosen chronologically from the my_dates.txt
    @unittest.skip("demonstrating skipping")
    def test_chron_my_dates(self):
        pass

    #This method ensures that a date is chosen chronologically from a combo of built in dates and homemade dates
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

if __name__ == '__main__':
    unittest.main()
    