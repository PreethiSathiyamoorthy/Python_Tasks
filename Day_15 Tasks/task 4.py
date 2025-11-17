import math

#parent class or base class

class shape:
    def area(self):
        return 0
    def perimter(self):
        return 0
#subclass or child class    
    
    class circle:
        def area (self,r):
            A=math.pi*(r**2)
            return A
        def perimeter(self,r):
            c=2*math.pi*r
            return c
    class triangle:
        def area(self,b,h):
            A=(1/2)*b*h
            return A
        def perimeter(self,a,b,c):
            p=a+b+c
            return p
    class square:
        def area(self,a):
            A=a**2
            return A
        def perimeter(self,a):
            p=4*a
            return p
obj1=shape.circle()
a=int(input("Enter the r value of circle:"))
print("Area of circle:",obj1.area(a))
print("permeter of circle:",obj1.perimeter(a))
obj2=shape.triangle()
b=int(input("Enter the l value of triangle:"))
h=int(input("Enter the b value of triangle:"))
print("area of triangle:",obj2.area(b,h))
a=int(input("Enter the a value of triangle:"))
b=int(input("Enter the b value of triangle:"))
c=int(input("Enter the c value of triangle:"))
print("perimeter of triangle:",obj2.perimeter(a,b,c))
obj3=shape.square()
a=int(input("Enter the a value of square:"))
print("area of square:",obj3.area(a))
print("perimeter of square:",obj3.perimeter(a))


        
        
    
