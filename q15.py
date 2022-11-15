"""
15. Write a python program which accepts the radius of a circle from user and computes the area (use math
module)
"""
from math import pi

r = float(input("Enter the radius of the circle: "))
area = pi*r**2

print(f'\nThe area of a circle with {r} unit(s) radius is {area} unit^2')
