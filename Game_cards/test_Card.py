<<<<<<< HEAD
from unittest import TestCase
from Card import Card

class TestCard(TestCase):
    def setUp(self):
        print("The Setup")
        self.card = Card(1, 10)

    # Test all valid cases of init in card
    def test__init__valid(self):
        self.assertEqual(self.card.suit, 1)
        self.assertEqual(self.card.value, 10)

    # Test invalid cases of init with wrong parameters types
    def test__init__invalid(self):
        with self.assertRaises(TypeError):
            invalid_card = Card("abc", 10)
        with self.assertRaises(TypeError):
            invalid_card = Card(1, "abc")

    # Test invalid parameters in init
    def test_invalid__init__parameters(self):
        with self.assertRaises(TypeError):
            invalid_card = Card(5, 10)
        with self.assertRaises(TypeError):
            invalid_card = Card(0, 10)
        with self.assertRaises(TypeError):
            invalid_card = Card(1, 14)
        with self.assertRaises(TypeError):
            invalid_card = Card(1, 0)

    # Test __gt__ function with wrong parameter type for other
    def test__gt__wrong_parameters(self):
        with self.assertRaises(TypeError):
            card1 = Card(1, 1)
            card2 = [1,2,3]
            self.assertTrue(card1 > card2)

    # Test __gt__ function True
    def test__gt__True(self):
        # The same suit and different value
        card1 = Card(1, 1)
        card2 = Card(1, 13)
        self.assertTrue(card1 > card2)
        # Different suit and different value
        card1 = Card(1, 13)
        card2 = Card(2, 12)
        self.assertTrue(card1 > card2)
        # Different value and same suit
        card1 = Card(2, 1)
        card2 = Card(1, 1)
        self.assertTrue(card1 > card2)

    # Test __gt__ function False
    def test__gt__False(self):
        # General test to see when program returns False with the highest cards
        card1 = Card(4, 1)
        card2 = Card(4, 13)
        self.assertFalse(card2 > card1)
        # The cards are equal in suit and value
        card1 = Card(1, 1)
        card2 = Card(1, 1)
        self.assertFalse(card2 > card1)
        self.assertFalse(card2 < card1)

    # Test __eq__ function with wrong parameter type for other
    def test__eq__wrong_parameters(self):
        with self.assertRaises(TypeError):
            card1 = Card(1, 1)
            card2 = [1, 2, 3]
            self.assertTrue(card1 == card2)

    # Test __eq__ function True
    def test__eq__True(self):
        card = Card(1, 10)
        self.assertTrue(self.card == card)

    # Test __eq__ function False
    def test__eq__False(self):
        card = Card(2, 10)
        self.assertFalse(self.card == card)
        card = Card(1, 9)
        self.assertFalse(self.card == card)


=======
from unittest import TestCase
from Card import Card

class TestCard(TestCase):
    def setUp(self):
        print("The Setup")
        self.card = Card(1, 10)

    # Test all valid cases of init in card
    def test__init__valid(self):
        self.assertEqual(self.card.suit, 1)
        self.assertEqual(self.card.value, 10)

    # Test invalid cases of init with wrong parameters types
    def test__init__invalid(self):
        with self.assertRaises(TypeError):
            invalid_card = Card("abc", 10)
        with self.assertRaises(TypeError):
            invalid_card = Card(1, "abc")

    # Test invalid parameters in init
    def test_invalid__init__parameters(self):
        with self.assertRaises(TypeError):
            invalid_card = Card(5, 10)
        with self.assertRaises(TypeError):
            invalid_card = Card(0, 10)
        with self.assertRaises(TypeError):
            invalid_card = Card(1, 14)
        with self.assertRaises(TypeError):
            invalid_card = Card(1, 0)

    # Test __gt__ function with wrong parameter type for other
    def test__gt__wrong_parameters(self):
        with self.assertRaises(TypeError):
            card1 = Card(1, 1)
            card2 = [1,2,3]
            self.assertTrue(card1 > card2)

    # Test __gt__ function True
    def test__gt__True(self):
        # The same suit and different value
        card1 = Card(1, 1)
        card2 = Card(1, 13)
        self.assertTrue(card1 > card2)
        # Different suit and different value
        card1 = Card(1, 13)
        card2 = Card(2, 12)
        self.assertTrue(card1 > card2)
        # Different value and same suit
        card1 = Card(2, 1)
        card2 = Card(1, 1)
        self.assertTrue(card1 > card2)

    # Test __gt__ function False
    def test__gt__False(self):
        # General test to see when program returns False with the highest cards
        card1 = Card(4, 1)
        card2 = Card(4, 13)
        self.assertFalse(card2 > card1)
        # The cards are equal in suit and value
        card1 = Card(1, 1)
        card2 = Card(1, 1)
        self.assertFalse(card2 > card1)
        self.assertFalse(card2 < card1)

    # Test __eq__ function with wrong parameter type for other
    def test__eq__wrong_parameters(self):
        with self.assertRaises(TypeError):
            card1 = Card(1, 1)
            card2 = [1, 2, 3]
            self.assertTrue(card1 == card2)

    # Test __eq__ function True
    def test__eq__True(self):
        card = Card(1, 10)
        self.assertTrue(self.card == card)

    # Test __eq__ function False
    def test__eq__False(self):
        card = Card(2, 10)
        self.assertFalse(self.card == card)
        card = Card(1, 9)
        self.assertFalse(self.card == card)


>>>>>>> 85be426bae901abedf8a32c86f567ccc2bc9f80a
