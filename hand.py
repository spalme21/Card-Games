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
        """Remove and return a card from the hand"""
        if card in self.cards:
            return self.cards.pop(self.cards.index(card))

    def show_hand(self):
        """Show the cards in the hand"""
        for card in self.cards:
            print(card)

    def check_for_match(self, card_to_check):
        """Check hand for matching card and return it"""
        for card in self.cards:
            if card_to_check.same_value(card):
                return self.remove_card(card)

    def check_for_pairs(self):
        card_dups = []
        pairs = []
        while self.cards:
            card_1 = self.cards.pop()
            for card_2 in self.cards:
                if card_1.same_value(card_2):
                    pairs.append(card_1)
                    pairs.append(card_2)
                    break
                
            
            
