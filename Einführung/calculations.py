'''Module for all calculations'''

def calculate_circle_area(radius):
    """
    Caculates the area of a circle given its radius

    """
    pi = 3.14159
    area = pi * radius ** 2
    return area

RADIUS = 5
CIRCLE_AREA = calculate_circle_area(RADIUS)
print("Area of the circle:", CIRCLE_AREA)
