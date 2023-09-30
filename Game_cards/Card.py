<<<<<<< HEAD
class Card:
    # This method will get a type of card (spade, heart ect) and the number of the card from 1 to 13
    def __init__(self, suit, value):
        if type(suit) != int:
            raise TypeError("suit needs to be type int!!!")
        if type(value) != int:
            raise TypeError("value needs to be type int!!!")
        if suit >= 5 or suit < 1:
            raise TypeError("suit needs to be between 1-4!!!")
        if value > 13 or value < 1:
            raise TypeError("value needs to be between 1-13!!!")
        self.suit = suit
        self.value = value

    # This method will print the card
    def __repr__(self):
        suits_dict = {1:"Diamond", 2:"Spade", 3:"Heart", 4:"Club"}
        if self.value == 1:
            return f"{suits_dict[self.suit]}:Ace"
        elif self.value == 11:
            return f"{suits_dict[self.suit]}:Jack"
        elif self.value == 12:
            return f"{suits_dict[self.suit]}:Queen"
        elif self.value == 13:
            return f"{suits_dict[self.suit]}:King"
        else:
            return f"{suits_dict[self.suit]}:{self.value}"

    # This method will determine which card is greater
    def __gt__(self, other):
        if type(other) != Card:
            raise TypeError("other must be type Card!!!")
        if self.value == 1 and other.value > 1:
            return True
        elif self.value > other.value != 1:
            return True
        elif self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False

    # This method will compare between two cards and see if they are equal
    def __eq__(self, other):
        if type(other) != Card:
            raise TypeError("other must be type Card!!!")
        if self.value == other.value and self.suit == other.suit:
            return True
        else:
            return False





=======
class Card:
    # This method will get a type of card (spade, heart ect) and the number of the card from 1 to 13
    def __init__(self, suit, value):
        if type(suit) != int:
            raise TypeError("suit needs to be type int!!!")
        if type(value) != int:
            raise TypeError("value needs to be type int!!!")
        if suit >= 5 or suit < 1:
            raise TypeError("suit needs to be type int!!!")
        if value > 13 or value < 1:
            raise TypeError("value needs to be type int!!!")
        self.suit = suit
        self.value = value

    # This method will print the card
    def __repr__(self):
        suits_dict = {1:"Diamond", 2:"Spade", 3:"Heart", 4:"Club"}
        if self.value == 11:
            return f"{suits_dict[self.suit]}:Jack"
        elif self.value == 12:
            return f"{suits_dict[self.suit]}:Queen"
        elif self.value == 13:
            return f"{suits_dict[self.suit]}:King"
        else:
            return f"{suits_dict[self.suit]}:{self.value}"

    # This method will determine which card is greater
    def __gt__(self, other):
        if type(other) != Card:
            raise TypeError("other must be type Card!!!")
        if self.value == 1 and other.value > 1:
            return True
        elif self.value > other.value != 1:
            return True
        elif self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False

    # This method will compare between two students and see if they are equal
    def __eq__(self, other):
        if type(other) != Card:
            raise TypeError("other must be type Card!!!")
        if self.value == other.value and self.suit == other.suit:
            return True
        else:
            return False





>>>>>>> 85be426bae901abedf8a32c86f567ccc2bc9f80a
