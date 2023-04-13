class Circle:
    def __init__(self, radius):
        self.radius = radius
        import math
        self.pi = math.pi

    def area(self):
        return self.pi * self.radius ** 2

    def perimeter(self):
        return 2 * self.pi * self.radius

    def display(self):
        print("Area of the circle:", self.area())
        print("Perimeter of the circle:", self.perimeter())


shape = Circle(float(input("Value of the Radius: ")))
shape.display()
