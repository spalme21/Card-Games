import time

from deck import Deck

class GoFish:
    """A game of Go Fish"""

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.computer_hand, self.player_hand = self.deck.deal_hands(2, 7)
        self.computer_pairs = self.computer_hand.check_for_pairs()
        self.player_pairs = self.player_hand.check_for_pairs()

    def run_game(self):
        """Run the game"""
        self._start()

    def _start(self):
        """Introduce the game and the rules"""
        print("Welcome to Go Fish!\n")
        time.sleep(1)
        name = input("Enter your name: ")
        print(f"Hello {name}!\n")
        time.sleep(1)
        print("Here's your hand, with pairs removed:")
        self.player_hand.show_hand()
        self._show_pairs(self.player_pairs)
        time.sleep(1)
        print("\nHere are my pairs: ")
        self._show_pairs(self.computer_pairs)

    def _turn(self):
        """A turn"""
        
    def _show_pairs(self, pairs):
        "Display pairs"
        print("\nPairs:")
        if pairs:
            for card in pairs:
                print(card)
        else:
            print("No pairs")


if __name__ == "__main__":
    game = GoFish()
    game.run_game()
