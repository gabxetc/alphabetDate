import dates.date_sorter as home_ops

my_dates = home_ops.sort_my_dates()
yes = 'yes'
no = 'no'

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
    my_own_date = input("Type your date idea: ").strip().capitalize().replace("-"," ").split(" ")
    for i in my_own_date:
        if i.isalpha() == False:
            return ask_for_date and "Please enter a valid date idea."
    final_date = " ".join(my_own_date)
    return final_date

def ask_again():
    try_again = input("Would you still like to add a new date to your personal list of dates?").lower().strip()
    if try_again == yes:
        add_my_dates()
    else:
        print("Alright, goodbye!")


def add_my_dates():
    my_own_date = ask_for_date()
    file_path = 'dates/my_dates.txt'

    with open(file_path, 'a+') as file:
        my_dates = [line.strip() for line in file.readlines()]
        
        if my_own_date in my_dates:
            print("This type of date already exists!")
            ask_again()
        else:
            file.write(my_own_date + '\n')
            return file
        
    # my_own_date = ask_for_date()
    # file = open('dates/my_dates.txt', 'a+')
    # my_dates = file.readlines()
    # if my_own_date in my_dates:
    #     print("This type of date already exists!")
    #     ask_again()
    # else:
    #     file.write(my_own_date)
    #     file.write('\n')
    #     file.close()
    #     return str(file)
    
    
    # with open('dates/my_dates.txt', 'a+') as file:
    #     # file.seek(0) moves the file pointer to the beginning before reading, 
    #     # so that we can check if the date already exists in the file.
    #     with open(file_path, 'a+') as file:
    #         my_dates = [line.strip() for line in file.readlines()]
            
    #         if my_own_date in my_dates:
    #             print("This type of date already exists!")
    #             ask_again()
    #         else:
    #             file.write(my_own_date + '\n')
                
    #             # Go back to the beginning of the file to read its content
    #             file.seek(0)
    #             file_content = file.read()
                
    #     return file_content
                
        
def get_new_file():
    final_file = add_my_dates()
    return final_file

