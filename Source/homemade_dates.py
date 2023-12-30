import Dates.date_sorter as home_ops

my_dates = home_ops.sort_my_dates

'''The following funtions are intended to ask ask the user to input their date idea
Then the programme will access the my_dates text file and write their inputed date
to the file without overwriting the current state of the file. If the inputed date idea
is already in the file, it will not write to the file and instead prompt the user to 
enter a new/different date
'''
# Change input to capitalise each first letter of a word
# Replace dashes with a space
# Split the input by spaces and into a list[str]
# join the words together to make one string and not a list[str]
def ask_for_date():
    my_own_date = input("Type your date idea: ").title().replace("-"," ").split(" ")
    for i in my_own_date:
        if i.isalpha() == False:
            return ask_for_date and "Please enter a valid date idea."
    final_date = " ".join(my_own_date)
    return final_date

def add_my_dates(my_own_date):
    with open('Dates/my_dates.txt', 'a') as file:
        # moves the file pointer to the beginning before reading, 
        # so that we can check if the date already exists in the file.
        file.seek(0)
        # if my_own_date not in my_dates: 
        '''I'm not sure if i want to check inside 
        the sorted list for the value or in the file for the value'''
        if my_own_date not in file.readlines():
            file.write(my_own_date)
            file.write('\n')
            return file
        else:
            print("This type of date already exists!")
            return ask_for_date()
        
def get_new_file():
    my_own_date = ask_for_date()
    final_file = add_my_dates(my_own_date)
    return final_file