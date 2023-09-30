<<<<<<< HEAD
from DeckOfCards import DeckOfCards
from Player import Player

class CardGame:
    # This method will create the game and all it's information including the players
    def __init__(self, name_p1, name_p2, dealt_cards = 26):
        if type(name_p1) != str:
            raise TypeError("The name of the player has to be type str!!!")
        if type(name_p2) != str:
            raise TypeError("The name of the player has to be type str!!!")
        if type(dealt_cards) != int:
            raise TypeError("dealt_cards needs to be type int!!!")
        for i in name_p1:
            if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                raise TypeError("name cannot have numbers in it!!!")
        for i in name_p2:
            if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                raise TypeError("name cannot have numbers in it!!!")
        if dealt_cards > 26 or dealt_cards < 10:
            dealt_cards = 26
        self.dealt_cards = dealt_cards
        self.deck_cards = DeckOfCards()
        self.player1 = Player(name_p1, dealt_cards)
        self.player2 = Player(name_p2, dealt_cards)
        self.new_game()

    # The method will print the players information
    def __repr__(self):
        return f"The Players:\n" \
               f"Player1: {self.player1}\n" \
               f"Player2: {self.player2}\n"

    # The method will shuffle the pack of cards and will give the players the number of cards they need
    def new_game(self):
        if len(self.player1.player_cards) > 0 or len(self.player2.player_cards) > 0:
            raise TypeError("The game has already started")
        if len(self.deck_cards.cards_pack) == 52:
            self.deck_cards.cards_shuffle()
            self.player1.set_hand(self.deck_cards)
            self.player2.set_hand(self.deck_cards)
        else:
            return None

    # This method will determine which player won the game
    def get_winner(self):
        length_card1 = len(self.player1.player_cards)
        length_card2 = len(self.player2.player_cards)
        if length_card1 > length_card2:
            return f"The winner in the game is {self.player1.name}!!!"
        elif length_card1 < length_card2:
            return f"The winner in the game is {self.player2.name}!!!"
        elif length_card1 == length_card2:
            return None



















=======
from DeckOfCards import DeckOfCards
from Player import Player

class CardGame:
    # This method will create the game and all it's information including the players
    def __init__(self, name_p1, name_p2, dealt_cards = 26):
        if type(name_p1) != str:
            raise TypeError("The name of the player has to be type str!!!")
        if type(name_p2) != str:
            raise TypeError("The name of the player has to be type str!!!")
        if type(dealt_cards) != int:
            raise TypeError("dealt_cards needs to be type int!!!")
        for i in name_p1:
            if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                raise TypeError("name cannot have numbers in it!!!")
        for i in name_p2:
            if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                raise TypeError("name cannot have numbers in it!!!")
        if dealt_cards > 26 or dealt_cards < 10:
            dealt_cards = 26
        self.dealt_cards = dealt_cards
        self.deck_cards = DeckOfCards()
        self.player1 = Player(name_p1, dealt_cards)
        self.player2 = Player(name_p2, dealt_cards)
        self.new_game()

    # The method will print the players information
    def __repr__(self):
        return f"The Players:\n" \
               f"Player1: {self.player1}\n" \
               f"Player2: {self.player2}\n"

    # The method will shuffle the pack of cards and will give the players the number of cards they need
    def new_game(self):
        if len(self.player1.player_cards) > 0 or len(self.player2.player_cards) > 0:
            raise TypeError("The game has already started")
        if len(self.deck_cards.cards_pack) == 52:
            self.deck_cards.cards_shuffle()
            self.player1.set_hand(self.deck_cards)
            self.player2.set_hand(self.deck_cards)
        else:
            return None

    # This method will determine which player won the game
    def get_winner(self):
        length_card1 = len(self.player1.player_cards)
        length_card2 = len(self.player2.player_cards)
        if length_card1 > length_card2:
            return f"The winner in the game is {self.player1.name}!!!"
        elif length_card1 < length_card2:
            return f"The winner in the game is {self.player2.name}!!!"
        elif length_card1 == length_card2:
            return None



















>>>>>>> 85be426bae901abedf8a32c86f567ccc2bc9f80a
