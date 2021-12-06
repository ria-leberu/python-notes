# method is anything you are calling on an object itself
# function is something that takes an object, and applies an operation to it

# Four principles of OOP

# Encapsulation

# Abstraction

# Inheritance

# Polymorphism

# self is an instance of the object

# main benefit of a class is that you can create multiple objects of the same class

# classes have methods (like functions) and attibutes (like variables to hold data)
# init will create the object with the attributes declared or initialized
# attributes may be added without putting them in init


class Character():

    # static variables
    party = []

    def __init__(self, name, strength, dexterity, intelligence, role):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.role = role
        # appends created object to a static variable list
        self.party.append(self.name)

    def get_stats(self):
        print(
            f"[Stats: STR {self.strength} | VIT {self.dexterity} | INT {self.intelligence}]")

    def speak(self):
        print(
            f"Hello, my name is {self.name}, I am a {self.role} and a civilian.")


class Tank(Character):

    def __init__(self, name, strength, dexterity, intelligence, role, job):
        super().__init__(name, strength, dexterity, intelligence, role)
        self.job = job

    def speak(self):  # function overrides the original function of the parent class
        print(
            f"Hello, my name is {self.name}, I am a {self.role} and a {self.job}.")


# jim = Character('Jim', 10, 10, 10, 'Shopkeeper')
# tim = Tank('Tim', 15, 12, 8, 'Fighter', 'Tank')

# jim.get_stats()

# jim.speak()
# jim.get_stats()
# tim.speak()
# tim.get_stats()

# print(Character.party)  # can be called with object name or class name

# overriding builtin methods


class Point():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return self.x * p.x + self.y * p.y

    def __str__(self):  # whenever we try to print the object, python tries to find __str__ method
        return f"({self.x}, {self.y})"


# p1 = Point(3, 4)
# p2 = Point(3, 2)
# p3 = Point(1, 3)
# p4 = Point(0, 1)

# p5 = p1 + p2
# p6 = p4 - p1
# p7 = p2 * p3

# print(p5, p6, p7)

# @classmethod  # this is a decorator, classmethod can be called on the name of the class

class Dog:
    dogs = []

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod  # static methods, only pass the parameters we want, no need for self or class
    def bark(n):
        for _ in range(n):
            print("Bark!")


# tim = Dog("tim")
# print(tim.num_dogs())

# Dog.bark(5)

# static methods are useful for adding functions that work out of the box without instantiating an object

# in python a private method may be denoted with an underscore at the front of the name
