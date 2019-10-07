def cone(radius, height):
    r = radius
    if r <= 0:
        raise ValueError("Error: Radius must be positive.")
    elif type(r) != int:
        raise TypeError("Error: Parameter radius and height must be numeric"):
    h = height
    if h <= 0:
        raise ValueError("Error: Height must be positive."):
    elif type(r) != int:
        raise TypeError("Error: Parameter radius and height must be numeric"):
    V = 3.1415 * (r ** 2) * (h/3)
    return V

except Value


print(cone(2,3))