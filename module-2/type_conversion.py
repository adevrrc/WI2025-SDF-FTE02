"""This module demonstrates type conversion for module 2."""

__author__ = "Damien Altenburg"
__version__ = "1.1.2025"

age = input("Enter your age: ")

print(age)

print(type(age))

age = int(age)

print(type(age))

print(age + 5)

print(int(7.666666))

# int()
# float()
# bool()
# str()

print(type(str(45)))
