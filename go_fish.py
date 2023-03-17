from deck import Deck

class GoFish:
    """A game of Go Fish"""

    def __init__(self):
        self.deck = Deck()
        self.computer_hand, self.player_hand = self.deck.deal_hands(2, 7)

    def intro(self):
        """Introduce the game and the rules"""
        print("Welcome to Go Fish!")

