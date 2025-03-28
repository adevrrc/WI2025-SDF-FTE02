"""This module defines the tests for the PlayingCard class.

Test Cases:
    __init__(Rank, Suit)
    - rank is not a Rank (TypeError: The rank must be a Rank.)
    - suit is not a Suit (TypeError: The suit must be a Suit.)
    - Initialize instance.

    rank Property
    - Get the current state
    - Set rank to a type that isn't Rank. (TypeError: The rank must be 
        a Rank.)
    - Set rank to update state.

    suit Property
    - Get the current state
    - Set suit to a type that isn't Suit. (TypeError: The suit must be 
        a Suit.)
    - Set suit to update state.

    is_face_up()
    - Get current state.

    __is_face_card()
    - Returns False when not a face card.
    - Returns True when is a face card.

    flip()
    - Flip card when face down.
    - Flip card when face up.

    __repr__()
    - Returns the official string representation.

    __str__()
    - Returns the informal string representation when face up.
    - Returns the informal string representation when face down.

Example:
    $ python -m unittest tests/test_playing_card.py
"""

__author__ = "Damien Altenburg"
__version__ = "1.3.2025"

import unittest
from playing_card.rank import Rank
from playing_card.suit import Suit
from playing_card.playing_card import PlayingCard

class TestPlayingCard(unittest.TestCase):
    """Defines the unit tests for the PlayingCard class."""

    ### __init__()

    def test_init_raises_TypeError_rank_is_not_a_Rank(self):
        # Arrange
        rank = "Rank.JACK"
        suit = Suit.CLUB

        # Act
        with self.assertRaises(TypeError) as context:
            card = PlayingCard(rank, suit)

        # Assert
        expected = "The rank must be a Rank."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_init_raises_TypeError_suit_is_not_a_Suit(self):
        # Arrange
        rank = Rank.JACK
        suit = "Suit.CLUB"

        # Act
        with self.assertRaises(TypeError) as context:
            card = PlayingCard(rank, suit)

        # Assert
        expected = "The suit must be a Suit."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_init_initialize_a_playing_card(self):
        # Arrange
        rank = Rank.JACK
        suit = Suit.CLUB

        # Act
        card = PlayingCard(rank, suit)

        # Assert
        expected_rank = Rank.JACK
        expected_suit = Suit.CLUB
        expected_is_face_up = False

        self.assertEqual(expected_rank, card._PlayingCard__rank)
        self.assertEqual(expected_suit, card._PlayingCard__suit)
        self.assertEqual(expected_is_face_up, card._PlayingCard__is_face_up)

    ### rank Property

    def test_rank_get_current_state(self):
        # Arrange
        rank = Rank.JACK
        suit = Suit.CLUB

        card = PlayingCard(rank, suit)

        # Act
        actual = card.rank

        # Assert
        expected = Rank.JACK
        self.assertEqual(expected, actual)

    def test_rank_set_to_a_value_not_a_Rank_raises_TypeError(self):
        # Arrange
        rank = Rank.JACK
        suit = Suit.CLUB

        card = PlayingCard(rank, suit)

        # Act
        with self.assertRaises(TypeError) as context:
            card.rank = "Rank.JACK"

        # Assert
        expected = "The rank must be a Rank."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_rank_set_updates_state(self):
        # Arrange
        rank = Rank.JACK
        suit = Suit.CLUB

        card = PlayingCard(rank, suit)

        # Act
        card.rank = Rank.ACE

        # Assert
        expected = Rank.ACE
        self.assertEqual(expected, card._PlayingCard__rank)

    ### suit Property

    def test_suit_get_current_state(self):
        # Arrange
        rank = Rank.JACK
        suit = Suit.CLUB

        card = PlayingCard(rank, suit)

        # Act
        actual = card.suit

        # Assert
        expected = Suit.CLUB
        self.assertEqual(expected, actual)

    def test_suit_set_to_a_value_not_a_Suit_raises_TypeError(self):
        # Arrange
        rank = Rank.JACK
        suit = Suit.CLUB

        card = PlayingCard(rank, suit)

        # Act
        with self.assertRaises(TypeError) as context:
            card.suit = "Suit.CLUB"

        # Assert
        expected = "The suit must be a Suit."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_suit_set_updates_state(self):
        # Arrange
        rank = Rank.JACK
        suit = Suit.CLUB

        card = PlayingCard(rank, suit)

        # Act
        card.suit = Suit.HEART

        # Assert
        expected = Suit.HEART
        self.assertEqual(expected, card._PlayingCard__suit)

    ### is_face_up Property

    def test_is_face_up_get_current_state(self):
        # Arrange
        rank = Rank.JACK
        suit = Suit.CLUB

        card = PlayingCard(rank, suit)

        # Act
        actual = card.is_face_up

        # Assert
        self.assertFalse(actual)

    ### __is_face_card()

    def test_is_face_card_not_face_card(self):
        # Arrange
        rank = Rank.TWO
        suit = Suit.CLUB

        card = PlayingCard(rank, suit)

        # Act
        actual = card._PlayingCard__is_face_card()

        # Assert
        self.assertFalse(actual)

    def test_is_face_card_is_face_card(self):
        # Arrange
        rank = Rank.QUEEN
        suit = Suit.CLUB

        card = PlayingCard(rank, suit)

        # Act
        actual = card._PlayingCard__is_face_card()

        # Assert
        self.assertTrue(actual)

    ### flip()

    def test_flip_card_starts_face_down(self):
        # Arrange
        rank = Rank.QUEEN
        suit = Suit.CLUB

        card = PlayingCard(rank, suit)

        # Act
        card.flip()

        # Assert
        self.assertTrue(card._PlayingCard__is_face_up)

    def test_flip_card_starts_face_up(self):
        # Arrange
        rank = Rank.QUEEN
        suit = Suit.CLUB

        card = PlayingCard(rank, suit)

        card._PlayingCard__is_face_up = True

        # Act
        card.flip()

        # Assert
        self.assertFalse(card._PlayingCard__is_face_up)

    ### __repr__()

    def test_repr_returns_string_representation(self):
        # Arrange
        rank = Rank.QUEEN
        suit = Suit.CLUB

        card = PlayingCard(rank, suit)

        # Act
        actual = card.__repr__()

        # Assert
        expected = "PlayingCard(Rank.QUEEN, Suit.CLUB)"
        self.assertEqual(expected, actual)

    ### __str__()

    def test_str_card_face_down(self):
        # Arrange
        rank = Rank.QUEEN
        suit = Suit.CLUB

        card = PlayingCard(rank, suit)

        # Act
        actual = card.__str__()

        # Assert
        expected = "\u2593"
        self.assertEqual(expected, actual)

    def test_str_card_face_up(self):
        # Arrange
        rank = Rank.QUEEN
        suit = Suit.CLUB

        card = PlayingCard(rank, suit)

        card._PlayingCard__is_face_up = True

        # Act
        actual = card.__str__()

        # Assert
        expected = "Q\u2663"
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
