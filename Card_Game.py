from Deck_Of_Cards import DeckOfCards
from Player import Player


class CardGame:
    def __init__(self, playername1, playername2, num_cards=26):
        '''this method gets the number of the cards for each player and his name. then it start the game. '''
        if 10 <= num_cards <= 26:
            num_cards = num_cards
        else:
            num_cards = 26
        self.player1 = Player(playername1, num_cards)
        self.player2 = Player(playername2, num_cards)
        self.deck = DeckOfCards()
        self.__new_game()

    def __repr__(self):
        return f"{self.player1}, {self.player2}"

    def __new_game(self):
        '''this method is private. it stars a new game, shuffle the cards and give each player his cards. '''
        self.deck.cards_shuffle()
        self.player1.set_hand()
        self.player2.set_hand()

    def get_winner(self):
        '''this method gives the winner of the game, based on the number of his cards.'''
        if len(self.player1.player_deck) > len(self.player2.player_deck):
            return self.player1.player_name
        elif len(self.player2.player_deck) > len(self.player1.player_deck):
            return self.player2.player_name
        else:
            return None




