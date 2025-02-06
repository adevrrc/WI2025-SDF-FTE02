"""A script to demonstrate selections.

Example: 
    $ python selections.py
"""

__author__ = "Damien Altenburg"
__version__ = "1.0.0"

age = 25
name = "Damien"

if age == 25:
    print("You are 25 years old.")

print("This statement is not part of the block.")

if age > 40:
    print("You are old.")
else:
    print("You are young.")

age = 40

if age == 30:
    print("You are 30.")
elif age == 40:
    print("You are 40.")

if age == 30:
    print("You are 30.")

if age == 40:
    print("You are 40.")

if age >= 10:
    print("The age is greater or equal to 10.")
elif age != 5:
    print("The age is less than 10 and not 5.")
else:
    print("The age is 5.")

if age >= 25 and name == "Damien":
    print("You are super cool!")

if age > 50 or name == "Damien":
    print("You are still pretty cool.")

name = "Damien"

if not name.isalpha():
    print("Error")

# Conditional Operator
# Syntax
# operand if operand else operand
# value if boolean_expression else value
age_description = "old" if age > 25 else "young"

print(f"You're {age_description}")

# Works in python, but not most other languages
print("True") if age == 25 else print("False")

names = ["kenny", "jon", "max", "chris", "saraya"]
name = "jason"

# Membership Operators
# Syntax
# value in collection_reference
# value not in collection_reference
negator = "" if name in names else "not "

print(f"{name.title()} is {negator}in the list.")
