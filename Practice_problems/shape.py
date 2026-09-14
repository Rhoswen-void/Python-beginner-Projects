class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"The shape is {self.color} in color and is {"filled" if self.is_filled else "not filled" } ")

class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a {self.color} circle with an area of {3.14*(self.radius**2)} sq units")

class Square(Shape):
    def __init__(self,color,is_filled,width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a {self.color} square and it has an area of {self.width**2} sq units")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, base, height):
        super().__init__(color, is_filled)
        self.base = base
        self.height = height

    def describe(self):
        print(f"It is a {self.color} triangle with an area of {0.5*self.height*self.base} sq units")


circle = Circle("Red",True,10)
square = Square("Blue",False,30)
triangle = Triangle("Yellow",True,5,12)

print(square.width)
print(square.color)
print(square.is_filled)
print()
print(circle.radius)
print(circle.color)
print(square.is_filled)
print()
print(triangle.base)
print(triangle.height)
print(triangle.color)
print(triangle.is_filled)
print()
triangle.describe()
circle.describe()
square.describe()