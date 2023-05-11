class Car:
    """Initialize attributes to describe a car."""
    def __init__(self, model, name, year):
        self.model = model
        self.name = name
        self.year = year
    
    def describe_it(self):
        return f"My Future Car is {self.year} {self.name} {self.model}."
    
    def update_odometer(self, mileage):
        self.odometer = mileage
        
    def read_odometer(self):
        return f"Odometer reading is: {self.odometer}"
    
    def increment_odometer(self, miles):
        self.odometer += miles
        
future_car = Car("New", "BMW", "2023")
print(future_car.describe_it())

future_car.update_odometer(250)
print(future_car.read_odometer())

future_car.increment_odometer(120)
print(future_car.read_odometer())
