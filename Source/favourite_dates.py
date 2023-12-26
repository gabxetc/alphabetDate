import date_sorter as chron_ops

'''
    The following functions retrieve the list[str]
    from the respective functions in the date_sorter modules
    and stores the data in variables to be used in this code    
'''
app_dates = chron_ops.sort_app_dates
my_dates = chron_ops.sort_my_dates
all_dates = chron_ops.sort_all_dates

# These variables are initializers of valid answers from the input 
yes = 'yes'.capitalize()
no = 'no'.capitalize()

remain = " will remain in your favourites"
not_added = " will not be added to your favourites"
'''
    The following function manages the add date to favourite
    of the built in dates of the app.
    
    add_app_faves, add_my_faves, add_all_faves functions:
    - the list of potential favourite dates in initalised and the state of favourite is set to false
    - we then loop through the list of app_dates
    - a condition checks if the input from the make_fav_action function is yes 
        - if yes:
            # favourite is set to True
            # the date at the current iteration is appended to the app_faves list
        - if no:
            # user receives a print statment informing them of the action
    - the list of favourites is then returned
'''

def add_app_faves():
    app_faves = []
    favourite = False

    for date in app_dates:
        if make_fav_action(date) == yes:
            favourite = True
            date.append(app_faves)
        else:
            print(date + not_added)
    return app_faves

'''
    The following function manages the remove date from favourite
    of the built in dates of the app.
    
    remove_app_faves, remove_my_faves, remove_all_faves functions:
    - the list of favourite dates is acces from the parameter app_faves
    - for this function the favourite tag is set to true because if the date
    is in the fav list then it is true that it is a favourite
    - we then loop through the list of app_faves (list of current favourites)
    - a condition checks if the input from the remove_fav_action function is yes 
        - if yes:
            # favourite is set to False
            # the date at the current iteration is removed from the app_faves list
        - if no:
            # user receives a print statment informing them of the action
    - the list of favourites is then returned
'''

def remove_app_faves(app_faves):
    new_app_faves = []
    favourite = True

    for date in app_faves:
        if remove_app_faves(date) == yes:
            favourite = False
            app_faves.remove(date)
        else:
            new_app_faves.append(date)
            print(date + remain)
    return new_app_faves

# The next two functions handle the removing and adding faves to the users homemade dates
def add_my_faves():
    my_faves = []
    favourite = False

    for date in my_dates:
        if make_fav_action(date) == yes:
            favourite = True
            date.append(my_faves)
        else:
            print(date + not_added)
    return my_faves

def remove_my_faves(my_faves):
    new_my_faves = []
    favourite = True

    for date in my_faves:
        if remove_app_faves(date) == yes:
            favourite = False
            my_faves.remove(date)
        else:
            new_my_faves.append(date)
            print(date + remain)
    return new_my_faves

# The next two functions handle the removing and adding faves to acombo of built in dates and homemade dates
def add_all_faves():
    all_faves = []
    favourite = False

    for date in all_dates:
        if make_fav_action(date) == yes:
            favourite = True
            date.append(all_faves)
        else:
            print(date + not_added)
    return all_faves

def remove_all_faves(all_faves):
    new_all_faves = []
    favourite = True

    for date in all_faves:
        if remove_app_faves(date) == yes:
            favourite = False
            all_faves.remove(date)
        else:
            new_all_faves.append(date)
            print(date + remain)
    return new_all_faves

'''
    The following functions handle the action of the user via inputs and returns a yes or no 
    value which was initialised at the top of this script.
    - make_fav_action: checks if the user would like to add the current date to the favourites list
    - remove_fav_action: checks if the user would like to remove the current date from the favourite list
'''
def make_fav_action(date):
    add_favourite = input("Would you like to add "+ date + "to your favourites list?\n")
    return yes or no

def remove_fav_action(date):
    remove_favourite = input("Would you like to remove "+ date + "from your favourite list?\n")
    return yes or no