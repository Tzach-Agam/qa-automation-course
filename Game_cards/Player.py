<<<<<<< HEAD
from Card import Card
from DeckOfCards import DeckOfCards
import random

class Player:
    # The method will create a player and all his information: his name, how many cards he'll have and a list of his cards
    def __init__(self, name, dealt_cards = 26):
        if type(name) != str:
            raise TypeError("name needs to be type str!!!")
        if type(dealt_cards) != int:
            raise TypeError("dealt cards has to be type int!!!")
        for i in name:
            if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                raise TypeError("name cannot have numbers in it!!!")
        self.name = name
        if dealt_cards > 26 or dealt_cards < 10:
            dealt_cards = 26
        self.dealt_cards = dealt_cards
        self.player_cards = []

    # This method will print the player information
    def __repr__(self):
        return f"The player's information: Name: {self.name}. His cards: {self.player_cards}"

    # This method will create the player's pack of cards by the number of cards they are dealt
    def set_hand(self, cards_pack:DeckOfCards):
        if type(cards_pack) != DeckOfCards:
            raise TypeError("The pack needs to be type DeckOfCards!!!")
        if len(cards_pack.cards_pack) < self.dealt_cards:
            raise TypeError("sorry!!! not enough cards!!")
        for card in range(self.dealt_cards):
            self.player_cards.append(cards_pack.deal_one())

    # This method will show the card the player put in the round
    def get_card(self):
        player_card = random.choice(self.player_cards)
        self.player_cards.remove(player_card)
        return player_card

    # The method will add a card to the players pack
    def add_card(self, card:Card):
        self.player_cards.append(card)

# player = Player("TZACH")
# deck = DeckOfCards()
# player.set_hand(deck)
# print(player)











=======
from Card import Card
from DeckOfCards import DeckOfCards
import random

class Player:
    # The method will create a player and all his information: his name, how many cards he'll have and a list of his cards
    def __init__(self, name, dealt_cards = 26):
        if type(name) != str:
            raise TypeError("name needs to be type str!!!")
        if type(dealt_cards) != int:
            raise TypeError("dealt cards has to be type int!!!")
        for i in name:
            if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                raise TypeError("name cannot have numbers in it!!!")
        self.name = name
        if dealt_cards > 26 or dealt_cards < 10:
            dealt_cards = 26
        self.dealt_cards = dealt_cards
        self.player_cards = []

    # This method will print the player information
    def __repr__(self):
        return f"The player's information: Name: {self.name}. His cards: {self.player_cards}"

    # This method will create the player's pack of cards by the number of cards they are dealt
    def set_hand(self, cards_pack:DeckOfCards):
        if type(cards_pack) != DeckOfCards:
            raise TypeError("The pack needs to be type DeckOfCards!!!")
        if len(cards_pack.cards_pack) < self.dealt_cards:
            raise TypeError("sorry!!! not enough cards!!")
        for card in range(self.dealt_cards):
            self.player_cards.append(cards_pack.deal_one())

    # This method will show the card the player put in the round
    def get_card(self):
        player_card = random.choice(self.player_cards)
        self.player_cards.remove(player_card)
        return player_card

    # The method will add a card to the players pack
    def add_card(self, card:Card):
        self.player_cards.append(card)













>>>>>>> 85be426bae901abedf8a32c86f567ccc2bc9f80a
