"""A script to demonstrate list comprehensions.

Example: 
    $ list_comprehensions.py
"""

__author__ = "your_name_here"
__version__ = "1.0.0"

names = ["kenny", "eric", "kyle", "stan", "butters", "clyde"]

squares = [number ** 2 for number in range(1, 11)]
print(squares)

odd_names = [name.title() for name in names if len(name) % 2 != 0]
print(odd_names)
