"""This module contains a program that counts the number of times a
value entered by the user can be square rooted.
"""

from math import sqrt

__author__ = "Damien Altenburg"
__version__ = "1.2.2025"

count = 0
starting_number = 0
MINIMUM_STARTING_NUMBER = 20

while starting_number <= MINIMUM_STARTING_NUMBER:
    try:
        starting_number = input("Enter a starting number greater than"
                                f" {MINIMUM_STARTING_NUMBER}: ")
        starting_number = int(starting_number)
    except ValueError:
        print("Please enter a number.")
        starting_number = 0

square_root = starting_number

while square_root >= 1.01:
    # Calculate the square root
    square_root = sqrt(square_root)

    count += 1

print(f"The number of square roots was {count}.")
