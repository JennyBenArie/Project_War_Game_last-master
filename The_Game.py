from Card_Game import CardGame


# Name insert
player1 = input("Enter player's name: ")
player2 = input("Enter second player's name: ")


our_game = CardGame(player1, player2, 26)
# Player1's Deck of cards
print(our_game.player1)
# Player2's Deck of cards
print(our_game.player2)

# The game: runs 10 rounds, every round there is a winner,  at the end of the game it show the winner of the game
for i in range(10):
    card_player1 = our_game.player1.get_card()
    card_player2 = our_game.player2.get_card()
    print(f"({player1}: {card_player1}) VS ({player2}: {card_player2}) ")
    if card_player1 > card_player2:
        our_game.player1.add_card(card_player2)
        our_game.player1.add_card(card_player1)
        print(f"{player1} won this round!")
    else:
        our_game.player2.add_card(card_player2)
        our_game.player2.add_card(card_player1)
        print(f"{player2} won this round!")

# print the number of cards each player has at the end of the game
print(player1, "number of cards: ", len(our_game.player1.player_deck))
print(player2, "number of cards: ",  len(our_game.player2.player_deck))
# prints the winner
if our_game.get_winner() is None:
    print(None)
else:
    print(f"{our_game.get_winner()} is the winner!!!")








