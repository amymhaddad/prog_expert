import random 

class Deck:

    valid_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    valid_suits = ['H', 'D', 'C', 'S']
 
    #creating optional param
    def __init__(self, cards=None):
        self.new_deck = self.create_cards()
        #if cards is None, then self.create_cards() is run
        self.cards = cards or self.create_cards()

    def create_cards(self):
        cards = []
        for value in Deck.valid_values:
            for suit in Deck.valid_suits:
                cards.append("".join([value, suit]))
        return cards

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards):
        returned_cards = self.cards 
        if num_cards > len(self.cards):
            self.cards = []
            return returned_cards 

        self.cards = self.cards[:len(self.cards)-num_cards]
        return returned_cards #here -- need to return the front most optoins -- not inlcuding hte returned_cards [a b c d e] -- need to return [a b c]
   
    def sort_by_suit(self):
        sorted_suits = []

        for suit in Deck.valid_suits:
            for card in self.cards:
                if card[1] == suit:
                    sorted_suits.append(card)
        print(sorted_suits)
        self.cards = sorted_suits

    def contains(self, card):
        return card in self.cards
    
    def copy(self):
        #Creating new deck w/copy of cards
        #return Deck(self.get_cards())
        return Deck(self.cards[:])

    def get_cards(self):
        return self.cards[:]

    def __len__(self):
        return len(self.cards)


deck1 = Deck()
for i in range(10):
    cards = deck1.deal(5)
    #self.assertEqual(5, len(cards))
print(deck1.cards)
#self.cards isn't staying updated after the for loop runs
# cards = deck1.deal(5)
# print(deck1.cards)
