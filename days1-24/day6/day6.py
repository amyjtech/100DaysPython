# OOP with Python
# Tech with Tim


class Dog(object):
    def __init__(self, name, age):
        #This is an attribute
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

'''wiggles = Cat('Wiggles', 5, 'Tabby')
wiggles.speak()

stella = Dog('Stella', 6)
stella.speak()'''

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

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return (self.x * p.x) + (self.y *p.y)

p1 = Point(3,4)
p2 = Point(3,2)
p3 = Point(1,3)
p4 = Point(0,1)

# Addition
p5 = p1 + p2

# Subtraction
p6 = p4 - p1

# Multiplication
p7 = p5 * p6

print(f"{p5}, {p6}, {p7}")