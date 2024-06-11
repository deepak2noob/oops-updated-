'''COnstructor
1)The constructor method "__init__()" is automatically called when an instance of a class is created.
2)It initializes the object's attributes and performs any necessary setup.
3)always present at 1st of class
4)very commonly used
'''
#example
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        print(f"A new car object of make {make} and model {model} has been created.")

my_car = Car("Toyota", "Corolla")
# Output: A new car object of make Toyota and model Corolla has been created.

#--------------------------------------------------------------------------------------------------------
'''Destructor:
1)The destructor method "__del__()" is called when an object is about to be destroyed.
2)It is not commonly used in Python because Python has automatic garbage collection. 
3)However, it can be useful for performing cleanup operations before an object is destroyed, 
such as closing file handles or releasing other resources.
4)very rarely used

'''
#example

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def __del__(self):
        print(f"The {self.make} {self.model} object is being destroyed.")

my_car = Car("Toyota", "Corolla")
del my_car
# Output: The Toyota Corolla object is being destroyed.

#------------------------------------------------------------------------------------------------------
'''super() method:
in python ,the super() function is used to call methods and constructors from the parent class within a subclass.

This is particularly useful when you want to extend the functionality of the parent class in the child class 
while still maintaining the behavior of the parent class.
'''
#example
class Parent:
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print("Name:", self.name)

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Calling the constructor of the Parent class
        self.age = age
    
    def display(self):
        super().display()  # Calling the display method of the Parent class
        print("Age:", self.age)

# Creating an object of the Child class
child_obj = Child("Alice", 25)
child_obj.display()

'''
if super() not used in child class, then childs constructor overrides the constructor values of
its parent class. thus you will not able to get parents self. name in child class.
super() helps you to extend the child constructor info.
'''
#---------------------------------------------------------------------------------------

'''types of super()
1)with parameter: only take parameterized values
2)without parameter: inherit  all inside method/constructor.'''

''''''
