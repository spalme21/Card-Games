class Card:
    """
    A class to represent a playing card
    """

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def same_value(self, *cards):
        """Compare the value of cards"""
        for card in cards:
            if card.value != self.value:
                return False
        return True
