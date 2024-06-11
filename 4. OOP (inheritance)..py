'''
Defination:

1)Inheritance is the capability of one class to inherit the properties from another class.
The class that inherit properties is called the child class and the class from which
the properties are being derived is called the base class or parent class.

2)The subclass(child) can override methods of the superclass to provide its own implementation
 or extend the functionality of the superclass(parent) methods.

'''

#inheritance example

#1
class Parent:
    hair_color = "brown"

class Child(Parent):
    pass

obj=Child()
print(obj.hair_color) # brown

#-----------------------------------------------------------------------------------------------
#you can even overidde the class if you want  using inheritance

class Parent:
    hair_color = "brown"

class Child(Parent):
    hair_color = "purple"

obj1=Parent()
obj2=Child()

print(obj.hair_color)#brown
print(obj2.hair_color)#purple

#-----------------------------------------------------------------------------------------------

#you can even extend the class if you want using inheritance


class Parent:
    hair_color = "brown"

class Child(Parent):
    hair_type = "long"

obj=Child()
print(obj.hair_color,obj.hair_type) #brown long


#-----------------------------------------------------------------------------------------------
'''types of inheritance:
1)single inheritance
2)multiple inheritance
3)multi level inheritance
3)Hierarchical Inheritance
4)hybrid inheritance
'''
#----------------------------------------------------------------------------------------------
'''Single Inheritance:
In single inheritance, a subclass inherits from only one superclass.
example:

class A:
    pass

class B(A):
    pass
'''

'''multiple inheritance:
Multiple inheritance allows a subclass to inherit attributes and methods from more than
one superclass.Each subclass can add its own additional attributes and methods.
This can lead to complex inheritance hierarchies and potential issues like the 
diamond problem
example:

class A:
    pass

class B:
    pass

class C(A, B):
    pass

'''

'''multi level inheritance:
In multilevel inheritance, a subclass inherits from a superclass,
and then another subclass inherits from the first subclass, forming a chain of inheritance.
Each subclass can add its own additional attributes and methods

example:

class A:
    pass

class B:
    pass

class C(A, B):
    pass
    
'''

'''Hierarchical inheritance:
In hierarchical inheritance, multiple subclasses inherit from a single superclass.
Each subclass can add its own additional attributes and methods

example:

class A:
    pass

class B(A):
    pass

class C(A):
    pass


'''

'''hybrid inheritance:
Hybrid inheritance is a combination of multiple types of inheritance. 
It can involve multiple inheritance, multilevel inheritance, 
and hierarchical inheritance within the same class hierarchy

example:

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

'''

#----------------------------------------------------------------------------------------------------

'''Diamond Problem:
it arises when  a class inherits from two or more classes that have a common ancestor.

    A
   / \
  B   C
   \ /
    D

    In this example:

Class A is the superclass.
Classes B and C both inherit from A.
Class D inherits from both B and C, creating a diamond-shaped inheritance hierarchy.

The diamond problem occurs when a  method or attribute defined in class A is overridden
in both classes B and C, and class D inherits from both B and C

In Python, the diamond problem is mitigated by using method resolution order (MRO)
to determine the order in which methods are inherited and invoked. 
'''