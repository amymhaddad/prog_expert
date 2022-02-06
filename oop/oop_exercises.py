from curses.ascii import EM
from dis import dis
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
# class GoCode(Code, RunCodeInterface):
#     pass


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

############### dunder methods
#Ex: __add__
class Page:
    def __init__(self, words, page_number):
        self.words = words 
        self.page_number = page_number

    #self -- curr obj (left operand); other (right operande)
    #This method must return a new object 
    #Now, I can add pages -- just like I can add ints, floats, strings. SO I overloaded the addition operation on the page method 
    def __add__(self, other):
        new_words = self.words + other.words
        new_page_number = max(self.page_number, other.page_number) + 1 #create new page number 
        return Page(new_words, new_page_number)
    
page1 = Page("page 1", 1)
page2 = Page("page 2", 2)
#NOW I want to add these pages together 
#ie: page1 + page2 --> page3 (ie, I want to take everything from page and and page 2 and add this info together)
#This will give me an error: page3 = page1 + page2 -- I need to tell python how to do this 
page3 = page1 + page2 
print(page3.words)


#Ex: __sub__ and __mul__
class StoreItem:
    TAX = 0.13

    def __init__(self, name, price):
        self.name = name 
        self.price = price 
        self.after_tax_price = 0 #Create after_tax_price as default that's handled in a method
        self.set_after_price_tax() #call method here so that the above method gets set right away 

    def set_after_price_tax(self):
        self.after_tax_price = round(self.price * (1 + self.TAX), 2)

    def __sub__(self, discount):
        return StoreItem(self.name, self.price - discount)
    
    def __mul__(self, discount):    
        return StoreItem(self.name, self.price * discount)


bread = StoreItem("Bread", 7)
#Ex for using __sub__ to subtract a value from an object and create a nwe object
#Now I want to be able t subtract a discount amount from this bread and get a new store item back that represents the discounted price
# discounted_bread = bread - 2
# print(discounted_bread.after_tax_price)

#Ex for using __mul__ to multiple a value from an object and create a nwe object
discounted_bread = bread * 0.8
print(discounted_bread.after_tax_price)


#Ex: __truediv__ --> / (reg divison)
#    __floordiv__ --> // (integer division)
# __len__ 


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def __truediv__(self, factor):
        new_point1 = (self.point1[0] / factor, self.point1[1] / factor)
        new_point2 = (self.point2[0] / factor, self.point2[1] / factor)
        return Line(new_point1, new_point2)

    def __floordiv__(self, factor):
        new_point1 = (self.point1[0] // factor, self.point1[1] // factor)
        new_point2 = (self.point2[0] // factor, self.point2[1] // factor)
        return Line(new_point1, new_point2)

    #__len__ must return an integer
    def __len__(self):
        pass 

line1 = Line((10, 5), (20, 10))

#print(line1.point1, line1.point2) #(10, 5) (20, 10)
#Note: using one / so I call the __truediv__ method
line2 = line1 / 2
print(line2.point1, line2.point2)

#Note: using one // so I call the __floordiv__ method
line3 = line1 // 2
print(line3.point1, line3.point2)

import math 

#Ex: Check for equality - comparison operations (== and !=)
class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def __len__(self):
        dist_x = (self.point1[0] - self.point2[0]) ** 2
        dist_y = (self.point1[1] - self.point2[1]) ** 2
        dist = math.sqrt(dist_x + dist_y)
        return round(dist)
    
    #Check for equality == 
    def __eq__(self, other):
        #see if the objects are the same -- is "other" a line? So I need to check if other is a Line. If I don't have this check, then I will get an error if I create an invalid value for a line (ie, line = 3)
        if not isinstance(other, Line):
            return False
        return self.point1 == other.point1 and self.point2 == other.point2
           
    #Check if not equal != 
    def __ne__(self, other):
        #The == will trigger __eq__ to run OR I can manually call it 
        #Here, I take the negation of what ever this self.__eq__(other) is 
        return not self.__eq__(other)
    
    #Compare the lens of the lines -- greater than
    def __gt__(self, other):
        #return self.__len__() > other.__len__()
        return len(self) > len(other)

    #greater than or eq to
    def __ge__(self, other):
         return len(self) >= len(other)

    #Other comparison: __lt__ (less than) AND __le__ (less than or eq to)

line1 = Line((10, 5), (20, 10))
line2 = Line((10, 5), (20, 10))
print(line1 == line2) #False b/c the comparison -- w/o the __eq__ checks to see if these objects are the same, and they're not. line1 nad line2 are separate objects -- just w/the same values.
#BUT this gives me the result I want:
line1 = Line((10, 5), (20, 10))
line2 = line1
print(line1 == line2) #True bc line1 and line2 are the same object
#So in this case, I want to use the __eq__ method bc I'm really checking for the value (ie, do both lines have the same value) and NOT if the lines are the same object 
#So I want line1 and line2 to return True bc they have the same values 

print(line1 == line2) #true bc I've included the dunder method 

print(line1 >= line2)


"""New ex: __str__"""
class Page:
    def __init__(self, text, page_number):
        self.text = text 
        self.page_number = page_number
    
    #Get the length of the text on a page
    def __len__(self):
        return len(self.text)
    
    #Use to rep a human readable representation of our object 
    def __str__(self):
        #return self.text 
        #The above return works, but typically this is what you see: (all of the params -- all of the details of the Page)
        return f"Page(text = {self.text}, page_number =  {self.page_number})"
    
    #Use __repr__ to represent the internal rep of an object; to use when debugging
    def __repr__(self):
        #return the same info as in the __str__ : return f"Page(text = {self.text}, page_number =  {self.page_number})"
        return self.__str__()


class Book:
    def __init__(self, title, author, pages, id_number):
        self.title = title 
        self.author = author
        self.pages = pages 
        self.id_number = id_number
    
    def __len__(self):
        return len(self.pages)
    
    def __str__(self):
        output = f"Book({self.title}, {self.author}, {self.id_number})"

        for page in self.pages:
            #when I get the str(page), I call the def __str__(self) method of the Page class
            output += "\n" + str(page)
        return output

    #Use repr to debug and display useful info about the object
    def __repr__(self):
        return f"Book(id_number: {self.id_number})"
    

page1 = Page("Page 1", 1)
page2 = Page("Page 2", 2)
book = Book("HW", "AMH", [page1, page2], 1)
#WHen I try to print an object: print(page1), I get object itself and its memory address
#The reason I get this output is bc behind the scenes I call teh string function on the object 
#BUT I can override this internal representation using: __str__ and this method needs to return some string
#print("Here", book)
#This is the result:
#  Book(HW, AMH, 1)
# Page(text = Page 1, page_number =  1)
# Page(text = Page 2, page_number =  2)

#To print the repr of an obj, I need to specify
#print(repr(book))

"""
Calling print() on an instance of a class will cause the __str__ method to be called. 
This is bc print() calls str() on all args before printing them 

"""

