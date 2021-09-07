# OOP with Python
# Tech with Tim


class Dog(object):
    def __init__(self, name, age):
        # This is an attribute
        self.name = name
        self.age = age

    # This is a method
    def speak(self):
        print(f"My name is {self.name}, and I am {self.age} years old.")


# (Dog) is the parent of Cat
class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print(f"My name is {self.name}, and I am {self.color} cat.")


'''
wiggles = Cat('Wiggles', 5, 'Tabby')
wiggles.speak()

stella = Dog('Stella', 6)
stella.speak()
'''

##################
##################
##################


class Vehicle():
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color

    def fillTank(self):
        self.gas = 100

    def emptyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas


class Car(Vehicle):
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.speed = speed

    def horn(self):
        print('Beep! Beep!')


class Truck(Vehicle):
    def __init__(self, price, gas, color, tires):
        super().__init__(price, gas, color)
        self.tires = tires

    def horn(self):
        print('Honk! Honk!')

# This inherits from the Vehicle and Car classes
# Vehicle > Car > Motorcycle


class Motorcycle(Car):
    def __init__(self, price, gas, color, speed, cc):
        super().__init__(price, gas, color, speed)
        self. cc = cc


##################
##################
##################

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    # addition
    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    # subtract
    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    # multiply
    def __mul__(self, p):
        return (self.x * p.x) + (self.y * p.y)

    # Math for gt, lt, and equals
    def length(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)

    # greater than
    def __gt__(self, p):
        return self.length() > p.length()

    # greater then/equal
    def __ge__(self, p):
        return self.length() >= p.length()

    # less than
    def __lt__(self, p):
        return self.length() < p.length()

    # less then/equal
    def __le__(self, p):
        return self.length() <= p.length()

    # equals
    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

    # converts to str
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"


p1 = Point(3, 4)
p2 = Point(3, 2)
p3 = Point(1, 3)
p4 = Point(0, 1)

# Addition
p5 = p1 + p2

# Subtraction
p6 = p4 - p1

# Multiplication
p7 = p5 * p6

'''
print(f"{p5}, {p6}, {p7}")

print(p1 == p2)
print(p1 > p3)
print(p4 <= p6)
'''
