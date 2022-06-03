import random

class Deck:

    valid_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    valid_suits = ['H', 'D', 'C', 'S']
        
    def __init__(self):
        self.new_deck = self.create_cards()
        self.cards = self.create_cards()

   
    def create_cards(self):
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
   
    def sort_by_suit(self):
        sorted_suits = []

        for suit in Deck.valid_suits:
            for card in self.cards:
                if card[1] == suit:
                    sorted_suits.append(card)
        self.cards = sorted_suits


        
c = Deck() 
c.deal(3)
c.sort_by_suit()
print(c.cards)
