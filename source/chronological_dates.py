import sys
sys.path.append('/home/gabxetc/Documents/solutions/alphabetDate')  # Replace this path with your project's root path
import dates.date_sorter as chron_ops
from typing import Union

app_dates = chron_ops.sort_app_dates()
my_dates = chron_ops.sort_my_dates()
all_dates = chron_ops.sort_all_dates()
answer = "You have chosen a "

yes = 'yes'
no = 'no'

app_dates_list = 'app'
my_dates_list = 'my'
all_dates_list = 'all'

'''
    The following funtion handles the route of the app
    after choosing which list you'd like to pick a date from.
'''

def select_list():
    date_index = 0
    choose_list = input("Which list of dates would you list to search? ").lower().strip()
    if choose_list == app_dates_list:
        return chron_app_dates(date_index)
    
    elif choose_list == my_dates_list:
        return chron_my_dates(date_index)
    
    elif choose_list == all_dates_list:
        return chron_all_dates(date_index)
    
    else:
        print("Please enter a valid list.")
        return select_list()

'''
    The following function handles the while loop of iterating through dates
    in the chosen list. It does this by:
    - while the user hasn't selcted a date and the program should go to the next date
    - the program will ask if you'd like to select the current date
    if yes:
        - it will ask if you are sure 
        - if you are sure:
            it will return true then go back to the respective date list handler function
        - if you are not sure:
            it will ask you if you would like to choose the current date you are on and continue in the while loop
    if no:
        - it will return false and index to the next date in the respective date list handler function
'''
def select_date(selected, go_next):
    if selected == False and go_next == True:
        choose_date = input("Would you like to select this date? ").lower().strip()
        if choose_date == yes:
            double_check = input("Are you sure you would like to choose this date? ").lower().strip()
            if double_check == yes:
                selected = True
                go_next = False
                return True
            else:
                return select_date(False, True)
        else:
            selected = False
            go_next = True
            return False
    else:
        return True

'''The following function monitors the action of iterating through the list of 
dates. It does this by using a counter to index through each date in the list.
    - while we haven't selected a date and while we go next
    - we check if the user has chosen that date
    - we then check if the user has selected the date
    - if yes:
        - we return the date at the current_app_date (index) and exit the while loop.
    - if no
        - we increment the index by 1
            - if the current index is greater than the length of the list minus 1, we go back to 0
            # We minus 1 because we are wokring with the index size of the list. list length = 5
            # but index starts at 0 so we need to minus one to get the correct range of the list
        - we then change then make go_next true and continue in the for loop.
'''

# Dates provided in the app
def chron_app_dates(date_index):
    go_next = True
    selected = False

    # for date in app_dates: -> we don't need the for loop anymore because we are using conditional statments and function calls for the program
    if select_date(selected, go_next) == True:
        chosen_app_date = app_dates[date_index]
        final_date = answer + chosen_app_date
        return final_date
    else:
        date_index += 1
        if date_index > len(app_dates)-1:
            date_index = 0
            return select_date(False, True)
        return select_date(False, True)

# Dates made by the user
def chron_my_dates(date_index):
    go_next = True
    selected = False

    if select_date(selected, go_next) == True:
        chosen_app_date = my_dates[date_index]
        final_date = answer + chosen_app_date
        return final_date
    else:
        date_index += 1
        if date_index > len(my_dates)-1:
            date_index = 0
            return select_date(False, True)
        return select_date(False, True)

# App dates and Homemade dates combined
def chron_all_dates(date_index): #-> Union[str, bool] Union specifies the return type of the function
    go_next = True
    selected = False

    if select_date(selected, go_next) == True:
        chosen_app_date = all_dates[date_index]
        final_date = answer + chosen_app_date
        return final_date
    else:
        date_index += 1
        if date_index > len(all_dates)-1:
            date_index = 0
            return select_date(False, True)
        return select_date(False, True)

        