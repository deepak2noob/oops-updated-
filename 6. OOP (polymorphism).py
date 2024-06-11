'''defination:
Polymorphism in Python refers to the ability of different objects to
respond to the same method or function call in different ways.
'''
'''types of polymorphism in python:
1)Method Overriding
2)Duck typing
3)operator overloading
'''
#--------------------------------------------------------------------------------------
'''method overriding:
This occurs when a subclass provides a specific method 
that is already defined in its superclass. this results overriding the 
superclass's method .
'''
#example
class Animal:
    def sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Woof!")

class Cat(Animal):
    def sound(self):
        print("Meow!")
#here Cat and Dog overrides sound method from its parent class.
#--------------------------------------------------------------------------------------
'''Duck typing:
This occurs when an object's suitability is determined by the presence 
of certain methods or properties rather than objects type.
'''
#example
class Duck:
    def sound(self):
        print("Quack!")

class Car:
    def sound(self):
        print("Vroom!")

def make_sound(entity):
    entity.sound()

# Polymorphic behavior
make_sound(Duck())
make_sound(Car())

'''here we made make_sound() function which requires parameter..
and if we put parameter as class , then it will give us class.sound() .
In conclusion ,  we called object/class method without using object
'''

#--------------------------------------------------------------------------------------
'''difference between method overloading and method overriding:
'''

'''method overloading:
1)Defination:
Method overloading refers to the ability to define multiple methods 
with the same name but with different parameters within the same class.

2)purpose:
It allows a class to have multiple methods with the same name but 
different behavior based on the number.

3)it is performed within a class.

4)it is not built in present in python . we have to do some ammendments
to make it work.

5)it is performed within one class

'''
#example:
class MathOperations:
    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b


math = MathOperations()
print(math.add(2, 3))       # Output: 5
print(math.add(2, 3, 4))    # Output: 9

'''here we can call this class method with different parameters.
'''

'''method overriding.
1)Definition: Method overriding refers to the ability of a subclass 
to provide a specific modifications of a method that is already defined in its superclass.

2)Purpose: It allows a subclass to provide its own modification of a method, 
thereby extending or modifying the behavior defined in the superclass.

3)it is performed within a Parent class and child class.

4)it is built in method in python.

5)it is performed more than 1 class
'''

class Animal:
    def sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Woof!")

#--------------------------------------------------------------------------------------
'''operator overloading
- Operator overloading in Python refers to the ability 
to define custom behavior for built-in operators (+, -, *, /, etc.) 
for objects of user-defined classes.

- it will allow to make same operator in different meaning

-Python provides special methods (also known as dunder methods) 
that can be defined in a class to implement operator overloading'''
#example
a,b=1,2
print(a.__add__(b)) #3

#implementation in oops
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Define addition behavior
        return Point(self.x + other.x, self.y + other.y)


# Usage
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # This will call __add__ as  p1.__add__(p2)
print(p3)     # Output: (4, 6)

#--------------------------------------------------------------------------------------