import math

class Point:
    """Class Point representing a coordinate point"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def read_point(p):
    p.x = float(input("x coordinate: "))
    p.y = float(input("y coordinate: "))

def print_point(p):
    print("(%g, %g)" % (p.x, p.y))

def distance(p1, p2):
    d = math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
    return d

# Create first object and read x and y for p1
p1 = Point()
print("Enter First point:")
read_point(p1)

# Create second object and read x and y for p2
p2 = Point()
print("Enter Second point:")
read_point(p2)

# Compute distance between p1 and p2
dist = distance(p1, p2)

# Print the points and the distance
print("First point is:")
print_point(p1)
print("Second point is:")
print_point(p2)
print("Distance is: %g" % dist)