class Car:
    def __init__(self, make, model):
        self._make = make  # Protected variable
        self._model = model  # Protected variable

    def _drive(self):  # Protected method
        print(f"Driving the {self._make} {self._model}")

my_car = Car("Toyota", "Corolla")
print(my_car._make)  # Output: Toyota
my_car._drive()  # Output: Driving the Toyota Corolla