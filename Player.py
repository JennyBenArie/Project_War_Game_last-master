from Deck_Of_Cards import DeckOfCards
from random import randint, choice


class Player:

    def __init__(self, player_name, num_of_cards=26):
        '''this method create the player for the game. each player has name and number of cards. '''
        self.player_deck = []
        self.player_name = player_name
        self.deck1=DeckOfCards()
        if 10 <= num_of_cards <= 26:
            self.num_of_cards = num_of_cards
        else:
            self.num_of_cards = 26

    def __repr__(self):
        return f"{self.player_name}, {self.player_deck}"

    def set_hand(self):
        '''this method give each player cards.'''
        for i in range(self.num_of_cards):
            self.player_deck.append(self.deck1.deal_one())

    def get_card(self):
        '''this method choose one random card from the deck and return it to the game. '''
        one_card= choice(self.player_deck)
        self.player_deck.remove(one_card)
        return one_card

    def add_card(self, card):
        '''this method add card from the game to the deck of the player.'''
        self.player_deck.append(card)



