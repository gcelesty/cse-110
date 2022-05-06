# area of square
sqr = float(input("\nWhat is the length of a side of the square (in cm)? "))
sqr_area = sqr ** 2
print(f"The area of the square is: {sqr_area} cm^2")
print(f"The area of the square is: {sqr_area / 10000} m^2\n")

# area of rectangle
rec_len = float(input("What is the length of the rectangle (in cm)? "))
rec_wid = float(input("What is the width of the rectangle (in cm)? "))
rec_area = rec_len * rec_wid
print(f"The area of the rectangle is: {rec_area} cm^2")
print(f"The area of the rectangle is: {rec_area / 10000} m^2\n")

# area of a circle
cir = float(input("What is the radius of the circle (in cm)? "))
import math
cir_area = math.pi * (cir ** 2)
print(f"The area of the circle is: {cir_area} cm^2")
print(f"The area of the circle is: {cir_area / 10000} m^2")

# volume of a cube with square side
cube = sqr ** 3
print(f"\nThe volume of the cube is: {cube} cm^3")

# volume of a sphere with that given radius
sphere = (4 / 3) * math.pi * (cir ** 3)
print(f"The volume of the sphere is: {sphere} cm^3\n")
