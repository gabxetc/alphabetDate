import random
import sys
import date_sorter as rand_ops

'''The following funtions select a random date
from the different lists of dates and saves it 
in a variable of the respective name; ie. built in app dates,
consumer made dates and a list that is a combo of those two lists'''

#here we choose a random int within the range of 0 to the length of the date list
#this number represents the index of the date in the list
#we then find the date at that index and store it in a variable which we also return

app_dates = rand_ops.sort_app_dates
my_dates = rand_ops.sort_my_dates
all_dates = rand_ops.sort_all_dates

# Dates provided in the app
def choose_rand_app_date():
    rand_app_date = random.randint(0, len(app_dates)-1)
    chosen_app_date = app_dates[rand_app_date]
    return chosen_app_date

# Dates made by the user
def choose_rand_my_date():
    rand_my_date = random.randint(0, len(my_dates)-1)
    chosen_my_date = my_dates[rand_my_date]
    return chosen_my_date

# App dates and Homemade dates combined
def choose_rand_all_date():
    rand_all_date = random.randint(0, len(all_dates)-1)
    chosen_all_date = all_dates[rand_all_date]
    return chosen_all_date