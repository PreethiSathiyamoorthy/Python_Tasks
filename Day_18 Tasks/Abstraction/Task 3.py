from abc import ABC, abstractmethod
import math

# Abstract class
class Shapes(ABC):
    @abstractmethod
    def volume(self):
        pass

# Subclass 1
class Cylinder(Shapes):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return math.pi * self.radius**2 * self.height

# Subclass 2
class Cone(Shapes):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return (1/3) * math.pi * self.radius**2 * self.height

# Subclass 3
class Sphere(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        return (4/3) * math.pi * self.radius**3

# Create objects
cylinder = Cylinder(3, 7)
cone = Cone(3, 7)
sphere = Sphere(4)
#create call function
cylinder.volume()
cone.volume()
sphere.volume()

# Print results
print("Cylinder Volume:", cylinder.volume())
print("Cone Volume:", cone.volume())
print("Sphere Volume:", sphere.volume())
print()


#another method 2

from abc import ABC, abstractmethod
import math

# Abstract class
class Shapes(ABC):
    @abstractmethod
    def volume(self):
        pass
# Subclass 1 - Cylinder
class Cylinder(Shapes):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return math.pi * self.radius**2 * self.height
# Subclass 2 - Cone
class Cone(Shapes):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return (1/3) * math.pi * self.radius**2 * self.height
# Subclass 3 - Sphere
class Sphere(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        return (4/3) * math.pi * self.radius**3
   
# --- User Input Section ---
print("Choose Shape: 1.Cylinder  2.Cone  3.Sphere")
choice = int(input("Enter your choice (1, 2, or 3): "))

if choice == 1:
    r = float(input("Enter radius of the cylinder: "))
    h = float(input("Enter height of the cylinder: "))
    obj2=Cylinder(r,h)
    print("Cylinder Volume = ",obj2.volume())    
elif choice == 2:
    r = float(input("Enter radius of the cone: "))
    h = float(input("Enter height of the cone: "))
    obj3=Cone(r,h)
    print("Cone Volume = ",obj3.volume())
elif choice == 3:
    r = float(input("Enter radius of the sphere: "))
    obj4=Sphere(r)
    print("Sphere Volume = ", obj4.volume())
else:
    print("Invalid choice!")

