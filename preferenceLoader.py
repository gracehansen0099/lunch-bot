from Utilities import dataManipulation as util

preferences = {}


# simply open a file, get the data and return a dictionary
def get_preferences():
    with open('preferences.txt', 'r') as f:
        for line in f:
            line_array = util.remove_linefeed(line).split("=")
            if '=' in line:
                preferences[line_array[0]] = line_array[1]

    return preferences
