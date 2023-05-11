class Car:
    """ A class to implement cars"""
    def __init__(self, model, name, year):
        self.model = model
        self.name = name
        self.year = year
    
    def describe_it(self):
        return f"My Future Car is {self.year} {self.name} {self.model}."

future_car = Car("New", "BMW", "2023")
print(future_car.describe_it())
