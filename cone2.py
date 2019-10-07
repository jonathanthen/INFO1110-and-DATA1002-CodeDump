def cone(radius, height):
    if not isinstance(radius,(int,float)) or not (height,(int,float)):
        raise TypeError('Error: Parameter radius and height must be numeric')
    if radius <= 0:
        raise ValueError("Error: Radius must be positive.")
    if height <= 0:
        raise ValueError("Error: Height must be positive.")
    V = 3.1415 * (radius ** 2) * (height/3)
    return V


print(cone("hello", 4))