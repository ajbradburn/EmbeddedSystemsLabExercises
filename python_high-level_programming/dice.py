#!/usr/bin/python

import sys
import getopt
from os.path import exists
import json
import random

def calc_combinations(roll_totals, remaining_die, cumulative_rolls):
    for r in range(1, 6 + 1):
        if remaining_die > 1:
            die_left = remaining_die - 1
            calc_combinations(roll_totals, die_left, cumulative_rolls + r)
        else:
            roll_totals.append(cumulative_rolls + r)


def main(argv):
# Initialize stats.
# Check if configuration file exists.
    file_name = 'die_stiats.json'
    if(exists(file_name)):
        file_handle = fopen(file_name)
        stats = json.load(file_handle)
    else:
        stats = {
                    1:{
                        1:{"rolls":0, "probability":0.16},
                        2:{"rolls":0, "probability":0.16},
                        3:{"rolls":0, "probability":0.16},
                        4:{"rolls":0, "probability":0.16},
                        5:{"rolls":0, "probability":0.16},
                        6:{"rolls":0, "probability":0.16},
                    }
                }

# Look for command line input of N die.
    help_string = 'output_with_format.py -i <file_name>'
    try:
        opts, args = getopt.getopt(argv, "hn:")
    except getopt.GetoptError:
        print(help_string)
        sys.exit(2)

    number_of_die = None

    for opt, arg in opts:
        if opt == '-h':
            print(help_string)
        elif opt in ("-n"):
            number_of_die = arg

# If NO, ask for user input of N Die.
    if number_of_die == None:
        number_of_die = input("Enter the number of die you'd like to roll:")
    
    # Make sure that any input is an int.
    number_of_die = int(number_of_die)

    if number_of_die < 1:
        print('You must enter a number greater than 1.')
        sys.exit(2)

    if not number_of_die in stats:
        die_combinations = []
        calc_combinations(die_combinations, number_of_die, 0)
# TODO
# Add the statistics changes to the stats dictionary.

# Roll Die.
    print("Rolling {} die.".format(number_of_die))

    rolls = {}
    roll_total = 0

    for d in range(1, number_of_die + 1):
        rolls[d] = random.randint(1, 6)
        stats[1][rolls[d]]['rolls'] = stats[1][rolls[d]]['rolls'] + 1
        roll_total = roll_total + rolls[d]

# Output die results.
    print(rolls)
    print(stats)

# Output die statistics.

# Save config and statistics to a file.

if __name__ == "__main__":
    main(sys.argv[1:])
