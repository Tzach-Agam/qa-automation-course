<<<<<<< HEAD
from unittest import TestCase
from Card import Card
from CardGame import CardGame

class TestCardGame(TestCase):
    def setUp(self):
        print("The setup")
        self.game = CardGame("Dani", "Shimi", 10)

    # Test valid parameters for init
    def test__init__valid(self):
        self.assertEqual(self.game.player1.name, "Dani")
        self.assertEqual(self.game.player2.name, "Shimi")
        self.assertEqual(self.game.dealt_cards, 10)

    # Test invalid parameters for init
    def test__init__invalid(self):
        with self.assertRaises(TypeError):
            invalid_game = CardGame(1, "Shimi")
        with self.assertRaises(TypeError):
            invalid_game = CardGame("Dani", 1)
        with self.assertRaises(TypeError):
            invalid_game = CardGame("Dani", "Shimi", "abc")
        with self.assertRaises(TypeError):
            invalid_game = CardGame("Dani2", "Shimi")
        with self.assertRaises(TypeError):
            invalid_game = CardGame("Dani", "Shimi2")

    # Test default dealt cards in init
    def test__init__default(self):
        game = CardGame("Dani","Shimi")
        self.assertEqual(game.dealt_cards, 26)
        # Test when the default dealt cards is lower than 10 or bigger than 26
        game = CardGame("Dani","Shimi", 27)
        self.assertEqual(game.dealt_cards, 26)
        game = CardGame("Dani","Shimi", 9)
        self.assertEqual(game.dealt_cards, 26)

    # Test if each player gets a pack of shuffled cards with the same amount and according to what they wanted
    def test_new_game(self):
        # Test if each player gets the same number of dealt cards (10 in this case)
        self.assertEqual(len(self.game.player1.player_cards), 10)
        self.assertEqual(len(self.game.player2.player_cards), 10)
        # Another option to see if the number of dealt cards is equal
        self.assertEqual(len(self.game.player1.player_cards), len(self.game.player2.player_cards))

    # Test if the program doesnt allow to start a new game after a game started
    def test_new_game_invalid(self):
        with self.assertRaises(TypeError):
            self.game.new_game()

    # Test get winner function in case of win for each side and a tie
    def test_get_winner(self):
        # Test player1 won
        self.game.player1.add_card(Card(1, 2))
        self.assertEqual(self.game.get_winner(), f"The winner in the game is {self.game.player1.name}!!!")
        # Test player2 won
        self.game.player2.add_card(Card(1, 2))
        self.game.player2.add_card(Card(1, 3))
        self.assertEqual(self.game.get_winner(), f"The winner in the game is {self.game.player2.name}!!!")
        # Test a tie
        self.game.player1.add_card(Card(1,4))
        self.assertEqual(self.game.get_winner(), None)


=======
from unittest import TestCase
from Card import Card
from CardGame import CardGame

class TestCardGame(TestCase):
    def setUp(self):
        print("The setup")
        self.game = CardGame("Dani", "Shimi", 10)

    # Test valid parameters for init
    def test__init__valid(self):
        self.assertEqual(self.game.player1.name, "Dani")
        self.assertEqual(self.game.player2.name, "Shimi")
        self.assertEqual(self.game.dealt_cards, 10)

    # Test invalid parameters for init
    def test__init__invalid(self):
        with self.assertRaises(TypeError):
            invalid_game = CardGame(1, "Shimi")
        with self.assertRaises(TypeError):
            invalid_game = CardGame("Dani", 1)
        with self.assertRaises(TypeError):
            invalid_game = CardGame("Dani", "Shimi", "abc")
        with self.assertRaises(TypeError):
            invalid_game = CardGame("Dani2", "Shimi")
        with self.assertRaises(TypeError):
            invalid_game = CardGame("Dani", "Shimi2")

    # Test default dealt cards in init
    def test__init__default(self):
        game = CardGame("Dani","Shimi")
        self.assertEqual(game.dealt_cards, 26)
        # Test when the default dealt cards is lower than 10 or bigger than 26
        game = CardGame("Dani","Shimi", 27)
        self.assertEqual(game.dealt_cards, 26)
        game = CardGame("Dani","Shimi", 9)
        self.assertEqual(game.dealt_cards, 26)

    # Test if each player gets a pack of shuffled cards with the same amount and according to what they wanted
    def test_new_game(self):
        # Test if each player gets the same number of dealt cards (10 in this case)
        self.assertEqual(len(self.game.player1.player_cards), 10)
        self.assertEqual(len(self.game.player2.player_cards), 10)

    # Test if the program doesnt allow to start a new game after a game started
    def test_new_game_invalid(self):
        with self.assertRaises(TypeError):
            self.game.new_game()

    # Test get winner function in case of win for each side and a tie
    def test_get_winner(self):
        # Test player1 won
        self.game.player1.add_card(Card(1, 2))
        self.assertEqual(self.game.get_winner(), f"The winner in the game is {self.game.player1.name}!!!")
        # Test player2 won
        self.game.player2.add_card(Card(1, 2))
        self.game.player2.add_card(Card(1, 3))
        self.assertEqual(self.game.get_winner(), f"The winner in the game is {self.game.player2.name}!!!")
        # Test a tie
        self.game.player1.add_card(Card(1,4))
        self.assertEqual(self.game.get_winner(), None)


>>>>>>> 85be426bae901abedf8a32c86f567ccc2bc9f80a
