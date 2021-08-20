# Day 5 Coding
# Object Orientated Programming (OOP)

'''def hello():
    print(hello)

# The function is a class, which is part of an object
# print(type(hello))'''

'''string = "hello"

# .upper() is a method acting on an object
print(string.upper())'''

class Dog:
    def __init__(self, name, age):
        # This is an attribute
        self.name = name
        self.age = age
        # Since this is in the __init__ method, it will be accessed anytime the object is created.
        #print(name)

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    # Method
    def bark(self):
        print("bark!")

d = Dog("Stella", 6)
# Showing that 'stella' is an instance of the class
# print(type(stella))

'''d.bark()
print(d.get_name())
print(d.get_age())

d.set_age(4)
print(d.get_age())'''

##################
##################
##################

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_avg_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

'''s1 = Student("Stella", 23, 80)
s2 = Student("Chris", 20, 74)
s3 = Student("Jane", 18, 93)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

print(course.get_avg_grade())'''

##################
##################
##################
'''
CLASS INHERITANCE
'''

# Parent class
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def speak(self):
        print("...")

# Inheriting the pet class
class Cat(Pet):
    def __init__(self, name, age, color):
        # super(). = references the parent class
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("meow!")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old, I am a {self.color}.")

# Inheriting the pet class
class Dog(Pet):
    def speak(self):
        print("bark!")

'''p = Pet("Jane", 4)
p.show()
p.speak()

c = Cat("Leah", 10, "tabby")
c.show()
c.speak()

d = Dog("Stella", 6)
d.show()
d.speak()'''

##################
##################
##################
'''
CLASS METHODS
'''

class Person:
    # Variable is not affected unless called within function
    # Variable local to this class
    number_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    # Acts on the class, not referencing self
    @classmethod
    def number_of_people(cls):
        return cls.number_people

    @classmethod
    def add_person(cls):
        cls.number_people += 1

'''p1 = Person("Stella")
print(Person.number_people)

p2 = Person("Amy")
print(Person.number_people)'''

##################
##################
##################
'''
STATIC METHODS
'''

class Math:
    # Not based on class or self
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def pr():
        print("run")

print(Math.add5(6))

Math.pr()