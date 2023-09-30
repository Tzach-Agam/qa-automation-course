<<<<<<< HEAD
from unittest import TestCase
from Card import Card
from DeckOfCards import DeckOfCards

class TestDeckOfCards(TestCase):
    def setUp(self):
        print("The Setup")
        self.card = Card(1, 10)
        self.deck = DeckOfCards()

    # Test the list of cards created in the init
    def test__init__list_valid(self):
        # Test if the list has 52 cards
        self.assertEqual(len(self.deck.cards_pack), 52)
        # Test if the values in the list are cards and if we indeed get a list
        self.assertTrue(type(self.deck.cards_pack[0]) == Card)
        self.assertTrue(type(self.deck.cards_pack) == list)
        # Tests highest and lowest cards in the list
        card = Card(1,1)
        self.assertEqual(self.deck.cards_pack[0], card)
        card = Card(4,13)
        self.assertEqual(self.deck.cards_pack[51], card)
        # Test for the entire list
        cards_list = []
        for suit in range(1,5):
            for value in range(1,14):
                card = Card(suit, value)
                cards_list.append(card)
        self.assertEqual(self.deck.cards_pack, cards_list)

    # Test if the function  shuffle the list
    def test_cards_shuffle(self):
        cards_list = self.deck.cards_pack.copy()
        self.deck.cards_shuffle()
        print(cards_list)
        print(self.deck.cards_pack)
        # Test the entire pack
        self.assertNotEqual(cards_list, self.deck.cards_pack)
        # Test the first and last card in the shuffled pack and the sorted pack
        self.assertNotEqual(cards_list[0], self.deck.cards_pack[0])
        self.assertNotEqual(cards_list[51], self.deck.cards_pack[51])

    # Test for the deal one function
    def test_deal_one(self):
        print(len(self.deck.cards_pack))
        # Test if the function returns a card
        self.assertTrue(type(self.deck.deal_one()) == Card)

    # Test if the pack loses a card with deal one function
    def test_deal_one_card_down(self):
        card = self.deck.deal_one()
        # Test if the dealt card is not in the pack
        self.assertNotIn(card, self.deck.cards_pack)
        # Test if the card if deal one function reduces the list in one card
        self.assertEqual(len(self.deck.cards_pack), 51)

=======
from unittest import TestCase
from Card import Card
from DeckOfCards import DeckOfCards

class TestDeckOfCards(TestCase):
    def setUp(self):
        print("The Setup")
        self.card = Card(1, 10)
        self.deck = DeckOfCards()

    # Test the list of cards created in the init
    def test__init__list_valid(self):
        # Test if the list has 52 cards
        self.assertEqual(len(self.deck.cards_pack), 52)
        # Test if the values in the list are cards and if we indeed get a list
        self.assertTrue(type(self.deck.cards_pack[0]) == Card)
        self.assertTrue(type(self.deck.cards_pack) == list)
        # Tests highest and lowest cards in the list
        card = Card(1,1)
        self.assertEqual(self.deck.cards_pack[0], card)
        card = Card(4,13)
        self.assertEqual(self.deck.cards_pack[51], card)
        # Test for the entire list
        cards_list = []
        for suit in range(1,5):
            for value in range(1,14):
                card = Card(suit, value)
                cards_list.append(card)
        self.assertEqual(self.deck.cards_pack, cards_list)

    # Test if the function  shuffle the list
    def test_cards_shuffle(self):
        cards_list = self.deck.cards_pack.copy()
        self.deck.cards_shuffle()
        print(cards_list)
        print(self.deck.cards_pack)
        # Test the entire pack
        self.assertNotEqual(cards_list, self.deck.cards_pack)
        # Test the first and last card in the shuffled pack and the sorted pack
        self.assertNotEqual(cards_list[0], self.deck.cards_pack[0])
        self.assertNotEqual(cards_list[51], self.deck.cards_pack[51])

    # Test for the deal one function
    def test_deal_one(self):
        print(len(self.deck.cards_pack))
        # Test if the function returns a card
        self.assertTrue(type(self.deck.deal_one()) == Card)

    # Test if the pack loses a card with deal one function
    def test_deal_one_card_down(self):
        card = self.deck.deal_one()
        # Test if the dealt card is not in the pack
        self.assertNotIn(card, self.deck.cards_pack)
        # Test if the card if deal one function reduces the list in one card
        self.assertEqual(len(self.deck.cards_pack), 51)

>>>>>>> 85be426bae901abedf8a32c86f567ccc2bc9f80a
