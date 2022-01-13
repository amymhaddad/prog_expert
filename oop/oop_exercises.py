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
print(person1.country)


class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Hayden")
p2 = Person("Jim")
print(p1.name)