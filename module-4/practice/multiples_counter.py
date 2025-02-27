"""This module contains a program that counts the number of numbers
evenly divisible by a specific number.
"""

DIVISOR = 7
LOW_RANGE = 33
HIGH_RANGE = 500

count = 0

for current_number in range(LOW_RANGE, HIGH_RANGE + 1):
    remainder = current_number % DIVISOR

    if remainder == 0:
        count += 1

print(f"The number of numbers divisible by {DIVISOR} between "
      f"{LOW_RANGE} and {HIGH_RANGE} is {count}.")
