"""A program to demonstrate handling file related exceptions.

Example: 
    $ python working_with_files.py
"""

__author__ = "Damien Altenburg"
__version__ = "1.0.0"

from os import path

SCRIPT_DIRECTORY = path.dirname(path.realpath(__file__))
FILENAME = "data.txt"
FILE_PATH = f"{SCRIPT_DIRECTORY}/{FILENAME}"

try:
    with open(FILE_PATH) as data_file:
        for record in data_file:
            print(record)
except FileNotFoundError:
    print(f"{FILENAME} not found.")

input("Press <enter> to continue...")
