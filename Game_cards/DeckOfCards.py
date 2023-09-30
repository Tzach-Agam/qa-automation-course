<<<<<<< HEAD
from Card import Card
import random

class DeckOfCards:
    # This method will create a list of all 52 cards by using the Card class
    def __init__(self):
        self.cards_pack = []
        for suit in range(1,5):
            for value in range(1,14):
                card = Card(suit, value)
                self.cards_pack.append(card)

    # This method will print the list of the cards
    def __repr__(self):
        return f"The deck of card is: {self.cards_pack}"

    # This method will shuffle the list of cards
    def cards_shuffle(self):
        random.shuffle(self.cards_pack)

    # This method will deal one card from the pack to the player
    def deal_one(self):
        rand_card = random.choice(self.cards_pack)
        self.cards_pack.remove(rand_card)
        return rand_card



# deck = DeckOfCards()
# print(deck.cards_pack)
# deck.cards_shuffle()
# print(type(deck.deal_one()))

















=======
from Card import Card
import random

class DeckOfCards:
    # This method will create a list of all 52 cards by using the Card class
    def __init__(self):
        self.cards_pack = []
        for suit in range(1,5):
            for value in range(1,14):
                card = Card(suit, value)
                self.cards_pack.append(card)

    # This method will print the list of the cards
    def __repr__(self):
        return f"The deck of card is: {self.cards_pack}"

    # This method will shuffle the list of cards
    def cards_shuffle(self):
        random.shuffle(self.cards_pack)

    # This method will deal one card from the pack to the player
    def deal_one(self):
        rand_card = random.choice(self.cards_pack)
        self.cards_pack.remove(rand_card)
        return rand_card



# deck = DeckOfCards()
# print(deck.cards_pack)
# deck.cards_shuffle()
# print(type(deck.deal_one()))

















>>>>>>> 85be426bae901abedf8a32c86f567ccc2bc9f80a
