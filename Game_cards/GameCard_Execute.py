<<<<<<< HEAD
from Card import Card
from DeckOfCards import DeckOfCards
from Player import Player
from CardGame import CardGame

The_game = CardGame("Dani", "Shimi")
print(The_game)
for i in range(10):
    card1 = The_game.player1.get_card()
    card2 = The_game.player2.get_card()
    print(f"Round {i + 1}")
    print(f"{The_game.player1.name}'s card: {card1}")
    print(f"{The_game.player2.name}'s card: {card2}")
    if card1 > card2:
        The_game.player1.add_card(card1)
        The_game.player1.add_card(card2)
        print(f"The winner in this round is {The_game.player1.name}\n")
    else:
        The_game.player2.add_card(card1)
        The_game.player2.add_card(card2)
        print(f"The winner this round is {The_game.player2.name}\n")

if The_game.get_winner() == None:
    print("It's a tie!!!")
else:
    print(The_game.get_winner())


=======
from Card import Card
from DeckOfCards import DeckOfCards
from Player import Player
from CardGame import CardGame

The_game = CardGame("Dani", "Shimi")
print(The_game)
for i in range(10):
    card1 = The_game.player1.get_card()
    card2 = The_game.player2.get_card()
    print(f"Round {i + 1}")
    print(f"{The_game.player1.name}'s card: {card1}")
    print(f"{The_game.player2.name}'s card: {card2}")
    if card1 > card2:
        The_game.player1.add_card(card1)
        The_game.player1.add_card(card2)
        print(f"The winner in this round is {The_game.player1.name}\n")
    else:
        The_game.player2.add_card(card1)
        The_game.player2.add_card(card2)
        print(f"The winner this round is {The_game.player2.name}\n")

if The_game.get_winner() == None:
    print("It's a tie!!!")
else:
    print(The_game.get_winner())


>>>>>>> 85be426bae901abedf8a32c86f567ccc2bc9f80a
