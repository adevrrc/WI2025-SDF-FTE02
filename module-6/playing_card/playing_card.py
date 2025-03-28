"""This module defines the PlayingCard class."""

from playing_card.rank import Rank
from playing_card.suit import Suit

__author__ = "Damien Altenburg"
__version__ = "1.3.2025"

class PlayingCard:
    """"""
    
    def __init__(self, rank: Rank, suit: Suit):
        """"""

        self.rank = rank
        self.suit = suit
        self.__is_face_up = False

    @property
    def rank(self) -> Rank:
        """"""

        return self.__rank
    
    @rank.setter
    def rank(self, rank: Rank) -> None:
        """"""

        if not isinstance(rank, Rank):
            raise TypeError("The rank must be of type Rank.")

        self.__rank = rank

    @property
    def suit(self) -> Suit:
        """"""

        return self.__suit
    
    @suit.setter
    def suit(self, suit: Suit) -> None:
        """"""

        if not isinstance(suit, Suit):
            raise TypeError("The suit must be of type Suit.")

        self.__suit = suit

    @property
    def is_face_up(self) -> bool:
        """"""

        return self.__is_face_up

    def flip(self) -> None:
        """"""

        self.__is_face_up = not self.__is_face_up

    def __repr__(self) -> str:
        """"""

        return f"PlayingCard({self.__rank}, {self.__suit})"
    
    def __str__(self) -> str:
        """"""

        card_text = "[CARD]"

        if self.is_face_up:
            card_text = f"{self.__rank} {self.__suit}"

        return card_text
