class Animal:
    def __init__(self, name, hunger = 5, energy = 5):
        self.name = name
        self.hunger = hunger
        self.energy = energy

    def __str__(self):
        return f"All animal info: name: {self.name}\n" \
               f"level of hunger: {self.hunger}\n" \
               f"level of energy: {self.energy}"

    def eat(self, food_amount):
        hunger_change = food_amount // 50
        if self.hunger - hunger_change < 0:
            self.hunger = 0
            print("The animal is satisfied but did not finish the food")
        else:
            self.hunger -= hunger_change
        energy_change = food_amount // 100
        if self.energy - energy_change < 0:
            self.energy = 0
        else:
            self.energy -= energy_change

    def play(self, play_time):
        energy_change = play_time // 10
        if self.energy - (energy_change * 2) < 0:
            self.energy = 0
            print("The game ended because the animal is tired")
        else:
            self.energy -= (energy_change * 2)
        hunger_change = play_time // 10
        if self.hunger + (hunger_change * 2) > 10:
            self.hunger = 10
        else:
            self.hunger += (hunger_change * 2)

    def rest(self, rest_amount):
        energy_change = rest_amount // 20
        if self.energy + energy_change > 10:
            self.energy = 10
            print("The animal finished rest and can play now")
        else:
            self.energy += energy_change
        hunger_change = rest_amount // 30
        if self.hunger + hunger_change > 10:
            self.hunger = 10
            print("The animal finished rest and wants to eat")
        else:
            self.hunger += hunger_change

The_animal = Animal("REXI")
activity = int(input("enter number of activity: "))
while activity != 0:
    if activity == 1:
        The_animal.eat(100)
        print(The_animal)
    elif activity == 2:
        The_animal.play(20)
        print(The_animal)
    elif activity == 3:
        The_animal.rest(30)
        print(The_animal)
    activity = int(input("enter number of activity: "))









