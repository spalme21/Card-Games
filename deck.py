from card import Card

class Deck:
    """A class to represent a deck of cards"""

    def __init__(self):
        suits = ("Hearts", "Spades", "Diamonds", "Clubs")
        values = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))
                