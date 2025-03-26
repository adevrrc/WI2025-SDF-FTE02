"""This module is used to demonstrate using a class."""

from playing_card.playing_card import PlayingCard

__author__ = "Damien Altenburg"
__version__ = "1.3.2025"

def main():
    """"""

    playing_card = PlayingCard(0, "Heart")

    print(playing_card)

    playing_card = PlayingCard(6, "Club")

    print(playing_card)

    playing_card.suit = "Heart"
    playing_card.rank = 10

    print(playing_card.rank)
    print(playing_card.suit)

    playing_card.flip()

    print(repr(playing_card))
    print(str(playing_card))

if __name__ == "__main__":
    main()
