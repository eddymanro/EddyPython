import random


class Card:
    all_values = ('A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K')
    all_suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def get_card(self):
        return {'value': self.value, 'suit': self.suit}

    def show_card(self):
        print(f'Card is : {self.value} of {self.suit}')


class DeckOfCards(Card):
    def __init__(self):
        self.deck = []
        for v in self.all_values:
            for s in self.all_suits:
                super().__init__(v, s)
                self.deck.append(super().get_card())

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        print(f'Dealt card is: {self.deck[-1]["value"]} of {self.deck[-1]["suit"]}')
        return self.deck.pop()

    def display_current_deck(self):
        print(f'Cards deck currently has a number of {len(self.deck)} cards left')
        for card in self.deck:
            print(f'{card["value"]} of {card["suit"]}')


def __main__():
    dk1 = DeckOfCards()
    dk1.shuffle()
    dk1.deal()
    dk1.deal()
    dk1.deal()
    dk1.display_current_deck()
    dk1.deal()
    dk1.display_current_deck()
    dk2 = DeckOfCards()
    dk2.display_current_deck()
    dk2.shuffle()
    dk2.display_current_deck()
    dk2.deal()
    dk3 = DeckOfCards()
    dk3.deal()
    dk3.shuffle()
    dk3.display_current_deck()


__main__()
