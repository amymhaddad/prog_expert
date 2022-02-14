import math


class Polygon:
    def get_area(self):
        raise NotImplementedError("You must provide an implementation for play()")

    def get_sides(self):
        raise NotImplementedError("You must provide an implementation for play()")

    #Return perimeter of polygon
    def get_perimeter(self):
        all_sides = self.get_sides()
        number_of_sides = (self.get_sides() - 2) * 180
        return all_sides[0] * number_of_sides



class Triangle(Polygon):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3 
    
    def get_sides(self):
        return [self.side1. self.side2, self.side3]

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

#implement 
class Square(Rectangle):
    def __init__(self, side):
       self.side = side 
    
    def get_sides(self):
        return Rectangle.get_sides()
    
    def get_area(self):
        return Rectangle.get_area()



# Use this function in your solution.
def get_triangle_area(side1, side2, side3):
    semi_perimeter = (side1 + side2 + side3) / 2
    return math.sqrt(
        semi_perimeter *
        (semi_perimeter - side1) *
        (semi_perimeter - side2) *
        (semi_perimeter - side3)
    )


# Use this function in your solution.
def get_rectangle_area(width, height):
    return width * height

