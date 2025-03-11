"""A script to demonstrate function standards and raising exceptions.

Example: 
    $ python function_standards.py
"""

__version__ = "1.11.2024"
__author__ = "Damien Altenburg"

def format_greeting(first_name: str, last_name: str, salutation="Hello", title="Mr.") -> str:
    """Returns a formatted greeting with the specified names.
    
    Args:
        first_name (str): The person's first name.
        last_name (str): The person's last name.
        ...
        
    Returns:
        str: A formatted greeting with the specified names.
    
    Example:
        >>> format_greeting("Damien", "Altenburg")
        Hello, Mr. Damien Altenburg
    """

    full_name = f"{first_name} {last_name}".strip()

    return f"{salutation}, {title} {full_name}"
