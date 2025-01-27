class Rectangle:  # Base class
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

"""The Rectangle class can be used as a base class for defining a Square class, as a square is a special case of rectangle."""

class Square(Rectangle):  # Derived class
    def __init__(self, s):
        super().__init__(s, s)  # Call parent constructor, w and h are both s
        self.s = s

# Creating instances
r = Rectangle(3, 4)  # Creating instance of Rectangle
s = Square(2)  # Creating instance of Square

# Printing results
print("Area of rectangle:", r.area())
print("Perimeter of rectangle:", r.perimeter())

print("Area of square:", s.area())
print("Perimeter of square:", s.perimeter())