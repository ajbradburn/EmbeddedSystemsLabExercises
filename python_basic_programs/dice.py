#!/usr/bin/python3

import sys
import getopt
import random


def main(argv):
    number_of_die = None

    number_of_die = input("Enter the number of die you'd like to roll: ")
    
    # Make sure that any input is an int.
    number_of_die = int(number_of_die)

    # Check the user input for a reasonable value.
    if number_of_die < 1:
        print('You must enter a number greater than 1.')
        sys.exit(2)

    die_faces = [4, 6, 8, 10, 12, 20]

    sides_of_die = input("How many sides for each die? [{}]: ".format(', '.join(str(item) for item in die_faces)))
    sides_of_die = int(sides_of_die)
    if sides_of_die not in die_faces:
        print('You must choose one of the options listed.')
        sys.exit(2)


    # Roll Die.
    print("Rolling {} die with {} faces each.".format(number_of_die, sides_of_die))

    rolls = {}
    roll_total = 0

    for d in range(1, number_of_die + 1):
        rolls[d] = random.randint(1, sides_of_die)
        str_roll = str(rolls[d])
        roll_total = roll_total + rolls[d]
    str_roll_total = str(roll_total)

    # Output die results.
    for d in rolls:
        print("Die {} rolled a {}.".format(d, rolls[d]))

if __name__ == "__main__":
    main(sys.argv[1:])
