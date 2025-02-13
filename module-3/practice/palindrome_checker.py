"""A program to check if a phrase is a palindrome.

Practice Problem 38
"""

__author__ = "Damien Altenburg"
__version__ = "1.0.0"

phrase = ""

while phrase == "":
    phrase = input("Enter a phrase> ")
    
    phrase = phrase.strip()

# Convert to lowercase
phrase = phrase.lower()

# Reverse the characters of the phrase
phrase_reversed = phrase[::-1]

negator = ""

if phrase != phrase_reversed:
    negator = " not"

# Print palindrome result
print(f"The phrase is{negator} a palindrome.")
