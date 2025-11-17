base=float(input("Enter the base b:"))
height=float(input("Enter the height h:"))
area=base*height
print("Area of paralleogram :",area)



#method 2
import math
base=float(input("Enter the base b:"))
height=float(input("Enter the height h:"))
area=math.prod([b,h])
print("Area of paralleogram :",area)
