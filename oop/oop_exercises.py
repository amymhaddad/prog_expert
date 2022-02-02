from curses.ascii import EM
from distutils.command.build_scripts import first_line_re
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
-Interface is like an abstract class -- BUT it only contains abstract methods. 
*There are no implementation details, except for methods. Then, it raises the NotImpelemetedError in each method
*Aim to outline/describe all methods that inerhit from the interface 
*They should not be instantiated    

"""


class RunCodeInterface:
    def compile_code(self):
        raise NotImplementedError("You must implement compile_code()")

    def execute_code(self):
        raise NotImplementedError("You must implement execute_code")

    # IF I keep this method then this class is no longer an interface bc it implements logic
    # def print_name(self):
    #     print()


# IF GoCode was inheriting from a parent class, then list the parent class first followed by the interface
class GoCode(Code, RunCodeInterface):
    pass


# GoCode must implmement ALL methods in RunCodeInterface. However, I'm free to add any other methods to this class.
class GoCode(RunCodeInterface):
    def compile_code(self):
        print("Compile Go code")

    def execute_code(self):
        print("Execute Go code")

    def print_name(self):
        print("name")


class JavaCode(RunCodeInterface):
    def compile_code(self):
        print("Compile Java code")

    def execute_code(self):
        print("exe Java code")


def run_code(code):
    code.compile_code()
    code.execute_code()


"""
-run_code() is a function that takes an object -- but I don't know what code is -- it could be Go or Java 
-BUT whatever obj is passed as the code object must have compile_code and execute_code methods 
-Don't call methods that are specific to the inheriting class in run_code (bc I don't know what obj type that will be passed in -- so I can't call print_name
bc that's specific to the inheriting class and NOT to the interface 
"""

# Declare what type should be passed in python; Taking any obj that accepts the RunCodeInterface
def run_code(code: RunCodeInterface):
    code.compile_code()
    code.execute_code()
