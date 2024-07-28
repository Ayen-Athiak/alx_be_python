import math


# Base Class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override the area() method")


# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


# Function to demonstrate polymorphism
def print_area(shape):
    print(f"The area of the shape is: {shape.area()}")


# Usage
if __name__ == "__main__":
    # Create instances of Rectangle and Circle
    rectangle = Rectangle(5, 3)
    circle = Circle(4)

    # Print areas using the polymorphic function
     # Output: The area of the shape is: 50.26548245743669
