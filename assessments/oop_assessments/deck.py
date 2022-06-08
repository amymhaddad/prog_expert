import random


class Deck:

    valid_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    valid_suits = ["H", "D", "C", "S"]

    def __init__(self, cards=None):
        self.cards = cards or self.create_deck()

    def create_deck(self):
        return [
            value + suit for value in Deck.valid_values for suit in Deck.valid_suits
        ]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards):
        cards_to_deal = self.cards
        if num_cards > len(self.cards):
            self.cards = []
            return cards_to_deal

        cards_to_deal = self.cards[len(self.cards) - num_cards :]
        self.cards = self.cards[: len(self.cards) - num_cards]
        return cards_to_deal

    def sort_by_suit(self):
        sorted_suits = []

        for suit in Deck.valid_suits:
            for card in self.cards:
                if card[-1] == suit:
                    sorted_suits.append(card)
        self.cards = sorted_suits

    def contains(self, card):
        return card in self.cards

    def copy(self):
        return Deck(self.get_cards())

    def get_cards(self):
        return self.cards[:]

    def __len__(self):
        return len(self.cards)
