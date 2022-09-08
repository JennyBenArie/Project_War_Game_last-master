from unittest import TestCase
from Card import Card


class TestCard(TestCase):

    def setUp(self):
        self.card1 = Card('diamond', 2)

    def test_init(self):
        # Test to confirm that the value and symbol added to Card
        self.assertEqual(self.card1.value, 2)
        self.assertEqual(self.card1.symbol, 'diamond')
        # Test to confirm that the TypeError will apper if the value is out of range
        with self.assertRaises(TypeError):
            Card('diamond', 14)
        with self.assertRaises(TypeError):
            Card('diamond', 0)

    def test_gt(self):
        card_high = Card('heart', 10)
        card_low = Card('heart', 9)
        card_e = Card('diamond', 10)
        # Test that insure the higher card is bigger than the lower card
        self.assertGreater(card_high, card_low)
        # Test that insure the values are equal
        self.assertEqual(card_e, card_high)






