import sys
import random

# Ask the user to tell us how many die they wish to roll.
number_of_die = input("Enter the number of die you'd like to roll: ")
# Make sure that any input is an int.
number_of_die = int(number_of_die)
# Check the user input for a reasonable value.
if number_of_die < 1:
    print('You must enter a number greater than 1.')
    sys.exit(2)

# Initialize a list of possible faces.
die_faces = [4, 6, 8, 10, 12, 20]
# Ask the user how many sides they want for the die that are rolled.
sides_of_die = input("How many sides for each die? [{}]: ".format(', '.join(str(item) for item in die_faces)))
# Make sure that any input is an int.
sides_of_die = int(sides_of_die)
# Check that the number provided was in our list of possible options.
if sides_of_die not in die_faces:
    print('You must choose one of the options listed.')
    sys.exit(2)

# Roll Die.
print("Rolling {} die with {} faces each.".format(number_of_die, sides_of_die))

# Create a dictionary that will store the rolls for each die.
rolls = {}
# Initialize a variable that will store the cumulative rolls.
roll_total = 0

# For each die indicated, make a roll.
for d in range(1, number_of_die + 1):
    # Select a number within the range possible for the number of sides.
    rolls[d] = random.randint(1, sides_of_die)
    # Add this new roll to the roll total.
    roll_total = roll_total + rolls[d]

# Output die results.
for d in rolls:
    print("Die {} rolled a {}.".format(d, rolls[d]))
print("The roll total is {}.".format(roll_total))
