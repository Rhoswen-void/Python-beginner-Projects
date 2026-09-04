pi = 3.14159

def area_of_circle(radius):
    return pi * radius ** 2

def circumference(radius):
    return 2 * pi * radius

def area_of_rectangle(length,width):
    return length * width

def area_of_triangle(base,height):
    return 0.5 * base * height

def area_of_square(side):
    return side ** 2

def area_of_trapezoid(base1,base2,height):
    return 0.5 * (base1 + base2) * height

def volume_of_cylinder(radius,height):
    return pi * radius ** 2 * height

def volume_of_sphere(radius):
    return (4/3) * pi * (radius ** 3)

def volume_of_cone(radius,height):
    return (1/3) * pi * (radius ** 2) * height  

def volume_of_cube(side):
    return side ** 3

def volume_of_cuboid(length,width,height):
    return length * width * height
