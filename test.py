class MyClass:
    def __init__(self, value):
        self.value = value
        print("Constructor called with value:", value)
        a=1

# Creating an instance of MyClass
obj = MyClass(10)

print(MyClass.a)