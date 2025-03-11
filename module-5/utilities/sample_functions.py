"""A module that includes sample functions to demonstrate unit 
testing.
"""

__version__ = "1.11.2024"
__author__ = "Damien Altenburg"

def format_greeting(first_name: str, last_name: str, 
                    salutation="Hello", title="Mr.") -> str:
    """Returns a formatted greeting with the specified name.

    Args:
        first_name (str): The person's first name.
        last_name (str): The person's last name.
        salutation (str): Optional, The phrase used for the salutation. 
                          Default: "Hello"
        title (str): Optional, The title used to address the person. 
                     Default: "Mr."

    Returns:
        str: A formatted greeting with the specified name.

    Raises:
        TypeError: Raise when any parameter is not a str type.
        ValueError: Raised when last_name, salutation, or title does not
                    contain non-whitespace characters.
    """

    if not isinstance(first_name, str):
        raise TypeError("First name must be a str.")

    if not isinstance(last_name, str):
        raise TypeError("Last name must be a str.")

    first_name = first_name.strip()
    last_name = last_name.strip()

    if last_name.strip() == "":
        raise ValueError("Last name must contain non-whitespace characters.")
    
    if not isinstance(salutation, str):
        raise TypeError("Salutation must be a str.")

    salutation = salutation.strip()

    if salutation == "":
        raise ValueError("Salutation must contain non-whitespace characters.")
    
    if not isinstance(title, str):
        raise TypeError("Title must be a str.")

    title = title.strip()

    if title == "":
        raise ValueError("Title must contain non-whitespace characters.")
    
    full_name = f"{first_name} {last_name}".strip()

    return f"{salutation}, {title} {full_name}"

def get_whole_number(prompt: str) -> int:
    """Returns a whole number entered via the console.

    Args:
        prompt: The text to display for the prompt.

    Returns:
        int: A whole number entered via the console.

    Raises:
        TypeError: Raised when the prompt is not a str type.
        ValueError: Raised when the console input is not a whole number.
    """
    
    if not isinstance(prompt, str):
        raise TypeError("Prompt must be a str.")
    
    whole_number = input(f"{prompt}: ")

    try:
        whole_number = int(whole_number)
    except ValueError as exception:
        raise ValueError("Input must be a whole number.") from exception
    
    return whole_number
