'''Module for all calculations'''

def calculate_circle_area(radius):
    """
    Caculates the area of a circle given its radius

    """
    pi = 3.14159
    area = pi * radius ** 2
    return area

radius = 5 
circle_area = calculate_circle_area(radius)
print("Area of the circle:", circle_area)