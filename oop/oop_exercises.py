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
        self.name = name #public attr: can access and modify outside of class
        self._salary = 0  #private attr: can only access and modify inside class (w/in defined constraints) w/getters and setters

    @property
    def salary(self): #getter returns private attribute
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

Car.number_of_cars += 3

c1 = Car("Ford", "x")
c2 = Car("Mazda", "3")
print(c1.number_of_cars)
print(c2.number_of_cars)