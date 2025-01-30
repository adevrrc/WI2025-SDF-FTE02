"""This module demonstrates string concatenation for module 2."""

__author__ = "Damien Altenburg"
__version__ = "1.1.2025"

first_name = "Damien"
last_name = "Altenburg"

# String concatenation
# + operator does string concatenation when both operands are str type.
full_name = first_name + last_name

print(full_name)

# Error: the + operator is attempting to do addition, because one of
# the operands is a numeric type. This will not do string concatenation.
# Uncomment the line below and run to see the error.
#print(first_name + 25)

# This is how you would have to do the previous statement.
# Uncomment the line below and run to see the result.
#print(first_name + str(25))

age = 25
color = "red"

print(f"Hello my name is {first_name} {last_name}. I am {age} years old. "
      f"My favorite color is {color}.")
