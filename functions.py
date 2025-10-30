def validate_age(age):
    """Validate that the age is a positive integer."""
    if not isinstance(age, int):
        raise ValueError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

def calculate_rectangle_area(length, width):
    return length * width
def calculate_circle_area(radius):
    import math
    return math.pi * (radius ** 2 )
def get_area(shape, *args):
    shape = shape.lower().strip()
    if shape not in ['rectangle', 'circle']:
        raise ValueError("Shape must be rectangle or circle")
    if shape == 'rectangle':
        length, width = args
        return calculate_rectangle_area(length, width)
    else:
        radius = args[0]
        return calculate_circle_area(radius)

# print(get_area("rectangle", 5, 10)) 
    