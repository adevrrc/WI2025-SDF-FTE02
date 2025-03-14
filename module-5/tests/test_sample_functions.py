"""Defines the TestSampleFunctions class to demonstrate unit testing.

Test Cases

format_greeting()

1. first_name not a string - TypeError (First name must be a str.)
2. last_name not a string - TypeError (Last name must be a str.)
3. last_name blank string - ValueError (Last name must contain 
non-whitespace characters.)
4. salutation not a string - TypeError (Salutation must be a str.)
5. salutation blank string - ValueError (Salutation must contain 
non-whitespace characters.)
6. title not a string - TypeError (Title must be a str.)
7. title blank string - ValueError (Title must contain non-whitespace 
characters.)
8. first_name blank string - returns formatted without a first name
9. first_name not blank - returns formatted with a first name
10. greeting with a specific salutation and title - returns a formatted
greeting with all the specified arguments

get_whole_number()

1. prompt not a string - TypeError (Prompt must be a str.)
2. console input not a whole number - exception (Input was not a whole 
number.)
3. console input is a whole number - returns whole number

Examples: 
    $ python -m unittest tests/test_sample_functions.py
    $ clear; python -m unittest tests/test_sample_functions.py
"""

import unittest
from unittest.mock import patch
from utilities.sample_functions import format_greeting
from utilities.sample_functions import get_whole_number

__version__ = "1.11.2024"
__author__ = "Damien Altenburg"

class TestSampleFunctions(unittest.TestCase):
    """Unit tests for the function within the sample_functions module.
    """

    #### format_greeting(str, str, str, str) Tests

    def test_format_greeting_exception_first_name_not_a_string(self):
        """"""
        
        # Arrange
        first_name = 4
        last_name = "Altenburg"

        # Act
        with self.assertRaises(TypeError) as context:
            format_greeting(first_name, last_name)

        # Assert
        expected = "First name must be a str."

        # Get error message from the exception
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_format_greeting_last_name_not_a_string(self):
        # Arrange
        first_name = "Damien"
        last_name = 10

        # Act
        with self.assertRaises(TypeError) as context:
            format_greeting(first_name, last_name)

        # Assert
        expected = "Last name must be a str."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_format_greeting_last_name_blank_string(self):
        # Arrange
        first_name = "Damien"
        last_name = ""

        # Act
        with self.assertRaises(ValueError) as context:
            format_greeting(first_name, last_name)

        # Assert
        expected = "Last name must contain non-whitespace characters."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_format_greeting_salutation_not_a_str(self):
        # Arrange
        first_name = "Damien"
        last_name = "Altenburg"
        salutation = None

        # Act
        with self.assertRaises(TypeError) as context:
            format_greeting(first_name, last_name, salutation)

        # Assert
        expected = "Salutation must be a str."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_format_greeting_salutation_blank_str(self):
        # Arrange
        first_name = "Damien"
        last_name = "Altenburg"
        salutation = ""

        # Act
        with self.assertRaises(ValueError) as context:
            format_greeting(first_name, last_name, salutation)

        # Assert
        expected = "Salutation must contain non-whitespace characters."
        actual = str(context.exception)
        self.assertEqual(expected, actual)
        
    def test_format_greeting_title_not_a_str(self):
        # Arrange
        first_name = "Damien"
        last_name = "Altenburg"
        title = None

        # Act
        with self.assertRaises(TypeError) as context:
            format_greeting(first_name, last_name, title=title)

        # Assert
        expected = "Title must be a str."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_format_greeting_title_blank_str(self):
        # Arrange
        first_name = "Damien"
        last_name = "Altenburg"
        title = ""

        # Act
        with self.assertRaises(ValueError) as context:
            format_greeting(first_name, last_name, title=title)

        # Assert
        expected = "Title must contain non-whitespace characters."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_format_greeting_returns_a_formatted_greeting_without_a_first_name(self):
        # Arrange
        first_name = ""
        last_name = "Lee"

        # Act
        actual = format_greeting(first_name, last_name)

        # Assert
        expected = "Hello, Mr. Lee"
        self.assertEqual(expected, actual)

    def test_format_greeting_returns_a_formatted_greeting_with_a_first_name(self):
        # Arrange
        first_name = "Damien"
        last_name = "Lee"

        # Act
        actual = format_greeting(first_name, last_name)

        # Assert
        expected = "Hello, Mr. Damien Lee"
        self.assertEqual(expected, actual)

    def test_format_greeting_return_a_formatted_greeting_with_salutation_and_title(self):
        # Arrange
        first_name = "Damien"
        last_name = "Lee"
        salutation = "Bonjour"
        title = "Dr."

        # Act
        actual = format_greeting(first_name, last_name, salutation, title)

        # Assert
        expected = "Bonjour, Dr. Damien Lee"
        self.assertEqual(expected, actual)

    #### get_whole_number(str) Tests

    def test_get_whole_number_prompt_not_a_string(self):
        # Arrange
        prompt = None

        # Act
        with self.assertRaises(TypeError) as context:
            get_whole_number(prompt)

        # Assert
        expected = "Prompt must be a str."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_get_whole_number_input_not_a_whole_number(self):
        # Arrange
        prompt = "Enter a whole number"

        # Act
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["hello"]

            with self.assertRaises(ValueError) as context:
                get_whole_number(prompt)

        # Assert
        expected = "Input must be a whole number."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_get_whole_number_return_whole_number_entered_via_keyboard(self):
        # Arrange
        prompt = "Enter your age"

        # Act
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["23"]
            actual = get_whole_number(prompt)

        # Assert
        expected = 23
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
