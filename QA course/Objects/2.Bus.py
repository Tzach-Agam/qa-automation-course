class Bus:
    def __init__(self, number_of_sits):
        self.number_of_sits = number_of_sits
        self.sits_list = []
        self.current_people_num = 0
        for sit in range(number_of_sits):
            self.sits_list.append("free")

    def __str__(self):
        return f"All bus data:number of sits: {self.number_of_sits}\n" \
               f"list of sits: {self.sits_list}\n" \
               f"number of people currently on the bus: {self.current_people_num} "

    def getOn(self, name):
        for sit in range(len(self.sits_list)):
            if self.sits_list[sit] == "free":
                self.sits_list[sit] = name
                self.current_people_num += 1
                break
        else:
            print(f"bus is full. {name} did not have a place")

    def getOff(self, name):
        for sit in range(len(self.sits_list)):
            if self.sits_list[sit] == name:
                self.sits_list[sit] = "free"
                self.current_people_num -= 1
                break
        else:
            print(f"{name} is not in the bus")

The_Bus = Bus(10)
activity = int(input("enter activity number: "))
while activity != 0:
    if activity == 1:
        name = input("enter a name: ")
        The_Bus.getOn(name)
    elif activity == 2:
        name = input("enter a name: ")
        The_Bus.getOff(name)
    activity = int(input("enter activity number: "))
print(The_Bus)







