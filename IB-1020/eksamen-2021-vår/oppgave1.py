from math import pi

# a)
def shaded_area(r):
    diameter = 2*r
    area_square = diameter ** 2
    area_circle = pi * r * r
    area_shaded = area_square - area_circle
    return area_shaded

# b)
radius = 2
while (shaded_area(radius)) < 100:
    radius += 1
print(radius)