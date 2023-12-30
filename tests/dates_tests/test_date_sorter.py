import unittest
from io import StringIO
import Source
import Dates.date_sorter as sorting
import Programme


class MySorterTestCase(unittest.TestCase):
    # This test ensures that that the necessary functions sort the dates in ascending order
    #DONE: Fix this test so it doesn't rely on one specific txt file and is adaptable to any test file 
    def test_sort_app_dates(self):
        self.assertEqual(sorting.sort_app_dates(),['Candle-light dinner date\n', 'Compassion date\n', 'Dance date\n', 'Double date\n', 'Elegant date\n', 'Friends date\n', 'Impromptu date\n', 'Lunch date\n', 'Make-up date\n', 'Movie date\n', 'Old love date\n', 'Picnic date\n', 'Special moment date\n', 'Sports date\n', 'Stay-at-home date\n', 'Travel date\n', 'Walk date\n'])

    #This is a fix of the "test_sort_app_dates"
    def test_sort_my_dates_mod(self):
        self.assertEqual(sorting.sort_app_dates(), sorting.get_app_dates())

    #This test ensures that the my_dates.txt file is successfully sorted
    def test_sort_my_dates(self):
        self.assertEqual(sorting.sort_my_dates(), sorting.get_my_dates())

if __name__ == '__main__':
    unittest.main()