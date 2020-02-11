def cone(radius, height):
    # Write your function code here!
    if (isinstance(radius,(int,float)) == True and isinstance(height,(int,float))) == True:   
        if radius <= 0:
            raise ValueError("Error: radius must be positive.")
        elif height <= 0:
            raise ValueError("Error: height must be positive.")
        else:
            V = 3.1415*(radius**2)*(height/3)
        return V
    else:
        raise TypeError("Error: parameters radius and height must be numeric.")
