# Cylinder surface area and volume
import math

r = float(input("Enter cylinder radius r: "))
h = float(input("Enter cylinder height h: "))

lateral_area = 2 * math.pi * r * h
total_area = lateral_area + 2 * math.pi * r**2  # = 2πrh + 2πr^2
volume = math.pi * r**2 * h

print(f"Lateral surface area = {lateral_area}")
print(f"Total surface area = {total_area}")
print(f"Volume = {volume}")
