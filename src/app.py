'''
Track a groups drink intake using a simple terminal interface. Output
the information into a .csv file for easy graphing and analysis.

Author: Greg Heiman
Date Created: 2022-05-30
License: MIT
'''
__author__ = "Greg Heiman"
__license__ = "MIT"
__version__ = "1.0"

import datetime
import pytz
import csv
import os

class Entry:
    '''
    Class representing an entry in the .csv file.

    :param name: str the name of the person in the entry.
    :param time: datetime the time of the entry.
    :param alc_percentage: float the percentage of the alcohol in the entry.
    :param alc_volume: float the volume of the alcohol in the entry.
    :param comments: str any comments for the entry (such as drink type).
    '''
    def __init__(self, name:str, time:datetime, alc_percentage:float,
                 alc_volume:float, comments:str):
        self.name = name
        self.time = time
        self.alc_percentage = alc_percentage
        self.alc_volume = alc_volume
        self.comments = comments

    def __str__(self):
        return('[name:' + self.name + ' time:' + str(self.time) +
               ' alc_percentage:' + str(self.alc_percentage) +
               ' alc_volume:' + str(self.alc_volume) + ' comments' +
               self.comments)

    def asdict(self):
        return {
            'Name': self.name,
            'Time': self.time,
            'Percentage': self.alc_percentage,
            'Volume': self.alc_volume,
            'Comments': self.comments
        }

def get_users_names() -> list:
    '''
    Create list of user's names that are tracking their drinks.

    :returns: a list of all of the user's names.
    '''
    names: list = []

    while True:
        print("How many users?")
        num_str = input()
        try:
            num = int(num_str)
            break
        except ValueError:
            print("Invalid input type within input: ", num_str)
            continue

    for x in range(num):
        print("What is player {}'s name?".format(x+1))
        name = input()
        names.append(name)

    print("The following are the input players:")
    for name in names:
        print(name)
    return names

def game_get_name(players_names: list) -> str:
    '''
    Get the user's name during the actual playing of the game.

    :param players_names: a list of all of the valid players names.
    :returns: the input user's name.
    '''
    while True:
        print("What is your name?")
        name = input()
        if name not in players_names:
            print("Invalid input. Input a valid player name.")
            print("The valid player names are:")
            for name in players_names:
                print(name)
            print("\n")
            continue
        else:
            break
    return name

def game_get_alc_percentage() -> float:
    '''
    Get the alcohol percentage of the current drink.

    :returns: the alcohol percentage as a float decimal (15% -> 0.15).
    '''
    while True:
        print("What is the alcohol percentage of your drink? (as decimal)")
        percentage_str = input()
        try:
            percentage = float(percentage_str)
            if percentage >= 1:
                print("Invalid input. Please enter in the alcohol percentage as a decimal.\n")
                continue
            else:
                break
        except ValueError:
            print("Invalid input type within input: ", percentage_str)
    return percentage

def game_get_alc_volume() -> float:
    '''
    Get the volume of the current drink.

    :returns: the volume of the drink as a float.
    '''
    while True:
        print("What is the volume of your drink (in mL)")
        volume_str = input()
        try:
            volume = float(volume_str)
            break
        except ValueError:
            print("Invalid input type within input: ", volume_str)
            continue
    return volume

def game_get_comments() -> str:
    '''
    Get any comments about the drink from the user.

    :returns: the comments the user input.
    '''
    print("Comments on your drink (type of drink, etc.)")
    comments = input()
    return comments

def game(players_names: list) -> None:
    '''
    Repeatedly ask the user for valid entries into the .csv file.
    To stop the game simply Ctrl-C to interrupt the terminal.

    :param players_names: list a list of all of the players names.
    '''
    filename = 'data_' + str(datetime.date.today()) + '.csv'
    fieldnames = [ 'Name', 'Time', 'Percentage', 'Volume', 'Comments']
    f = open(filename, 'a+', newline='')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    if not os.path.isfile(filename):
        writer.writeheader()

    print("\nThe game has started!")
    while True:
        # Retrieve all the info nessacary to create an entry into the .csv file
        name = game_get_name(players_names)
        percentage = game_get_alc_percentage()
        volume = game_get_alc_volume()
        comments = game_get_comments()

        print("\nHere is what you entered\nName: {}\nPercentage: {}\nVolume: {}\nComments: {}\n"
              .format(name, percentage, volume, comments))

        entry = Entry(name, datetime.datetime.now(pytz.timezone('US/Central')),
                      percentage, volume, comments)

        writer.writerow(entry.asdict())

    f.close()

def main():
    players = get_users_names()
    game(players)

if __name__ == "__main__":
    main()
