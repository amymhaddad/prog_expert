class Vector:
    def __init__(self, a, b):
        self.a = a 
        self.b = b 

    def __eq__(self, vector):
        return self.a == vector.a and self.b == vector.b 

    #return string obj
    def __repr__(self):
        return f"Vector({self.a}, {self.b})"

    def __add__(self, vector):
        return Vector(self.a + vector.a, self.b+vector.b)
    
    def __sub__(self, vector):
        return Vector(self.a - vector.a, self.b - vector.b)

    def __mul__(self, vector):
        #sum_vector = self.__add__(vector)


v1 = Vector(4, 5)
v2 = Vector(1, 2)
print(v1 - v2)
