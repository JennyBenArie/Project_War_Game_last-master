from unittest import TestCase
from Player import Player
from Card import Card


class TestPlayer(TestCase):

    def test_init(self):
        # Test that Tests the default setting, edge cases and invalid user input in num_of_cards
        player1 = Player('jenny')
        self.assertEqual(player1.num_of_cards, 26)
        player1 = Player('jenny', 16)
        self.assertEqual(player1.num_of_cards, 16)
        player1 = Player('jenny', 27)
        self.assertEqual(player1.num_of_cards, 26)
        player1 = Player('jenny', 9)
        self.assertEqual(player1.num_of_cards, 26)

    def test_set_hand(self):
        # Test to insure that player get cards from deck of cards and deleting the cards taken
        player1 = Player('ron', 20)
        player1.set_hand()
        self.assertEqual(len(player1.player_deck), 20)
        self.assertEqual(len(player1.deck1.list1), 32)

    def test_get_card(self):
        # Test that tests if card is draw to the table from the deck of player
        player1 = Player('ron', 20)
        player1.set_hand()
        player1.get_card()
        self.assertEqual(len(player1.player_deck), 19)

    def test_add_card(self):
        # Test that make sure the card we gave is added to the player deck
        card = Card('diamond', 10)
        player = Player('ron', 20)
        player.add_card(card)
        self.assertIn(card, player.player_deck)

