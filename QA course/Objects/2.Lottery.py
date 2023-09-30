from random import randint

class Lottery:
    def __init__(self):
        self.low = 1
        self.up = 45
        self.numbers = self.random_numbers()
        self.max_win = self.get_max_winning_sum()

    def random_numbers(self):
        numbers = [randint(self.low, self.up) for i in range(6)]
        return numbers

    def get_max_winning_sum(self):
        win_amount = int(input(" enter max winning amount: "))
        return win_amount

    def show_numbers(self):
        print(self.numbers)

    def check_guess(self, num):
        if num in self.numbers:
            return True
        else:
            return False

    def prize(self, guess_num):
        if guess_num <= 1:
            return 0
        elif 2 <= guess_num <= 5:
            return (self.max_win * guess_num) / 6
        elif guess_num == 6:
            return self.max_win


The_bet = Lottery()
The_bet.show_numbers()
count = 0
for i in range(6):
    guess = int(input("enter a guess between 1-45: "))
    if guess > 45 or guess < 1:
        print("incorrect number! You have failed")
        print("THE PRIZE IS:", The_bet.prize(0))
        break
    elif The_bet.check_guess(guess):
        count += 1
print("THE PRIZE IS:", The_bet.prize(count))

# bugs:
# a player can choose the good guess again and again
# the program will print two different prizes if a player inputs invalid number during the game
