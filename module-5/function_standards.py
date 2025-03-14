"""A script to demonstrate function standards and raising exceptions.

Example: 
    $ python function_standards.py

TODO:
    - format_greeting: Add parameter validation for salutation and 
    title.
"""

__version__ = "1.11.2024"
__author__ = "Damien Altenburg"

def format_greeting(first_name: str, last_name: str, salutation="Hello", title="Mr.") -> str:
    """Returns a formatted greeting with the specified names.
    
    Args:
        first_name (str): The person's first name.
        last_name (str): The person's last name.
        salutation (str): The beginning phrase of the greeting. The
        default is "Hello".
        title (str): The person's title. The default is "Mr.".

    Returns:
        str: A formatted greeting with the specified names.

    Raises:
        TypeError: Raised when the first_name or last_name is not a
            str type.
        ValueError: Raised when last_name has no non-whitespace 
            characters.
    
    Example:
        >>> format_greeting("Damien", "Altenburg")
        Hello, Mr. Damien Altenburg
    """

    first_name = first_name.strip()

    if not isinstance(first_name, str):
        raise TypeError("First name must be a str type.")
    
    if not isinstance(last_name, str):
        raise TypeError("Last name must be a str type.")

    last_name = last_name.strip()

    if len(last_name) == 0:
        raise ValueError("Last name must contain a minimum of one non-whitespace character.")

    full_name = f"{first_name} {last_name}".strip()

    return f"{salutation}, {title} {full_name}"

def main() -> None:
    """The main function of the program."""

    greeting = format_greeting("Damien", "Altenburg")
    print(greeting)

if __name__ == "__main__":
    main()
