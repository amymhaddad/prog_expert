import math


class ShapeInterface:
    def get_area(self):
        raise NotImplementedError()

    def get_perimeter(self):
        raise NotImplementedError()


class Square(ShapeInterface):
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return self.side_length * self.side_length

    def get_perimeter(self):
        return self.side_length * 4


class Circle(ShapeInterface):
    pi = math.pi

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return Circle.pi * (self.radius ** 2)

    def get_perimeter(self):
        return 2 * Circle.pi * self.radius
