'''The following fuctions access the txt file of built in dates 
and consumer added dates, sorts them alphabetically and returns
a list of strings(dates)'''

''' The first function does the following:
    - opens the txt file in read mode and the obj is assigned to the var file
    - all lines from the file are read, stored in a list named app_dates
    - this list is then sorted in ascending order
    - the file is then closed
    - the func returns a sorted list of app dates
'''
#sorted list of built in dates
def sort_app_dates():
    file = open("app_dates.txt", 'r')
    app_dates = file.readlines()
    app_dates.sort()
    file.close()    
    return app_dates

#sorted list of consumer added dates
def sort_my_dates():
    file = open("my_dates.txt", 'r')
    my_dates = file.readlines()
    my_dates.sort() #sort returns None
    file.close()    
    return my_dates

#sorted list of combination of both built in and consumer added dates
def sort_all_dates():
    all_dates = sorted(sort_my_dates+sort_app_dates)
    return all_dates