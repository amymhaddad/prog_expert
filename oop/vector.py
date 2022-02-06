class Vector:
    def __init__(self, a, b):
        self.a = a 
        self.b = b 

    def __eq__(self, vector):
        return self.a == vector.a and self.b == vector.b 

v1 = Vector(1, 2)
v2 =  Vector(1, 2)
print(v1 == v2)



