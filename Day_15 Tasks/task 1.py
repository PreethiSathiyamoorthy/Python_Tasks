import math
class circle:
    def area(self,r):
        A=math.pi*(r**2)
        return A
           
    def perimeter(self,r):
        c=2*math.pi*r
        return c
obj = circle ()
a=int(input("Enter the value:"))
print(obj.area(a))
print(obj.perimeter(a))
      
    
    
