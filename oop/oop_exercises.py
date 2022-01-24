from socket import AI_V4MAPPED_CFG


class Foo:
    def __init__(self, name):
        self.name = name


a = Foo("a")
b = Foo("b")
a.name = b.name
b.name = "c"
a.x = 2
b.x = 1


class ContactInformation:
    country = None

    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number


person1 = ContactInformation("Amy", "Haddad", "ex.com", 123)
person2 = ContactInformation("John", "Haddad", "ex.com", 123)


class Person:
    def __init__(self, name):
        self.name = name  # public attr: can access and modify outside of class
        self._salary = 0  # private attr: can only access and modify inside class (w/in defined constraints) w/getters and setters

    @property
    def salary(self):  # getter returns private attribute
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary < 0:
            raise ValueError("Invalid salary")
        self._salary = salary


p1 = Person("A")
p1.salary = 10010


class Person:
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.population = 1
        Person.population += 1


p1 = Person("Tim", 100)
p2 = Person("Clement", 54)

x = Person.population


class Car:
    number_of_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.number_of_cars = 1
        Car.number_of_cars += 1

    @classmethod
    def update_num_cars(cls, cars):
        cls.number_of_cars = cars


Car.number_of_cars += 3

c1 = Car("Ford", "x")
c2 = Car("Mazda", "3")
Car.update_num_cars(4)

"""
Aim of Circle is to group together related attr's and methods 
Now I can modify the class attribute, pi, which will modify the 2 methods defined below
-The methods do NOT rely on an instance of the Circle class   

-Class method/class - can't access anything related to instances 
"""


class Circle:
    pi = 3.14

    @classmethod
    def area(cls, radius):
        return cls.pi * (radius ** 2)

    @classmethod
    def perimeter(cls, radius):
        return 2 * cls.pi * radius

    @classmethod
    def get_area_and_permiter(cls, radius):
        # using methods w/in a method
        return cls.area(radius), cls.perimeter(radius)


class Student:
    bump_amt = 2.0

    def __init__(self, name, grades=[]):
        self.name = name
        self.grades = grades

    def ave(self):
        return sum(self.grades) / len(self.grades)

    @classmethod
    def ave_from_grades_plus_bump(cls, grades):
        ave = cls.ave_grades(grades)
        return min(ave + cls.bump_amt, 100)

    @staticmethod
    def ave_grades(grades):
        return sum(grades) / len(grades)


t1 = Student("Tim", [80, 65, 75, 100])
t2 = Student("C", [40, 50, 60, 76])
