import sys
sys.path.append('/home/gabxetc/Documents/solutions/alphabetDate')  # Replace this path with your project's root path
import dates.date_sorter as chron_ops

app_dates = chron_ops.sort_app_dates()
my_dates = chron_ops.sort_my_dates()
all_dates = chron_ops.sort_all_dates()
answer = "You have chosen a "

yes = 'yes'
no = 'no'

app_dates_list = 'app'
my_dates_list = 'my'
all_dates_list = 'all'


def select_list():
    choose_list = input("Which list of dates would you list to search? ").lower().strip()
    if choose_list == app_dates_list:
        return chron_app_dates()
    elif choose_list == my_dates_list:
        return chron_my_dates()
    elif choose_list == all_dates_list:
        return chron_all_dates()
    else:
        print("Please enter a valid list.")
        return select_list()

def select_date(selected, go_next):
    while selected == False and go_next == True:
        choose_date = input("Would you like to select this date? ").lower().strip()
        if choose_date == yes:
            double_check = input("Are you sure you would like to choose this date? ")
            if double_check == yes:
                selected = True
                go_next = False
                return True
            else:
                selected = False
                go_next = True
        else:
            selected = False
            go_next = True
            return False

'''The following function monitors the action of iterating through the list of 
dates. It does this by using the index of each date to move through the list.
    - while we haven't selected a date and while we go next
    - we loop through each date in the list of dates
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
def chron_app_dates():
    app_date_index = 0
    go_next = True
    selected = False

    for date in app_dates:
        if select_date(selected, go_next) == True:
            chosen_app_date = app_dates[app_date_index]
            return answer + chosen_app_date
        elif select_date(selected, go_next) == False:
            app_date_index += 1
            if app_date_index > len(app_dates)-1:
                app_date_index = 0
                return select_date(False, True)
            return select_date(False, True)

# Dates made by the user
def chron_my_dates():
    my_date_index = 0
    go_next = False
    selected = False

    for date in my_dates:
        result = select_date(selected, go_next)
        if result == True:
            chosen_app_date = date[my_date_index]
            return "You have selected a " + chosen_app_date
        elif result == False:
            my_date_index += 1
            if my_date_index > len(my_dates)-1:
                my_date_index = 0
                return select_date(False, True)
            return select_date(False, True)

# App dates and Homemade dates combined
def chron_all_dates():
    all_date_index = 0
    go_next = False
    selected = False

    for date in all_dates:
        result = select_date(selected, go_next)
        if result == True:
            chosen_app_date = date[all_date_index]
            return "You have selected a " + chosen_app_date
        elif result == False:
            all_date_index += 1
            if all_date_index > len(all_dates)-1:
                all_date_index = 0
                return select_date(False, True)
            return select_date(False, True)
        