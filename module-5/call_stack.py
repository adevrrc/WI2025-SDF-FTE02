"""A script to demonstrate the call stack.

Example: 
    $ python call_stack.py
"""

__version__ = "1.11.2024"
__author__ = "Damien Altenburg"

def functionD() -> None:
    """The "D" function."""

    print("Start of function D - Added to stack")
    print("End of function D - Removed from call stack")

def functionC() -> None:
    """The "C" function."""
    
    print("Start of function C - Added to stack")
    functionD()
    print("End of function C - Removed from call stack")

def functionB() -> None:
    """The "B" function."""
    
    print("Start of function B - Added to stack")
    functionC()
    print("End of function B - Removed from call stack")

def functionA() -> None:
    """The "A" function."""
    
    print("Start of function A - Added to stack")
    functionB()
    print("End of function A - Removed from call stack")

print("Start of main - Add to call stack")
functionA()
print("End of main - Removed from call stack")
