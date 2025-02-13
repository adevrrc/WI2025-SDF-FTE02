"""A script to demonstrate file output.

Example: 
    python file_output.py
"""

__author__ = "your_name_here"
__version__ = "1.0.0"

FILE_PATH = "grades.txt"

grades = [85, 34, 67, 78, 89, 99, 21, 45, 64, 88, 92]

# Write to a file then close the file
with open(FILE_PATH, "w") as file:
    file.write(str(grades[0]))

# Write to file using List
with open(FILE_PATH, "w") as file:
    for grade in grades:
        # Writes without a line ending
        #file.write(str(grade))

        # Write with line ending
        file.write(f"{grade}\n")

# Append to a file
with open(FILE_PATH, "a") as file:
    for grade in [66, 77, 88]:
        file.write(f"{grade}\n")
