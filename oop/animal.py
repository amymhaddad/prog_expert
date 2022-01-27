class Animal:
    def __init__(self, age, weight, height):
        self.age = age
        self.weight = weight
        self.height = height


class Mammal(Animal):
    def __init__(self, age, weight, height, sex):
        super().__init__(age, weight, height)
        self.sex = sex 
     

class Reptile(Animal):
    def __init__(self, age, weight, height):
        super().__init__(age, weight, height)
        self.legs = None 

class Monkey(Mammal):
    fingers = 5

    def __init__(self, age, weight, height, sex, color):
        super().__init__(age, weight, height, sex)
        self.color = color 
       
        

class Lizard(Reptile):
    tail = True
    def __init__(self, age, weight, height, color):
        super().__init__(age, weight, height)
        self.color = color 
       
        
lizard = Lizard(10, 50, 1.5, 0, "red")
print(lizard.tail)

# class Manager(Employee):
#     #Override Employee class constructor
#     def __init__(self, first_name, last_name, salary, department):
#         super().__init__(first_name, salary, last_name)
#         self.department = department

# class Owner(Person):
#     def __init__(self, first_name, last_name, net_worth):
#         super().__init__(first_name, last_name)
#         self.networth = net_worth
