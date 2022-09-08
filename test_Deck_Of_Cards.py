from unittest import TestCase
from Deck_Of_Cards import DeckOfCards
from Card import Card


class TestDeckOfCards(TestCase):

    def setUp(self) :
        self.deck1 = DeckOfCards()

    def test_init(self):
        # Test that insure the cards edge cases are inside the deck of cards
        self.assertIn(Card('diamond', 13), self.deck1.list1)
        self.assertIn(Card('diamond', 1), self.deck1.list1)
        #card values 0 and 14 been tested in Card test

    def test_cards_shuffle(self):
        # Test to insure no cards removed from the deck
        self.deck1.cards_shuffle()
        self.assertEqual(len(self.deck1.list1), 52)

    def test_deal_one(self):
        # Test to insure the card removed from the list
        deleted_card = self.deck1.deal_one()
        self.assertNotIn(deleted_card, self.deck1.list1)
        self.assertEqual(51, len(self.deck1.list1))

    def test_deal_one_empty(self):
        # Test to check if ValueError is apper on empty list
        self.deck1.list1= []
        with self.assertRaises(ValueError):
            self.deck1.deal_one()