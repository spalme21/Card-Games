import card

class Hand:
    """
    A class to represent a hand of playing cards
    """

    def __init__(self):
        self.cards = []

    def add_card(self, card):
        """Add a card to the hand"""
        self.cards.append(card)

    def remove_card(self, card):
        """Remove a card from the hand"""
        self.card.remove(card)

    def show_hand(self):
        """Show the cards in the hand"""
        for card in self.cards:
            print(card)