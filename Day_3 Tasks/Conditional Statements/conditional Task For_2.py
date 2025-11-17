side1 = float(input("Enter length of 1 side :"))
side2 = float(input("Enter length of 2 side :"))
side3 = float(input("Enter length of 3 side :"))

if (side1+side2>side3)and(side2+side3>side1)and(side1+side3 > side2):
    if side1== side2== side3:
        print("Equilateral triangle")
    elif side1== side2 or side2==side3 or side1==side3:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("The sides do not form a valid triangle")
    
