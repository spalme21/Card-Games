import time

from deck import Deck

class GoFish:
    """A game of Go Fish"""

    def __init__(self):
        self.deck = Deck()
        self.computer_hand, self.player_hand = self.deck.deal_hands(2, 7)
        self.computer_pairs = []
        self.player_pairs = []

    def run_game(self):
        """Run the game"""
        self._intro()

    def _intro(self):
        """Introduce the game and the rules"""
        print("Welcome to Go Fish!")
        time.sleep(1)
        name = input("Enter your name: ")
        print(f"Hello {name}!")
        time.sleep(1)
        print("Here's your hand:")
        self.player_hand.show_hand()
        time.sleep(1)
        

if __name__ == "__main__":
    game = GoFish()
    game.run_game()
