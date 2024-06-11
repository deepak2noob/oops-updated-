class Myclass:
    hi=1 #class variable                                            #creating class
    def __init__(self,name,Class): #instance method
        self.name=name #instance variable         
        self.Class=Class #instance variable
        print(name,Class)
        


obj=Myclass("deepak","bruh")   #creating object , instance
#----------------------------------------------------------------------------------

#calling class directly using class 
print(Myclass("hello", "bye")) #ave to fill all parameters otherwise it will show error
'''
    output: deepak bruh
            hello bye

it printed hello bye later because it is written later
in constructor            
'''
#----------------------------------------------------------------------------------

#calling class directly using object
'''
In Python, you can't directly call an object. 
there are some special  methods that help u to call obj directly but
its not in syllabus

example:

print(obj) # will tell u address of object
print(obj())#will call Myclass class which is not callable 
'''
#----------------------------------------------------------------------------------

#calling class constructor , instance method variables

#using class
'''
#print(Myclass.name , Myclass.Class) ---> error

'''

#using object
print(obj.name , obj.Class)  #output : deepak bruh
'''
You cannot directly access instance variables using the class name
This will raise an AttributeError
print(MyClass.instance_variable) -->errror
'''
#----------------------------------------------------------------------------------
#Note:
'''
 Methods like .__init__() and .__str__() are called dunder methods because they begin and end with double underscores. 
'''



