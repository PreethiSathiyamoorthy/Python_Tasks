from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# Subclass 1
class Lion(Animal):
    def sound(self):
        return "Lion roars"

# Subclass 2
class Tiger(Animal):
    def sound(self):
        return "Tiger growls"

# Create objects
lion = Lion()
tiger = Tiger()

# Call methods
lion.sound()
tiger.sound()
print("The Lion Sound is :",lion.sound())
print("The Tiger Sound is :",tiger.sound())
