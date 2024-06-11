#creating method of class
class MyClass: #constructor
    def __init__(self, value):
        self.value = value

    def display_value(self): #method
        print("Value:", self.value)

# Creating an instane ,c object of MyClass
obj = MyClass(10)

#-------------------------------------------------------------------------

# Calling the method using instance
obj.display_value()

#calling the method using class
'''
calling method using class is actually little bit
complex . so , it is better not to know it. (for now)
'''
#-------------------------------------------------------------------------

'''types of method:
1)abstract method
2)concrete method
3)class method

1st and 2nd explained in OOP (abstraction)

3)@classmethod

'''

