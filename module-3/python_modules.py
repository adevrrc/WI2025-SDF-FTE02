"""A script to demonstrate python modules; math and random.

Example: 
    $ python_modules.py
"""

from math import sqrt, pow, pi, ceil, floor
from random import random, randint, uniform, choice, shuffle

__author__ = "your_name_here"
__version__ = "1.0.0"

teams = ["jets", "flames", "oilers", "canucks", "senators", "canadians"]

print(sqrt(9))

print(pow(3, 5))

print(pi)

# roll of a die
for count in range(5):
    print(randint(1, 6))

# Math Functions
# Returns square root of the specified value
print(sqrt(64))

# Rounds up to the nearest integer
print(ceil(1.4))

# Rounds down to the nearest integer
print(floor(1.4))

radius: float = 3.4
print(f"Area: {pi * pow(radius, 2):.2f}")

# random Module Functions
# Random value between 0 and 1
random_number = random()
print(random_number)

# Random integer
random_number = randint(3, 9)
print(random_number)

# Random float value
random_number = uniform(3.0, 9.0)
print(random_number)

# Return a random value from the specified collection
random_team = choice(teams)
print(random_team)

# Reorder element values in a random order
shuffle(teams)
print(teams)
