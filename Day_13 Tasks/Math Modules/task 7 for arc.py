import math
radius = float(input("Enter the radius of the circle: "))#arc=r*degree
angle_deg = float(input("Enter the angle in degrees: "))

# Convert degrees to radians
angle_rad = math.radians(angle_deg)  #math.radians converts degrees to radians

# Calculate arc length
arc_length = radius * angle_rad     
print("Arc length of the angle is:", arc_length)
