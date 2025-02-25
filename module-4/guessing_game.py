"""A simple guessing game program.

Example: 
    $ python guessing_game.py
"""

__author__ = "Damien Altenburg"
__version__ = "1.0.0"

from random import randint

title_text = "** JELLYBEAN GUESSING GAME **"

LOW_RANGE = 1
HIGH_RANGE = 10
NUMBER_OF_JELLYBEANS = randint(LOW_RANGE, HIGH_RANGE)

guess_count = 0

print(title_text)
print("=" * len(title_text))

prompt_text: str = "Enter your guess: "

guess = -99

while guess != NUMBER_OF_JELLYBEANS:
    guess_is_out_of_range = True
    guess = ""

    if guess_count > 0:
        print("That guess is incorrect.")

        prompt_text = "Guess again: "

    while guess_is_out_of_range:
        try:
            guess = input(prompt_text)
            guess = int(guess)

            guess_is_out_of_range = guess < LOW_RANGE or guess > HIGH_RANGE

            if guess_is_out_of_range:
                print(f"Your guess must be between {LOW_RANGE}-{HIGH_RANGE}.")
                prompt_text = f"Guess ({LOW_RANGE}-{HIGH_RANGE}): "
        except ValueError as exception:
            print("You must enter a whole number.")
            
            prompt_text = "Re-enter guess: "

    guess_count += 1

print(f"It took you {guess_count} guess{'' if guess_count == 1 else 'es'}.")
