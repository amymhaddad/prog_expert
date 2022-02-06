from turtle import pd


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, vector):
        return self.a == vector.a and self.b == vector.b

    # return string obj
    def __repr__(self):
        return f"Vector({self.a}, {self.b})"

    def __add__(self, vector):
        return Vector(self.a + vector.a, self.b + vector.b)

    def __sub__(self, vector):
        return Vector(self.a - vector.a, self.b - vector.b)

    def __mul__(self, vector):
        curr_vector = (self.a * vector.a) + (self.b * vector.b)
        return curr_vector
