# Function polymorphism example

def add(x, y, z=0):
    return x + y + z

# Calling the same function in different ways
print("Sum of two numbers:", add(5, 10))
print("Sum of three numbers:", add(5, 10, 15))
print("Sum of strings:", add("Hello ", "World"))



#another example

class shape:
    def area(self):
        pass
class square(shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side*self.side
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
shape=(square(2),circle(5))
for i in shape:
    print(i.area())
