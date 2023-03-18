from random import shuffle

from card import Card
from hand import Hand

class Deck:
    """A class to represent a deck of cards"""

    def __init__(self):
        suits = ("Hearts", "Spades", "Diamonds", "Clubs")
        values = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

        self.cards = [Card(suit, value) for suit in suits for value in values]

    def shuffle_deck(self):
        """Return a shuffled deck"""
        shuffle(self.cards)

    def draw(self):
        """Remove the top card and return it"""
        return self.cards.pop()

    def deal_hands(self, number_of_hands, size_of_hand):
        """Return  a set number of hands of a set number of cards"""
        hands = [Hand() for i in range(number_of_hands)]
        for i in range(size_of_hand):
            for hand in hands:
                hand.add_card(self.draw())
        return hands
