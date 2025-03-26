"""This module defines the PlayingCard class."""

__author__ = "Damien Altenburg"
__version__ = "1.3.2025"

class PlayingCard:
    """"""
    
    def __init__(self, rank: int, suit: str):
        """"""

        self.__rank = rank
        self.__suit = suit
        self.__is_face_up = False

    @property
    def rank(self) -> int:
        """"""

        return self.__rank
    
    @rank.setter
    def rank(self, rank: int) -> None:
        """"""

        self.__rank = rank

    @property
    def suit(self) -> str:
        """"""

        return self.__suit
    
    @suit.setter
    def suit(self, suit: str) -> None:
        """"""

        self.__suit = suit

    @property
    def is_face_up(self) -> bool:
        """"""

        return self.__is_face_up

    def flip(self) -> None:
        # if self.__is_face_up:
        #     self.__is_face_up = False
        # else:
        #     self.__is_face_up = True

        self.__is_face_up = not self.__is_face_up

    def __repr__(self) -> str:
        """"""

        return f"PlayingCard({self.__rank}, {self.__suit})"
    
    def __str__(self) -> str:
        """"""

        return f"{self.__rank} {self.__suit}"
    
    