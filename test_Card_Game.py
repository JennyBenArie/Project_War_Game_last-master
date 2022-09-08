from unittest import TestCase
from Card_Game import CardGame
from Card import Card


class TestCardGame(TestCase):
    def test_init(self):
        game = CardGame('jenny', 'ron')
        # Default is 26
        self.assertEqual(game.player1.num_of_cards, 26)
        self.assertEqual(game.player2.num_of_cards, 26)
        game = CardGame('jenny', 'ron', 27)
        # If number of cards invalid, default is 26
        self.assertEqual(game.player1.num_of_cards, 26)
        self.assertEqual(game.player2.num_of_cards, 26)
        game = CardGame('jenny', 'ron', 9)
        # If number of cards invalid, default is 26
        self.assertEqual(game.player1.num_of_cards, 26)
        self.assertEqual(game.player2.num_of_cards, 26)
        game = CardGame('jenny', 'ron', 10)
        # A valid edge case
        self.assertEqual(game.player1.num_of_cards, 10)
        self.assertEqual(game.player2.num_of_cards, 10)

    def test_get_winner_None(self):
        # If both player's deck of card is equal, the method will return None
        # If one of the players wins it return his name
        game = CardGame('Ron', 'Jenny', 13)
        self.assertIsNone(game.get_winner())
        game.player1.player_deck.append(Card('diamond', 9))
        self.assertEqual(len(game.player1.player_deck), 14)
        self.assertEqual(game.player1.player_name, game.get_winner())
        game = CardGame('Ron', 'Jenny', 13)
        game.player2.player_deck.append(Card('diamond', 6))
        self.assertEqual(len(game.player2.player_deck), 14)
        self.assertEqual(game.player2.player_name, game.get_winner())










