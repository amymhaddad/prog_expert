import random

class Deck:

    valid_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    valid_suits = ['H', 'D', 'C', 'S']
        
    def __init__(self):
        self.new_deck = self.create_cards()
        self.cards = self.create_cards()

   
    def create_cards(self):
        # valid_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        # valid_suits = ['H', 'D', 'C', 'S']
        cards = []
        for value in Deck.valid_values:
            for suit in Deck.valid_suits:
                cards.append("".join([value, suit]))
        return cards

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards):
        if num_cards > len(self.cards):
            self.cards = self.new_deck
            return self.deck
        self.cards = self.cards[: len(self.cards)-num_cards]
        return self.cards
        
c = Deck() 
c.deal(3)
print(c.cards, len(c.cards))
