import date_sorter as home_ops

my_dates = home_ops.sort_my_dates

'''The following funtions are intended to ask ask the user to input their date idea
Then the programme will access the my_dates text file and write their inputed date
to the file without overwriting the current state of the file. If the inputed date idea
is already in the file, it will not write to the file and instead prompt the user to 
enter a new/different date
'''

def ask_for_date():
    my_own_date = input("Type your date idea:\n")
    return my_own_date

def add_my_dates(my_own_date):
    with open('my_dates.txt', 'a') as file:
        file.seek(0)
        # if my_own_date not in my_dates: 
        '''I'm not sure if i want to check inside 
        the sorted list for the value or in the file for the value'''
        if my_own_date not in file.read():
            file.write(my_own_date)
            file.write('\n')
        else:
            print("This type of date already exists!")
            return ask_for_date()