from random import shuffle

from card import Card

class Deck:
    """A class to represent a deck of cards"""

    def __init__(self):
        suits = ("Hearts", "Spades", "Diamonds", "Clubs")
        values = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

        self.cards = [Card(suit, value) for suit in suits for value in values]

    def shuffle_deck(self):
        """Return a shuffled deck"""
        shuffle(self.cards)

    def draw(self):
        """Remove the top card and return it"""
        return self.cards.pop()
