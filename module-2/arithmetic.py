"""This module demonstrations arithmetic operators in Python."""

__author__ = "Damien Altenburg"
__version__ = "1.1.2025"

age = 25

print(1 + 1)
print(6 - 2)
print(10 % 2)
print(2 ** 3)

# Variables as operands
print(age + 1)
print(age - 4)

# Store result of arithmetic
age = age + 1
friend_age = age - 4

print(f"age: {age}")

# Shortcut operators
age += 1

print(age)

age -= 1
#age = age - 1

print(age)

# Order of precedence
result = ((10 + 5) * 2) / 3 - 1
print(result)
