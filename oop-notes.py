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


class Vehicle():

    def __init__(self, name, color):  # constructor method
        self.name = name
        self.color = color
        print(f"You've created a new vehicle: {self.name}")
        pass

    def set_color(self, color):
        self.color = color
        pass

    def get_color(self):
        return print(f"The color of the {self.name} is {self.color}.")


# inherits from the vehicle class
class Boat(Vehicle):
    def __init__(self, name, color, weight):
        super().__init__(name, color)
        self.color = color


honda = Vehicle('Honda', 'Red')
chevrolet = Vehicle('Chevrolet', 'Blue')

yamaha = Boat('Yamaha', 'White', 600)

chevrolet.get_color()
honda.get_color()

yamaha.get_color()
