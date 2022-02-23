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
    file_name = 'die_stats.json'
    if(exists(file_name)):
        file_handle = open(file_name, 'r')
        stats = json.load(file_handle)
        file_handle.close()
        file_handle = open(file_name, 'w')
    else:
        file_handle = open(file_name, 'w')
        stats = {
                    '1':{
                        'run_count': 0,
                        '1':{"rolls":0, "percentage":16},
                        '2':{"rolls":0, "percentage":16},
                        '3':{"rolls":0, "percentage":16},
                        '4':{"rolls":0, "percentage":16},
                        '5':{"rolls":0, "percentage":16},
                        '6':{"rolls":0, "percentage":16},
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
    str_number_of_die = str(number_of_die)

    # Check the user input for a reasonable value.
    if number_of_die < 1:
        print('You must enter a number greater than 1.')
        sys.exit(2)

    # Increment our run counter.

    if not str_number_of_die in stats:
        die_combinations = []
        calc_combinations(die_combinations, number_of_die, 0)
        roll_values = (list(set(die_combinations)))

        stats[str_number_of_die] = {}
        stats[str_number_of_die]['run_count'] = 0
        for rv in roll_values:
            roll_possibilities = len(die_combinations)
            roll_frequency = die_combinations.count(rv)
            roll_percentage = int(roll_frequency / roll_possibilities * 100)
            stats[str_number_of_die][str(rv)] = {"rolls":0, "percentage":roll_percentage}

    # Roll Die.
    print("Rolling {} die.".format(number_of_die))

    rolls = {}
    roll_total = 0

    for d in range(1, number_of_die + 1):
        rolls[d] = random.randint(1, 6)
        str_roll = str(rolls[d])
        stats['1'][str_roll]['rolls'] = stats['1'][str_roll]['rolls'] + 1
        stats['1']['run_count'] = stats['1']['run_count'] + 1
        roll_total = roll_total + rolls[d]
    str_roll_total = str(roll_total)
    stats[str_number_of_die][str_roll_total]['rolls'] = stats[str_number_of_die][str_roll_total]['rolls'] + 1
    stats[str_number_of_die]['run_count'] = stats[str_number_of_die]['run_count'] + 1

    # Output die results.
    for d in rolls:
        print("Die {} rolled a {}.".format(d, rolls[d]))

    str_actual_roll_percent = int((stats[str_number_of_die][str_roll_total]['rolls'] / stats[str_number_of_die]['run_count']) * 100)
    print("Out of the {} times that this program has been run {} has been rolled {} times, a percentage of {}. A roll of {} should occur {}% of the time.".format(stats[str_number_of_die]['run_count'], str_roll_total, stats[str_number_of_die][str_roll_total]['rolls'], str_actual_roll_percent, str_roll_total, stats[str_number_of_die][str_roll_total]['percentage']))

# Output die statistics.

# Save config and statistics to a file.
    stats_string = json.dumps(stats, indent=4)
    file_handle.truncate()
    file_handle.write(stats_string)

if __name__ == "__main__":
    main(sys.argv[1:])
