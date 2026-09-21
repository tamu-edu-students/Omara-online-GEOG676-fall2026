class Shape():
    def __init__(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def area(self):
        return self.width * self.length

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

file = open(r'C:\Users\liamo\Downloads\shape.txt', 'r')
lines = file.readlines()
file.close()

for line in lines:
    components = line.split(',')
    shape = components[0]

    if shape == 'Rectangle':
        rect = Rectangle(int(components[1]), int(components[2]))
        print('Area of Rectangle: ', rect.area())
    elif shape == 'Circle':
        circ = Circle(int(components[1]))
        print('Area of Circle: ', circ.area())
    elif shape == 'Triangle':
        tri = Triangle(int(components[1]), int(components[2]))
        print('Area of Triangle: ', tri.area())
    else:
        pass