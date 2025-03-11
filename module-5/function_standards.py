"""A script to demonstrate function standards and raising exceptions.

Example: 
    $ python function_standards.py
"""

__version__ = "1.11.2024"
__author__ = "Damien Altenburg"

def format_greeting(first_name: str, last_name: str, salutation="Hello", title="Mr.") -> str:
    full_name = f"{first_name} {last_name}".strip()

    return f"{salutation}, {title} {full_name}"
