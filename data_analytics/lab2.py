class A:
    _x = 5  # Protected variable

class B(A):
    def __init__(self, y):
        self._y = y  # Initialize the instance variable _y

    def add(self, other):
        return self._y + other._x  # Accessing _x from class A

    def display(self):
        print(f"x = {self._x}, y = {self._y}")  # Properly formatted print statement

# Creating objects
obj1 = B(5)
obj2 = B(6)

# Displaying the values of obj1 and obj2
obj1.display()
obj2.display()

# Adding obj2._y to obj1._x
print(obj2.add(obj1))  # Accesses the values and prints the sum
