class Circle:
    def __init__(self, radius):
        self.PI = 3.14
        self.radius = radius

    def area(self):
        S = self.radius ** 2 * self.PI
        return S

    def circumference(self):
        P = self.radius * 2 * self.PI
        return P

The_circle = Circle(5)
print(The_circle.area())
print(The_circle.circumference())
