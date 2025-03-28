"""This module defines the tests for the PlayingCard class."""

__author__ = "Damien Altenburg"
__version__ = "1.3.2025"

import unittest
from playing_card.rank import Rank
from playing_card.suit import Suit
from playing_card.playing_card import PlayingCard

class TestPlayingCard(unittest.TestCase):
    """Defines the unit tests for the PlayingCard class."""
    
    ### __init__(Rank, Suit)

    def test_init_TypeError_rank_is_not_a_Rank_type(self):
        # Arrange
        rank = ""
        suit = Suit.CLUB

        # Act
        with self.assertRaises(TypeError) as context:
            playing_card = PlayingCard(rank, suit)

        # Assert
        expected = "The rank must be of type Rank."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_init_TypeError_suit_is_not_a_Suit_type(self):
        # Arrange
        rank = Rank.QUEEN
        suit = "Suit.CLUB"

        # Act
        with self.assertRaises(TypeError) as context:
            playing_card = PlayingCard(rank, suit)

        # Assert
        expected = "The suit must be of type Suit."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_init_initial_state_set(self):
        # Arrange
        rank = Rank.QUEEN
        suit = Suit.CLUB

        # Act
        playing_card = PlayingCard(rank, suit)

        # Assert
        expected_rank = Rank.QUEEN
        expected_suit = Suit.CLUB
        expected_is_face_up = False

        self.assertEqual(expected_rank, playing_card._PlayingCard__rank)
        self.assertEqual(expected_suit, playing_card._PlayingCard__suit)
        self.assertEqual(expected_is_face_up, playing_card._PlayingCard__is_face_up)

    ### rank Property

    def test_rank_gets_the_current_state(self):
        # Arrange
        rank = Rank.QUEEN
        suit = Suit.CLUB

        playing_card = PlayingCard(rank, suit)

        # Act
        actual = playing_card.rank

        # Assert
        expected = Rank.QUEEN
        self.assertEqual(expected, actual)

    def test_rank_set_updates_state(self):
        # Arrange
        rank = Rank.QUEEN
        suit = Suit.CLUB

        playing_card = PlayingCard(rank, suit)

        # Act
        playing_card.rank = Rank.ACE

        # Assert
        expected = Rank.ACE
        actual = playing_card._PlayingCard__rank
        self.assertEqual(expected, actual)

    ### flip()

    def test_flip_state_changes_to_face_up(self):
        # Arrange
        rank = Rank.QUEEN
        suit = Suit.CLUB

        playing_card = PlayingCard(rank, suit)

        # Act
        playing_card.flip()

        # Assert
        expected = True
        actual = playing_card._PlayingCard__is_face_up
        self.assertEqual(expected, actual)

    def test_flip_state_changes_to_face_down(self):
        # Arrange
        rank = Rank.QUEEN
        suit = Suit.CLUB

        playing_card = PlayingCard(rank, suit)

        # Card needs to be face up
        playing_card._PlayingCard__is_face_up = True

        # Act
        playing_card.flip()

        # Assert
        expected = False
        actual = playing_card._PlayingCard__is_face_up
        self.assertEqual(expected, actual)

    ### __str__()

    def test_repr_returns_string_representation(self):
        # Arrange
        rank = Rank.QUEEN
        suit = Suit.CLUB

        playing_card = PlayingCard(rank, suit)

        # Act
        actual = playing_card.__repr__()

        # Assert
        expected = "PlayingCard(Rank.QUEEN, Suit.CLUB)"
        self.assertEqual(expected, actual)
    
if __name__ == "__main__":
    unittest.main()
