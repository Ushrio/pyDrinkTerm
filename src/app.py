import datetime
import pytz
import csv
import os

def get_users_names() -> list:
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

def game(players_names: list) -> None:
    filename = 'data_' + str(datetime.date.today()) + '.csv'
    fieldnames = [ 'Name', 'Time (US/Central)', 'Percentage', 'Volume', 'Comments']
    f = open(filename, 'a+', newline='')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    if not os.path.isfile(filename):
        writer.writeheader()

    print("\nThe game has started!")
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

        while True:
            print("What is the alchol percentage of your drink? (as decimal)")
            percentage_str = input()
            try:
                percentage = float(percentage_str)
                if percentage >= 1:
                    print("Invalid input. Please enter in the alchol percentage as a decimal.\n")
                    continue;
                else:
                    break;
            except ValueError:
                print("Invalid input type within input: ", percentage_str)

        while True:
            print("What is the volume of your drink (in mL)")
            volume_str = input()
            try:
                volume = float(volume_str)
                break;
            except ValueError:
                print("Invalid input type within input: ", volume_str)
                continue;

        print("Comments on your drink (type of drink, etc.)")
        comments = input()

        print("\nHere is what you entered\nName: {}\nPercentage: {}\nVolume: {}\nComments: {}\n"
              .format(name, percentage, volume, comments))

        data_dict = {
            "Name": name,
            "Time (US/Central)": datetime.datetime.now(pytz.timezone('US/Central')),
            "Percentage": percentage,
            "Volume": volume,
            "Comments": comments
        }

        writer.writerow(data_dict)

    f.close()

def main():
    players = get_users_names()
    game(players)

if __name__ == "__main__":
    main();
