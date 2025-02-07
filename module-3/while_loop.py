"""A script to demonstrate the while loop.

Example: 
    $ python while_loop.py
"""

__author__ = "your_name_here"
__version__ = "1.0.0"

successfully_confirmed: bool = False

# Syntax
# while boolean_expression:
#     statement(s)
while not successfully_confirmed:
    password = input("Enter your new password: ")

    password_confirmation = input("Confirm: ")

    successfully_confirmed = password == password_confirmation

    confirmation_message = \
        ("Confirmation was not successful. Please try again."
         if not successfully_confirmed else "Password updated.")

    print(confirmation_message)
