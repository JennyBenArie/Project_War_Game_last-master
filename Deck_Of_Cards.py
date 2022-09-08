from Card import Card
from random import randint
from random import shuffle


class DeckOfCards:

    def __init__(self):
        """method that takes the Card class and make a deck of cards
        by a form of 52 cards in 4 different shape,
        13 cards in each shape"""
        self.d1 = {'diamond': 1, 'spade': 2, 'heart': 3, 'club': 4}
        self.list1 = []
        for shape in self.d1.keys():
            for i in range(1, 14):
                new_card = Card(shape, i)
                self.list1.append(new_card)

    def cards_shuffle(self):
        """method that shuffle the deck"""
        shuffle(self.list1)

    def deal_one(self):
        """method that deal and delete one of the cards from the deck"""
        x = randint(0, len(self.list1)-1)
        y = self.list1.pop(x)
        if len(self.list1) == 0:
            raise ValueError("no more cards")
        return y



