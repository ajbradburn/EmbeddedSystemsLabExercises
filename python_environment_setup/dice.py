# Import the random library.
import random

# Ask the user for the number of die they want to roll.
number_of_die = input("Enter the number of die you'd like to roll: ")
number_of_die = int(number_of_die)

# Initialize some variables that will store our roll data.
rolls = {}
roll_total = 0

# Using a loop, roll each die, and save the roll results to the variables.
for d in range(1, number_of_die + 1):
    rolls[d] = random.randint(1, 6)
    roll_total = roll_total + rolls[d]

# Output die results.
# Output individual results.
for d in rolls:
    print("Die {} rolled a {}.".format(d, rolls[d]))
# Output the combined results.
print("The roll total was: {}.".format(roll_total))
