import math

# function to compute the area of square, rectangle, circle
def compute_area_square(side):
    area = compute_area_rectangle(side, side)
    return area

def compute_area_rectangle(length, width):
    return length * width

def compute_area_circle(radius):
    return math.pi * radius * radius

def compute_area(shape, value1, value2=0):
    area = -1

    if shape == "square":
        area = compute_area_square(value1)
    elif shape == "circle":
        area = compute_area_circle(value1)
    elif shape == "rectangle":
        area = compute_area_rectangle(value1, value2)

    return area


# the main program starts here
shape = ""

while shape != "quit":
    shape = input("\nWhat shape do you have? ")

    # convert to all lower case to make code simplier to read
    shape = shape.lower()

    if shape == "square":
        side = float(input("WHat is the length of the side? "))
        area = compute_area(shape, side)
        print(f"The area is {area}")
    elif shape == "rectangle":
        length = float(input("What is the length? "))
        width = float(input("What is the width? "))
        area = compute_area(shape, length, width)
        print(f"The area is {area}")
    elif shape == "circle":
        radius = float(input("What is the radius? "))
        area = compute_area(shape, radius)
        print(f"The area is {area}")