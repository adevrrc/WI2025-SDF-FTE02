"""A script to demonstrate the basics of functions.

Example: 
    $ python functions_basics.py
"""

__version__ = "1.11.2024"
__author__ = "Damien Altenburg"

# Syntax: def id([params]) -> type

def print_greeting(first_name: str="world", last_name: str="") -> None:
    print(f"Hello {first_name} {last_name}!")

print_greeting()
print_greeting("beautiful")
print_greeting(last_name="cup")

def format_greeting(first_name: str, last_name: str, salutation="Hello", title="Mr.") -> str:
    return f"{salutation}, {title} {first_name} {last_name}"

print(format_greeting("Damien", "Altenburg"))
print(format_greeting("Damien", "Altenburg", "Bonjour"))
print(format_greeting("Jane", "Doe", "Bonjour", "Mrs."))
print(format_greeting("Jane", "Doe", title="Dr."))
