import random

number_of_die = input("Enter the number of die you'd like to roll: ")
number_of_die = int(number_of_die)

rolls = {}
roll_total = 0

for d in range(1, number_of_die + 1):
    rolls[d] = random.randint(1, 6)
    roll_total = roll_total + rolls[d]

# Output die results.
for d in rolls:
    print("Die {} rolled a {}.".format(d, rolls[d]))
print("The roll total was: {}.".format(roll_total))
