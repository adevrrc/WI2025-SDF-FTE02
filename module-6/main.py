"""This module is used to demonstrate using a class."""

from playing_card.playing_card import PlayingCard
from playing_card.rank import Rank
from playing_card.suit import Suit

__author__ = "Damien Altenburg"
__version__ = "1.3.2025"

def main():
    """"""

    #playing_card = PlayingCard(Rank.ACE, "Club")

    #playing_card = PlayingCard(0, "Heart")
    playing_card = PlayingCard(Rank.ACE, Suit.HEART)

    print(playing_card)

    #playing_card = PlayingCard(6, "Club")
    playing_card = PlayingCard(Rank.SIX, Suit.CLUB)

    print(playing_card)

    playing_card.suit = Suit.HEART
    playing_card.rank = Rank.TEN

    print(playing_card.rank)
    print(playing_card.suit)

    playing_card.flip()

    print(repr(playing_card))
    print(str(playing_card))

if __name__ == "__main__":
    main()
