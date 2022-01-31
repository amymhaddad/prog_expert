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
abstract class - a class w/no instances; meant to act as a parent/base/super class to other classes 
-Aim to increase abstraction in program and contain common implementation details common to other classes
-Can implement methods and abstract methods
*abstract methods - a method that's not implemented by the class but is req'd to be implemented by any class that inherits from it 
*Can't enforce abstract classes in Python

-Denote an abstract class by calling it as such: 
class AbstractGame
*Inside class create behavior that's specific to a game 
*Make as general as possible

-An abstract method is any method that needs to be implemented that inherits from this AbstractGame clas

"""


class AbstractGame:

    # Make this a class or static method (ie, don't pass self) bc this method doesn't access attributes on instances of this class
    # static method - works like a regular function -- not specific to an instance

    # Here, I need to use self bc I need to access the self -- the instance -- in order to access another methdo
    def start(self):
        while True:
            start = input("Would you like to start?")
            if start.lower() == "yes":
                break
        self.play()

    def end(self):
        print("The game is ended")
        self.reset()

    # If I call this method and it hasn't been implemented, then I get an erro
    # By implemented: a child/derived class inherits AbstractGame and imp,emetn this method
    # Anythign that inherits this AbstractGame class needs to override this method and provide an implementation
    def play(self):
        raise NotImplementedError("You must provide an implementation for play()")

    def reset(self):
        raise NotImplementedError("You must provide an implementation for reset()")


"""
-This class by itself won't work. I need to have a class that inherits AbstractGame and implement the methods 

-Abstract classes give framework for how game will be start/end BUT it tells whoever inherits from it that it must have a play() and reset() method; how these are defined is general (abstract)
*Leave the concrete implementation to the child class 

-play() and reset() give us a framework for each game; both are specific to each gaem 
-BUT the way the game starts and end is always the same (via AbstractGame). So a class that inherits AbstarctGame already gets start and end 
*start and end will use play() and reset() but the inheriting class must use these methods otherwise an exception will be raised 

"""

"""
Ex

"""


class AbstractGame:
    def start(self):
        # Get asked if want to play game
        while True:
            start = input("Would you like to start?")
            if start.lower() == "yes":
                break

        # Then it runs the play method, which is in this case is the play() method from RandomGuesser
        self.play()

    def end(self):
        print("The game is ended")
        self.reset()

    def play(self):
        raise NotImplementedError("You must provide an implementation for play()")

    def reset(self):
        raise NotImplementedError("You must provide an implementation for reset()")


import random

# class RandomGuesser() inherits from AbstractGame; can do what I want w/this class -- but it must have play() and reset()
class RandomGuesser(AbstractGame):
    def __init__(self, rounds):
        # start at 0 and go until self.rounds
        self.rounds = rounds
        self.round = 0

    # reset the game by taking a new number of rounds
    def reset(self):
        self.round = 0

    def play(self):
        while self.round < self.rounds:
            self.round += 1
            print(f"Welcome to round {self.round}")

            random_num = random.randint(10)
            while True:
                guess = input("Enter a number between 1 and 10: ")
                if int(guess) == random_num:
                    print("You got it!")
                    break
            # Once game has ended call self.end(), which in turn resets the game
            self.end()


class AnotherGame(AbstractGame):
    pass


r2 = AnotherGame()
r2.start()


r = RandomGuesser(2)
r.start()
"""
-Abstract class -- I never instantiate it
*An abstract class is designed to act as the base class in an inheritcance hierarchy and is NOT designed to be instantiated. 
*They usually contain abstract methods that are meant to be implementend (via overriding) by classes that inherit from them
*Some abstract classes contain concrete methods (ie, start()) AND abstract methods that are implemented (via overriding) from child class that inherits from it
*Aim of an abstract class: to funciton as a base class that provides already impelmented behavior that can be extended by any subclass 
*There's concrete implementation: there's code that does something (ie, start())
*Define all other methods that the inheriting class will need to implement
(ie, play() and reset(), which are the abstract methods. IF these methods are used without being defined in the inheriting class, then an error will occur) 
-RandomGuesser is a concrete class that overrides the abstract methods in the parent class: play() and reset() 

r = RandomGuesser(2)
r.start()
-->I call start() on the "r" instance of RandomGuesser, which calls the play() method 

-Any game that inherits from AbstractGame begins the same way: instance_name.start() THEN the specific implementionat defined in the inheriting class will impelement the game detials for that specific game 

This will throw an error:
class AnotherGame(AbstractGame):
    pass 

r2 = AnotherGame()
r2.start()

Bc I haven't defined play() or reset() so the play() method gets run from AbstractGame, which raises an erorr (bc the inheriting class doesn't override the play() method of the parent class )
vs 
In RandomGuesser(AbstractGame) uses the play() method defined inside of its class

"""

"""Study"""


class Animal:
    def sleep(self):
        print("ZzzZzz")

    def animal_sound(self):
        raise NotImplementedError("Method not implemented")

    def wake_up(self):
        self.animal_sound()
        print("I am awake!")


class Lion(Animal):
    def animal_sound(self):
        print("Roar!")


l = Lion()
l.sleep()
l.wake_up()
