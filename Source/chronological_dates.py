import date_sorter as chron_ops

app_dates = chron_ops.sort_app_dates
my_dates = chron_ops.sort_my_dates
all_dates = chron_ops.sort_all_dates

'''The following function monitors the action of iterating through the list of 
dates. It does this by using the index of each date to move through the list.
    - we lookp through each date in the list of dates
    - we check if the user has clicked next
    - if yes:
        - we increment the index by 1
            - if the current index is greater than the length of the list, we go back to 0
        - we then retreieve the date via the current_app_date (index)
        - and return that date
    -if no
        - we return the date at the current_app_date (index)
'''

def chron_app_dates():
    current_app_date = 0
    go_next = False

    for date in app_dates:
        if go_next == True:
            current_app_date += 1
            if current_app_date > len(app_dates):
                current_app_date = 0
            chosen_app_date = date[current_app_date]
            return chosen_app_date
        else:
            chosen_app_date = date[current_app_date]
            return chosen_app_date
        

def chron_my_dates():
    pass

def chron_all_dates():
    pass