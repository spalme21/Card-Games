import card

class Hand:
    """
    A class to represent a hand of playing cards
    """

    def __init__(self):
        self.cards = []

    def is_empty(self):
        if self.cards:
            return False
        return True

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
        return False

    def check_for_pairs(self):
        """Check hand for pairs and remove them"""
        card_dups = []
        pairs = []
        while self.cards:
            card_1 = self.cards.pop()
            for card_2 in self.cards:
                if card_1.same_value(card_2):
                    pairs.append(card_1)
                    pairs.append(self.cards.pop(self.cards.index(card_2)))
                    break
            if card_1 not in pairs:
                card_dups.append(card_1)
        self.cards = card_dups
        return pairs
    