# Εισάγουμε την κλάση ABC και τον διακοσμητή abstractmethod από την βιβλιοθήκη abc.
# Η βιβλιοθήκη abc μας επιτρέπει να δημιουργήσουμε abstract base classes (ΑΒC), δηλαδή κλάσεις
# που δεν μπορούν να δημιουργηθούν άμεσα και απαιτούν από τις υποκλάσεις να υλοποιήσουν
# κάποιες μεθόδους.
from abc import ABC, abstractmethod

# Εισάγουμε την βιβλιοθήκη math, η οποία περιέχει μαθηματικές συναρτήσεις και σταθερές.
# Χρησιμοποιούμε την math για να υπολογίσουμε την τιμή του π (π) με τη σταθερά math.pi,
# η οποία είναι πιο ακριβής και αξιόπιστη από το να ορίσουμε το π χειροκίνητα.
import math

# 1. Abstract Class Shape (Geometric Shape)
# This is the abstract base class that will define the structure for all shapes.
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

# 2. Subclass Circle (Circle)
# This class inherits from Shape and implements the methods for calculating area and perimeter for a circle.
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # Attribute to store the radius of the circle

    def area(self):
        # Area of a circle: π * r²
        return math.pi * self.radius ** 2

    def perimeter(self):
        # Perimeter (circumference) of a circle: 2 * π * r
        return 2 * math.pi * self.radius

# 3. Subclass Rectangle (Rectangle)
# This class inherits from Shape and implements the methods for calculating area and perimeter for a rectangle.
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width  # Attribute to store the width of the rectangle
        self.height = height  # Attribute to store the height of the rectangle

    def area(self):
        # Area of a rectangle: width * height
        return self.width * self.height

    def perimeter(self):
        # Perimeter of a rectangle: 2 * (width + height)
        return 2 * (self.width + self.height)

# 4. Subclass Triangle (Triangle)
# This class inherits from Shape and implements the methods for calculating area and perimeter for a triangle.
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base  # Attribute to store the base of the triangle
        self.height = height  # Attribute to store the height of the triangle

    def area(self):
        # Area of a triangle: 0.5 * base * height
        return 0.5 * self.base * self.height

    def perimeter(self):
        # Perimeter calculation for the triangle (with 3 sides)
        # Here, we assume the triangle is equilateral for simplicity
        side_length = self.base  # For simplicity, assuming all sides are equal
        return 3 * side_length  # Perimeter for an equilateral triangle is 3 * side length

# 5. Testing the Shapes

# Create a Circle object with a radius of 5
circle = Circle(5)
print("Circle Area:", circle.area())        # Print the area of the circle
print("Circle Perimeter:", circle.perimeter())  # Print the perimeter (circumference) of the circle

# Create a Rectangle object with width 4 and height 6
rectangle = Rectangle(4, 6)
print("\nRectangle Area:", rectangle.area())        # Print the area of the rectangle
print("Rectangle Perimeter:", rectangle.perimeter())  # Print the perimeter of the rectangle

# Create a Triangle object with base 6 and height 8
triangle = Triangle(6, 8)
print("\nTriangle Area:", triangle.area())        # Print the area of the triangle
print("Triangle Perimeter:", triangle.perimeter())  # Print the perimeter of the triangle
