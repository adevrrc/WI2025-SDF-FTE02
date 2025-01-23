"""This module demonstrates data types for module 2."""

__author__ = "Damien Altenburg"
__version__ = "1.1.2025"

# Syntax: Declaring a variable
# identifier = value
name = "Damien Altenburg"
age = 25
annual_income = 67890.45
is_employed = True

# This identifier is not well named and is only for demonstration sake
value_type = type(25)
print(value_type)

print(type(25))

# Constants
DAYS_IN_A_WEEK = 7
SALES_TAX = .05

# BAD!!!
# DAYS_IN_A_WEEK = 99

print(DAYS_IN_A_WEEK)

# Getting input
#last_name = input("What is your last name? ")

#print(last_name)

#age = input("Please enter your age: ")

#print(age)

print(type(age))

# My name is [name] and I am [age] years old.
print("My name is", name, "and I am", age, "years old.")

print(f"My name is {name} and I am {age} years old.")

PI = 3.1415

# Value of Pi: #.##
print(f"Value of Pi: {PI:.2f}")

print(PI)

annual_income = 20000000

# $###,###.#0
print(f"Damien's annual salary is ${annual_income:,.2f}.")
