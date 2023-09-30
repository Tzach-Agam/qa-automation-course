class Person:
    def __init__(self, name, age, num_of_children):
        self.name = name
        self.age = age
        self.num_of_children = num_of_children

    def show(self):
        print(f"The details of the person are: "
              f"name- {self.name}, "
              f"age- {self.age}, "
              f"number of children- {self.num_of_children}")

    def has_children(self):
        if self.num_of_children > 0:
            return True
        else:
            return False

    def age_group(self):
        if 0 <= self.age <= 18:
            return "Child"
        elif 19 <= self.age <= 60:
            return "Adult"
        elif 61 <= self.age <= 120:
            return "Senior"
name = input("Enter a name: ")
age = int(input("Enter an age: "))
children = int(input("Enter number of children: "))

The_Person = Person(name, age, children)
The_Person.show()
print(The_Person.has_children())
print(The_Person.age_group())