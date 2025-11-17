a=float(input("Enter the length of first parallel side a:"))
b=float(input("Enter the length of second parallel side b:"))
h=float(input("Enter the height:"))
sum=(a+b)  #formula of area=a+b/2*h
area=(sum/2)/h
print("Area of trapezoid :",area)



#method 2
import math
a=float(input("Enter the length of first parallel side a:"))
b=float(input("Enter the length of second parallel side b:"))
h=float(input("Enter the height:"))

area=(math.fsum([a,b])/2)*h
print("Area of trapezoid :",area)
