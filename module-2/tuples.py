"""This module demonstrations the tuple collection in Python."""

__author__ = "Damien Altenburg"
__version__ = "1.1.2025"

# Define variable as a tuple
# Standard to wrap tuple in parentheses
rrc_programs = ("BIT", "DSML", "FSWD", "IS", "IBIT", "ITOps", "NST")

print(rrc_programs)

# Define tuple with one element
courses = ("SDF", )

# Access tuple element
program = rrc_programs[0]

print(program)

# Use tuple to create another tuple
updated_programs = rrc_programs + ("ABC", )

print(updated_programs)

# Functions that have tuple arguments
print(len(rrc_programs))

print(sorted(rrc_programs))

# Convert a list to a tuple
temperatures = [23.4, 36.1, 24.5, 20.8, 15.6]
temperatures = tuple(temperatures)

# Numeric tuple functions
print(max(temperatures))
print(min(temperatures))
print(sum(temperatures))
print(sorted(temperatures))

# Other methods
# Returns the number of occurrences of the argument
# count(value)

# Returns the index of the first occurrence
# index(value) 
