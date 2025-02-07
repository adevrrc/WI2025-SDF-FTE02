"""A script to demonstrate boolean expressions.

Example: 
    $ python boolean_expressions.py
"""

__author__ = "Damien Altenburg"
__version__ = "1.0.0"

age: int = 25
name: str = "Damien"

# Boolean literals
print(True)
print(False)

# Boolean variables
is_damien_cool: bool = True
print(is_damien_cool)

# Boolean Functions
print(name.isalpha())
print(name.isdigit())

# Comparison Operators (Boolean Operations)
print(age == 25)
print(age == 35)
print(age != 35)
print(age < 14)
print(age <= 25)
print(age > 25)
print(age >= 25)
