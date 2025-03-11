"""A script to demonstrate variable scope.

Example: 
    $ python variable_scope.py
"""

__version__ = "1.11.2024"
__author__ = "Damien Altenburg"

def to_binary(decimal_number: int) -> str:
    """Returns a string containing the binary equivalent to the
    specified decimal number.
    
    Args:
        decimal_number: The decimal number to convert.
        
    Returns:
        str: A string containing the binary equivalent to the
            specified decimal number.

    Example:
        >>> to_binary(147)
        "10010011"
    """
    
    binary_number = ""

    while decimal_number > 0:
        # The binary digit is the remainder of dividing by 2
        binary_digit = decimal_number % 2

        # Update the number to the the quotient
        decimal_number = int(decimal_number / 2)

        # Add the digit to the beginning of the string
        binary_number = str(binary_digit) + binary_number

    return binary_number

print(to_binary(147))
