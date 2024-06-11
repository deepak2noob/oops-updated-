'''lambda function
-A lambda function is a small anonymous function defined with the keyword lambda in Python
-It can have any number of arguments, but it can only have one expression.
syntax:
lambda arguments: expression
'''
'example'
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5

'''
arguments= no of inputs function need to run . 
expression =operations of code
'''

'''types of lambda function:
1)First-Class Functions
2)Higher-Order Functions
3)Proxy Function
'''
'''first-class Functions
functions in a programming language can be passed as arguments to other functions'''

# making main function that gooing to input lambda function
def apply_func(func, value):
    return func(value)

#taking lambda function as input
result = apply_func(lambda x: x ** 2, 4)
print(result)  # Output: 16

'''Higher-Order Functions

'''