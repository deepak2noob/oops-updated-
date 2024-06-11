'''Defination
It's a way to restrict access to some parts of an object and to expose 
only the necessary parts to the outside world.
This is achieved by using access modifiers such as private, 
protected, and public.
'''
'''types of modifiers:
1)private
2)protected
3)public
'''
#--------------------------------------------------------------------------------
'''Private access modifiers: 
1)In private access modifier, the data members and member 
functions of a class are accessible only within the class. 

2)Other classes cannot access them directly. 

3)In Python, private members are conventionally indicated 
using a double underscore __ prefix.
'''
#example
class Car:
    def __init__(self, make, model):
        self.__make = make   #private variable
        self.__model = model #private variable

    def drive(self):
        print(f"Driving the {self.__make} {self.__model}")

    def __drive(Self):#private method
        pass

my_car = Car("Toyota", "Corolla")

# print(my_car.__make)  error
#print(my_car.drive())     error
'''
this would raise an AttributeError because __ makes is private.


'''
my_car.drive()  # Output: Driving the Toyota Corolla
'''
called private variables using public method present within class'''
'''
here you cant call __make and __model variables directly because of __.
you need another method inside same class to call these variables.
like here you used my_car.drive() to call both private variables'''
#------------------------------------------------------------------------------
'''Protected access modifier: 
In protected access modifier, the data members and member functions of a class are 
accessible only within the class and its subclasses (derived classes). 
In Python, it is indicated using a single underscore _ prefix 
for attributes and methods.
'''
class Car:
    def __init__(self, make, model):
        self._make = make  # Protected variable
        self._model = model  # Protected variable

    def _drive(self):  # Protected method
        print(f"Driving the {self._make} {self._model}")

my_car = Car("Toyota", "Corolla")
print(my_car._make)  # Output: Toyota
my_car._drive()  # Output: Driving the Toyota Corolla
'''
here you can call both variable and method within class
'''
#-----------------------------------------------------------------------------
'''Public access modifier:
In public access modifier, all data members and member functions 
of a class are accessible from outside the class. 
This is the default behavior in many programming languages, including Python. 
You can access attributes and methods directly from outside the class.
'''
class Car:
    def __init__(self, make, model):
        self.make = make #public variable
        self.model = model

    def drive(self): # public method
        print(f"Driving the {self.make} {self.model}")

my_car = Car("Toyota", "Corolla")
print(my_car.make)  # Output: Toyota
my_car.drive()  # Output: Driving the Toyota Corolla

#----------------------------------------------------------------------------
