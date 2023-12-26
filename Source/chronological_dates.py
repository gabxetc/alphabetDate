import date_sorter as chron_ops

app_dates = chron_ops.sort_app_dates
my_dates = chron_ops.sort_my_dates
all_dates = chron_ops.sort_all_dates

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
    go_next = False
    selected = False

    while selected == False and go_next == True:
        for date in app_dates:
            if selected == True:
                chosen_app_date = date[app_date_index]
                go_next = False
                return chosen_app_date
            else:
                app_date_index += 1
                if app_date_index > len(app_dates)-1:
                    app_date_index = 0
                    go_next = True
                else:
                    go_next = True

# Dates made by the user
def chron_my_dates():
    my_date_index = 0
    go_next = False
    selected = False

    while selected == False and go_next == True:
        for date in my_dates:
            if selected == True:
                chosen_app_date = date[my_date_index]
                go_next = False
                return chosen_app_date
            else:
                my_date_index += 1
                if my_date_index > len(my_dates)-1:
                    my_date_index = 0
                    go_next = True
                else:
                    go_next = True

# App dates and Homemade dates combined
def chron_all_dates():
    all_date_index = 0
    go_next = False
    selected = False

    while selected == False and go_next == True:
        for date in all_dates:
            if selected == True:
                chosen_app_date = date[all_date_index]
                go_next = False
                return chosen_app_date
            else:
                all_date_index += 1
                if all_date_index > len(all_dates)-1:
                    all_date_index = 0
                    go_next = True
                else:
                    go_next = True