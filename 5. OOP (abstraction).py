'''defination:
Abstraction in Python, like in many programming languages, refers to the concept
of hiding complex implementation details and exposing only the necessary 
functionalities or interfaces to the users.
'''

#abstraction in python is achieved though module 
from abc import ABC, abstractmethod

#----------------------------------------------------------------
#abstract class

from abc import ABC, abstractmethod
class Abstractclass(ABC):      
    pass
"when parameter has 'ABC' written then it is abstract class."


'''properties of abstract class:
1)It's main purpose is to serve as a blueprint for other classes.
2)It's designed to be subclassed . so most of the time , it is present in parent classes only.
3)we cant make object of abstract class as python doesnot allow us .
4)ABC class is known as Meta class as this class defines the behaviour of other classes
5)abstract class can have both abstract method and concrete method
'''
#example
class Shape(ABC):  # Shape is an abstract class
    @abstractmethod
    def area(self):  # This is an abstract method
        pass

    def print_info(self):  # This is a concrete method
        print("This is a shape.")

#-----------------------------------------------------------------
'''types of method in abstraction:
1)abstract method
2)concrete method
'''

'''abstract method:
1)method present in abstract class and its action is not defined on abstract class .
Its actually defined on its subclass or childclass(defined in inherited classes)
2)we have to write @abstractmethod decorator for abstract method.
'''
#example
class Shape(ABC):  # Shape is an abstract class
    @abstractmethod
    def area(self):  # This is an abstract method
        pass


'''Concrete method
1)it is a method which is also defined inside abstract class .
Unlike abstract method , this method contains actions inside it .
2)no need to write any decorator for this method . eg:
'''
from abc import ABC , abstractmethod

class Father(ABC):
  @abstractmethod
  def disp(self):  #abstract method / method without body
    pass
  def show(self ): #concrete method / method with body
    pass
#------------------------------------------------------------------------------------
'''Rules for Abstract class and its methods:
1)python cannot create object of an abstract class .

2)it is not necessary to declare all methods abstract in abstract class. 
some can be concrete method also.

3)Abstract class can have both abstract method and concrete methods.

4)if there is any abstract method in class , then class must be abstract class.

5)the abstract method of abstract class must be defined in its child class.

6)if you are inheriting any abstract class that have abstract method , you either
have to define its abstract methods or make this class also abstract class

'''

#--------------------------------------------------------------------------------------
#proof that you cant make object of abstract class(parent class)
from abc import ABC , abstractmethod

class Father(ABC):
  @abstractmethod
  def disp(self): #abstract method
    pass
  def show(self): #concrete method
    print("hi bruh")

#object
object = Father()     #Output : Type error
"""it is not possible to make object for abstract class"""


#try to make object of child class of abstract class
from abc import ABC , abstractmethod
class Father(ABC):  #abstract class
  @abstractmethod
  def disp(self): #abstract method
    pass
  def show(self): #concrete method
    print("hi bruh")

class Child(Father):
  def disp(self):
    print("child class")
    print("defining abstract method")
#object
object = Child()
object.disp() # calling abstract method
object.show() #calling concrete method


#--------------------------------------------------------------------------------------
'''example of abstraction 
                             ___________________
                            |  Defence Force   |
                            | Gun = AK 47      |
                            | Area =           |
                            | _________________|
                                      |
          ____________________________|__________________________                                                    
 _________|__________       __________|_________         ________|_________
|       Army        |      |     Air Force     |        |       Navy       |
| Gun = AK 47      |       | Gun = AK 47       |        | Gun = AK 47      |
| Area = Land      |       | Area = Sky        |        | Area = Sea       |
|___________________|      |___________________|        |__________________|



-here Defence force is abstract class .

-here , we gave value to Gun but not to Area because Gun of this class is concrete method 
(as it's value will be going to be same in all its subclasses) and Area is Abstract method 
(as every subclassses will have its different value)because its value will be putted later.

-this shows us why and when to use abstract class .

\\Note
abstract class never have its owwn object because it is always made to be inherited by other 
classes .

'''
#lets make code of this example
from abc import ABC, abstractmethod

class DefenceForce(ABC): #abstract class or blueprint for other classes
  @abstractmethod
  def Area(self):
    pass
  def Gun(self):
    print("AK 47")

class Army(DefenceForce): #child class 1
  def Area(self):
    print("Land")

class AirForce(DefenceForce): # child class 2
  def Area(self):
    print("sky")

class Navy(DefenceForce): # child class 3
  def Area(self):
    print("Sea")

#creating objects

a=Army()
ar=AirForce()
n=Navy()

#calling child class values

a.Gun()
a.Area()
print()

ar.Gun()
ar.Area()