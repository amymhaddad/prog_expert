import math

# Use this function in your solution.
def get_triangle_area(side1, side2, side3):
    semi_perimeter = (side1 + side2 + side3) / 2
    return math.sqrt(
        semi_perimeter
        * (semi_perimeter - side1)
        * (semi_perimeter - side2)
        * (semi_perimeter - side3)
    )


# Use this function in your solution.
def get_rectangle_area(width, height):
    return width * height


class Polygon:
    def get_area(self):
        raise NotImplementedError("get_area() method must be implemented")

    def get_sides(self):
        raise NotImplementedError("get_sides() method must be implemented")

    def get_perimeter(self):
        return round(sum(self.get_sides()))


class Triangle(Polygon):
    def __init__(self, s1, s2, s3):
        self.sides = [s1, s2, s3]

    def get_sides(self):
        return self.sides

    def get_area(self):
        s1, s2, s3 = self.sides
        return get_triangle_area(s1, s2, s3)


class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_sides(self):
        return [self.width, self.width, self.height, self.height]

    def get_area(self):
        return get_rectangle_area(self.width, self.height)


class Square(Rectangle):
    def __init__(
        self, side_length
    ):  # side_length is the attr I want to inherit from Rectangle class
        super().__init__(
            side_length, side_length
        )  # super references Rectange; pass side_length 2x for width and height
