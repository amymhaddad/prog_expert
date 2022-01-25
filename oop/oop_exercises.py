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


"""
-Use inheritance to inherit functionality from another class
-Have funciotionalty that's common among classes stored in a single place 
-Have related classes re-use functionality 

-Polymorphism - many forms

"""
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name 
        self.last_name = last_name

    def say_hello(self):
        print(f"Hi, my name is {self.first_name}")
    
"""
-Now I want to create an Employee class. I want all Employees to have the same functionality as my Person class
Bc every Employee is a person
So use inheritance

-The Employee class has access to everythign in Person (ie, it's super class)
-BUT the super class can't access what's inside of the subclass

-Override methods inside base class 
"""
#The Employee class inherits from the Person class 
#Employee is now known as: child, subclass, or derived class 
#Person (the class I inherit from) is known as: super, base, or parent class 
class Employee(Person):
    #Overriding method in parent class 
    def say_hello(self):
        print("------")
        #super() gives me access to the parent class 
        super().say_hello() #pass self to the super/parent class 
        print("------")

"""
-How to override constructor to include other attributes 
-Repeat constructor along w/any other attributes to init the Employee
"""
class Employee(Person):
    def __init__(self, first_name, last_name, salary):
        #super() invisiably passes "self" for me to the super class. Then, I provide the attributes from the paraent class 
        super().__init__(first_name, last_name)
        #manually create my own 
        self.salary = salary


"""
Multiple inheritances
"""
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name 
        self.last_name = last_name

    def say_hello(self):
        print(f"Hi, my name is {self.first_name}")

class Employee(Person):
    #Overriding method in parent class 
    def say_hello(self):
        print("------")
        #super() gives me access to the parent class 
        super().say_hello() #pass self to the super/parent class 
        print("------")

#Any instance of Manager is an Employee and a Person 
#Employee is the base/super class. So I inherit functionality from this class 
class Manager(Employee):
    #Override Employee class constructor
    def __init__(self, first_name, last_name, salary, department):
        super().__init__(first_name, salary, last_name)
        self.department = department


m = Manager("a", "b", 100, "sport")
m.say_hello() #This will use the method defined in Employee bc Manager inherits from Employee 


"""
Multi inheritance - another ex
"""
#Owner is not an employee, but it is a Person
class Owner(Person):
    def __init__(self, first_name, last_name, net_worth):
        super().__init__(first_name, last_name)
        self.networth = net_worth

o = Owner("T", "Programmer", 50000)
#type(o) -- the type of an instance of "o" is Owner, BUT it's also of type Person
#Verify this: print(isinstnace(o, Person)) --> is "o" of type Person
"""
-If I call say_hello() on instance of Owner, which method runs?
>>>
The method inside Person runs -- Person is the base/super/parent class 

-is a rule - if Owner inherits from Person, Owner IS A Person 
-->How to determine if need to use inheritance  

"""


"""
Multi inheritance - another ex
"""
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name 
        self.last_name = last_name

    def say_hello(self):
        print(f"Hi, my name is {self.first_name}")

class Employee(Person):
    def say_hello(self):
        print("------")
        super().say_hello() #pass self to the super/parent class 
        print("------")

class Manager(Employee):
    #Override Employee class constructor
    def __init__(self, first_name, last_name, salary, department):
        super().__init__(first_name, salary, last_name)
        self.department = department

class Owner(Person):
    def __init__(self, first_name, last_name, net_worth):
        super().__init__(first_name, last_name)
        self.networth = net_worth

"""
m = Manager("A", "B", 40000, "cs")
Is a Manager also a Person?
print(isinstance(m, Person))
>>>
True
-Bc a Manager is an Employee, and an Employee is a Person 


p = Person("T", "B")
Is a Person an Owner
print(isintance(p, Owner))
>>>
False
-Inheritance is only one direction. Owner(Person) means Owner inherits from Person BUT it does not mean that Person inherits from Owner 

"""


"""
Multi inheritances - ex
"""

class A:
    def __init__(self):
        print("A")

class B: 
     def __init__(self):
        print("B")


#classes A and B are BOTH parent classes to class C; class C is the subclass/child/derived class 
class C(A, B):
    pass 

#What prints out:
c = C() 
print(c)

"""
A
-Whatever is defined first is where Python looks for methods first

Workflow:
-Create instance of class C, so Python checks if there's an init method in C. There's not
-So Python goes through the parent classes (A, B) IN the order they're defined looking for the init method 
-Since class A has the init method, we use the method that's there. BUT if class A didn't have the init method, we'd run the init method in class B
**Key point: the init that is found first is run 

"""


"""
Multi inheritances - ex
"""

class A:
    def __init__(self):
        print("A")

class B: 
     def __init__(self):
        print("B")

#classes A and B are BOTH parent classes to class C; class C is the subclass/child/derived class 
class C(A, B):
    super().__init__()

#What prints out:
c = C() 
print(c)
"""
A

-super() will reference class A. BUT if class A didn't have a the init method, it'd use class B.
-super() references all super classes -- all of the classes we inherit from. We just start w/ the one that we define first 

MRO - method resolution order 
*Start by looking at main class
*If NOT in main class, look at first super class 
*If NOT in first super class, look at next super class 

-For this multi inheritance to work, class C is an A and class C is a B (the "is a" rule needs to apply )

"""


"""
Inheritance ex 
Duck typing 
"""
class Duck:
    def swim(self):
        print("Swimming duck")
    
    def fly(self):
        print("Flying duck")

class Whale:
    def swim(self):
        print("Swimming whale")

animals = [Duck(), Duck(), Whale()]

for animal in animals:
    animal.swim()
    animal.fly()

"""
In Python, the code above runs until I get an error when try to execute animal.fly() on instance of Whale9) 
-Python tries to run the method anyway -- it doesn't check if a method exists on an object in advance 
"""



"""
-child, derived, subclass are syn for a class that inherits from another class 
-parent, base, superclass are syn for a class for a class that's inherited from 
"""


#Ex1
class A:
    pass

class B:
    pass

class C(A, B):
    pass

class D(C):
    pass

a = C()

"""
What class us "a" an instance of (ie, if I call isinstance(a, X) where X is a class name)

>>>
A, B, C
-a is an instance of C which inherits from both classes A and B 
"""

#Ex 2 
class A:
    pass

class B:
    pass

class C(A, B):
    pass

class D(C):
    pass

a = D()

"""
What class us "a" an instance of (ie, if I call isinstance(a, X) where X is a class name)

>>>
A, B, C, D
-a is an instance of D which inherits from class C which inherits from both classes A and B 
"""

#Ex 3
class A:
    def foo(self):
        print('A')

class B:
    def foo(self):
        print('B')

class C(A, B):
    def foo(self):
        print('C')

class D(C):
    pass

a = D()
#what is printed when a.foo() is called?
#>>>

#"C'"