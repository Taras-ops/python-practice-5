def calculate_rectangle_area(length, width):
    return length * width


def calculate_circle_area(radius):
    return 3.14 * radius ** 2


def calculate_triangle_area(base, height):
    return 0.5 * base * height


def calculate_area(shape, *dimensions):
    if shape == 'rectangle':
        return calculate_rectangle_area(*dimensions)
    elif shape == 'circle':
        return calculate_circle_area(*dimensions)
    elif shape == 'triangle':
        return calculate_triangle_area(*dimensions)
    else:
        return 'Not found calculating area function for this shape'


print(calculate_area('rectangle', 10, 20))
print(calculate_area('circle', 10))
print(calculate_area('triangle', 10, 5))
