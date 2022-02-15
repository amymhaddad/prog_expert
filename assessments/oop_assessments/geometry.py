
import math
from turtle import pd


class Polygon:
    def get_area(self):
        raise NotImplementedError("You must provide an implementation for play()")

    def get_sides(self):
        raise NotImplementedError("You must provide an implementation for play()")

    #Return perimeter of polygon
    def get_perimeter(self):
       # import pdb; pdb.set_trace()
        all_sides = self.get_sides()
        return len(all_sides) * all_sides[0]


class Triangle(Polygon):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3 
    
    def get_sides(self):
        return [self.side1, self.side2, self.side3]

    def get_area(self):
        s = get_triangle_area(self.side1 + self.side2 + self.side3)
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area 
    

class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height 
    
    def get_sides(self):
        return [self.width, self.width, self.height, self.height]

    def get_area(self):
         return get_rectangle_area(self.width, self.height)

    def get_perimeter(self):
       # import pdb; pdb.set_trace()
       return self.height + self.height + self.width + self.width

class Square(Rectangle):
    def __init__(self, side):
       self.side = side 
    
    def get_sides(self):
       # import pdb; pdb.set_trace()
        return Rectangle.get_sides(self.side, self.side)
    
    def get_area(self):
        return self.side ** 2
    
    def get_perimeter(self):
        return 4 * self.side

def get_triangle_area(side1, side2, side3):
    semi_perimeter = (side1 + side2 + side3) / 2
    return math.sqrt(
        semi_perimeter *
        (semi_perimeter - side1) *
        (semi_perimeter - side2) *
        (semi_perimeter - side3)
    )


def get_rectangle_area(width, height):
    return width * height

# triangle = Triangle(1, 1, 1)
# print(triangle.get_perimeter()) #3
# rect = Rectangle(2, 3)
# print(rect.get_perimeter())
# square = Square(3)
# print(square.get_perimeter())

# triangle = Triangle(1, 5, 6)
# print(sorted(triangle.get_sides()))
square = Square(3)

print(sorted(square.get_sides()))