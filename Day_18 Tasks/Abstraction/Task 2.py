from abc import ABC, abstractmethod
import math

# Abstract class
class Shape(ABC):
    @abstractmethod
    def Area(self):
        pass

    @abstractmethod
    def Perimeter(self):
        pass

# Subclass 1
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return math.pi * self.radius * self.radius

    def Perimeter(self):
        return 2 * math.pi * self.radius

# Subclass 2
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def Area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def Perimeter(self):
        return self.a + self.b + self.c

# Create objects
circle = Circle(5)
triangle = Triangle(3, 4, 5)
#Call methods
circle.Area()
circle.Perimeter()
triangle.Area()
triangle.Perimeter()

# Print results
print("Circle Area:", circle.Area())
print("Circle Perimeter:", circle.Perimeter())

print("Triangle Area:", triangle.Area())
print("Triangle Perimeter:", triangle.Perimeter())
print()


#another example 2

from abc import ABC, abstractmethod
import math

# Abstract class
class Shape(ABC):
    @abstractmethod
    def calculateArea(self):
        pass

    @abstractmethod
    def calculatePerimeter(self):
        pass


# Subclass 1 - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculateArea(self):
        return math.pi * self.radius * self.radius

    def calculatePerimeter(self):
        return 2 * math.pi * self.radius


# Subclass 2 - Triangle
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculateArea(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def calculatePerimeter(self):
        return self.a + self.b + self.c


#User Input Section
print("Choose Shape: 1.Circle  2.Triangle")
choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    r = float(input("Enter radius of the circle: "))
    circle = Circle(r)
    print("\n--- Circle Results ---")
    print("Area:", circle.calculateArea())
    print("Perimeter:", circle.calculatePerimeter())

elif choice == 2:
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))
    triangle = Triangle(a, b, c)
    print("\n--- Triangle Results ---")
    print("Area:", triangle.calculateArea())
    print("Perimeter:", triangle.calculatePerimeter())

else:
    print("Invalid choice!")

