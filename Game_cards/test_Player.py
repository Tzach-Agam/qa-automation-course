<<<<<<< HEAD
from unittest import TestCase, mock
from Card import Card
from DeckOfCards import DeckOfCards
from Player import Player

class TestPlayer(TestCase):
    def setUp(self):
        print("The Setup")
        self.deck = DeckOfCards()
        self.player = Player("Dani",10)

    # Test all valid cases of init in player
    def test__init__valid(self):
        self.assertEqual(self.player.name, "Dani")
        self.assertEqual(self.player.dealt_cards, 10)
        self.assertEqual(self.player.player_cards, [])

    # Test invalid cases of init in player with wrong parameters
    def test__init__invalid(self):
        with self.assertRaises(TypeError):
            invalid_player = Player(1, 10)
        with self.assertRaises(TypeError):
            invalid_player = Player("Dani", "abc")
        # Test invalid name
        with self.assertRaises(TypeError):
            invalid_player = Player("Dani1")

    # Test all defaults __init__
    def test__init__default(self):
        # Test if the default is 26
        player1 = Player("Shimi")
        self.assertEqual(player1.dealt_cards, 26)
        # Test when the default dealt cards is lower than 10 or bigger than 26
        player2 = Player("Shimi",27)
        self.assertEqual(player2.dealt_cards, 26)
        player3 = Player("Shimi",9)
        self.assertEqual(player3.dealt_cards, 26)

    # Test invalid parameter for set hand
    def test_set_hand_invalid(self):
        with self.assertRaises(TypeError):
            self.player.set_hand("abc")
            self.player.set_hand([1, 2, 3])

    # Test if the function sets a pack with the card given to it
    @mock.patch('DeckOfCards.DeckOfCards.deal_one', return_value= Card(1, 10))
    def test_set_hand(self, mock_deal_one):
        card1 = Card(1, 10)
        self.player.set_hand(self.deck)
        # Test if the card is in the pack
        self.assertIn(card1, self.player.player_cards)
        # Test if the card is in the list the 10 times
        self.assertEqual(self.player.player_cards[0], card1)
        self.assertEqual(self.player.player_cards[9], card1)

    # Test if the function sets a pack with the number of cards given to it
    def test_set_hand_pack_len(self):
        self.player.set_hand(self.deck)
        self.assertEqual(len(self.player.player_cards), 10)

    # Test if the function doesn't give cards when there aren't enough
    def test_set_hand_no_cards(self):
        with self.assertRaises(TypeError):
            self.deck.cards_pack = self.deck.cards_pack[:9]
            self.player.set_hand(self.deck)
        with self.assertRaises(TypeError):
            self.deck.cards_pack = []
            self.player.set_hand(self.deck)

    # Test if the function returns a card
    def test_get_card(self):
        self.player.set_hand(self.deck)
        self.assertTrue(type(self.player.get_card()) == Card)

    # Test if the function makes the pack to lose a card
    def test_get_card_card_down(self):
        self.player.set_hand(self.deck)
        print(len(self.player.player_cards))
        # Test if the dealt card is not in the pack
        card = self.player.get_card()
        self.assertNotIn(card, self.player.player_cards)
        # Test if the get card function reduce the number of cards in the pack
        self.assertEqual(len(self.player.player_cards), 9)

    # Test if the function adds a card to the player's pack
    def test_add_card(self):
        self.player.set_hand(self.deck)
        card = Card(1,10)
        self.player.add_card(card)
        # Test if the card is in the pack
        self.assertIn(card, self.player.player_cards)
        # Test if the pack has one more card
        self.assertEqual(len(self.player.player_cards), 11)



=======
from unittest import TestCase, mock
from Card import Card
from DeckOfCards import DeckOfCards
from Player import Player

class TestPlayer(TestCase):
    def setUp(self):
        print("The Setup")
        self.deck = DeckOfCards()
        self.player = Player("Dani",10)

    # Test all valid cases of init in player
    def test__init__valid(self):
        self.assertEqual(self.player.name, "Dani")
        self.assertEqual(self.player.dealt_cards, 10)
        self.assertEqual(self.player.player_cards, [])

    # Test invalid cases of init in player with wrong parameters
    def test__init__invalid(self):
        with self.assertRaises(TypeError):
            invalid_player = Player(1, 10)
        with self.assertRaises(TypeError):
            invalid_player = Player("Dani", "abc")
        # Test invalid name
        with self.assertRaises(TypeError):
            invalid_player = Player("Dani1")

    # Test all defaults __init__
    def test__init__default(self):
        # Test if the default is 26
        player1 = Player("Shimi")
        self.assertEqual(player1.dealt_cards, 26)
        # Test when the default dealt cards is lower than 10 or bigger than 26
        player2 = Player("Shimi",27)
        self.assertEqual(player2.dealt_cards, 26)
        player3 = Player("Shimi",9)
        self.assertEqual(player3.dealt_cards, 26)

    # Test invalid parameter for set hand
    def test_set_hand_invalid(self):
        with self.assertRaises(TypeError):
            self.player.set_hand("abc")
            self.player.set_hand([1, 2, 3])

    # Test if the function sets a pack with the card given to it
    @mock.patch('DeckOfCards.DeckOfCards.deal_one', return_value= Card(1, 10))
    def test_set_hand(self, mock_deal_one):
        card1 = Card(1, 10)
        self.player.set_hand(self.deck)
        # Test if the card is in the pack
        self.assertIn(card1, self.player.player_cards)
        # Test if the card is in the list the 10 times
        self.assertEqual(self.player.player_cards[0], card1)
        self.assertEqual(self.player.player_cards[9], card1)

    # Test if the function sets a pack with the number of cards given to it
    def test_set_hand_pack_len(self):
        self.player.set_hand(self.deck)
        self.assertEqual(len(self.player.player_cards), 10)

    # Test if the function doesn't give cards when there aren't enough
    def test_set_hand_no_cards(self):
        with self.assertRaises(TypeError):
            self.deck.cards_pack = self.deck.cards_pack[:9]
            self.player.set_hand(self.deck)
        with self.assertRaises(TypeError):
            self.deck.cards_pack = []
            self.player.set_hand(self.deck)

    # Test if the function returns a card
    def test_get_card(self):
        self.player.set_hand(self.deck)
        self.assertTrue(type(self.player.get_card()) == Card)

    # Test if the function makes the pack to lose a card
    def test_get_card_card_down(self):
        self.player.set_hand(self.deck)
        print(len(self.player.player_cards))
        # Test if the dealt card is not in the pack
        card = self.player.get_card()
        self.assertNotIn(card, self.player.player_cards)
        # Test if the get card function reduce the number of cards in the pack
        self.assertEqual(len(self.player.player_cards), 9)

    # Test if the function adds a card to the player's pack
    def test_add_card(self):
        self.player.set_hand(self.deck)
        card = Card(1,10)
        self.player.add_card(card)
        # Test if the card is in the pack
        self.assertIn(card, self.player.player_cards)
        # Test if the pack has one more card
        self.assertEqual(len(self.player.player_cards), 11)



>>>>>>> 85be426bae901abedf8a32c86f567ccc2bc9f80a
