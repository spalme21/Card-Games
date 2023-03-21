import time
from random import choice

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
        while self.deck.cards:
            self.player_turn()
            self.computer_turn()

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

    def player_turn(self):
        """A turn"""
        print("It's your turn.")
        time.sleep(1)
        if self.player_hand.is_empty():
            print("\nYou have no cards. Draw.")
            self.player_hand.add_card(self.deck.draw())
        print("\nHere's your hand: ")
        self.player_hand.show_hand()
        time.sleep(1)
        request = input("\nEnter the card you want to ask for: ").upper()
        options = [card.value for card in self.player_hand.cards]
        while request not in options:
            request = input("Invalid card. Try again: ").upper()
        for card in self.player_hand.cards:
            if card.value == request:
                requested_card = self.player_hand.remove_card(card)
        match = self.computer_hand.check_for_match(requested_card)
        if match:
            time.sleep(1)
            print("You got a match!")
            self.player_pairs.append(match)
            self.player_pairs.append(requested_card)
            self._show_pairs(self.player_pairs)
            print("\nGo again!")
            time.sleep(1)
            self.player_turn()
        else:
            time.sleep(1)
            print("Go fish!")
            time.sleep(1)
            drawn = self.deck.draw()
            print(f"You drew a {drawn}.\n")
            time.sleep(1)
            if drawn.same_value(requested_card):
                print("You got the card you asked for!")
                self.player_pairs.append(drawn)
                self.player_pairs.append(requested_card)
                self._show_pairs(self.player_pairs)
                time.sleep(1)
                self.player_turn()
            else:
                self.player_hand.add_card(requested_card)
                match = self.player_hand.check_for_match(drawn)
                if match:
                    print("You got a match!")
                    self.player_pairs.append(match)
                    self.player_pairs.append(drawn)
                    self._show_pairs(self.player_pairs)
                else:
                    self.player_hand.add_card(drawn)
                    
    def computer_turn(self):
        """Computers turn"""
        print("Now it's my turn.")
        time.sleep(1)
        if self.computer_hand.is_empty():
            print("I have no cards, so I'll draw.")
            self.computer_hand.add_card(self.deck.draw())
        request = self.computer_hand.remove_card(choice(self.computer_hand.cards))
        print(f"Do you have any {request.value}'s")
        match = self.player_hand.check_for_match(request)
        time.sleep(1)
        if match:
            print("I got a match!")
            self.computer_pairs.append(match)
            self.computer_pairs.append(request)
            print("Here are my pairs: ")
            self._show_pairs(self.computer_pairs)
            print("\nI'll go again!")
            time.sleep(1)
            self.computer_turn()
        else:
            print("Not a match. I'll go fish.")
            drawn = self.deck.draw()
            time.sleep(1)
            if drawn.same_value(request):
                print("I got the card I asked for! Here are my pairs: ")
                self.computer_pairs.append(drawn)
                self.computer_pairs.append(request)
                print("Here are my pairs: ")
                self._show_pairs(self.computer_pairs)
                print("\nI'll go again!")
                time.sleep(1)
                self.computer_turn()
            else:
                self.computer_hand.add_card(request)
                match = self.computer_hand.check_for_match(drawn)
                if match:
                    print("I got a match!")
                    self.computer_pairs.append(match)
                    self.computer_pairs.append(request)
                    print("Here are my pairs: ")
                    self._show_pairs(self.computer_pairs)
                    time.sleep(1)


        

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
