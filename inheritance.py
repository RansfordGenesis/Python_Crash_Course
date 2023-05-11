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
        
class ElectricCar(Car):
    
    def __init__(self, model, name, year):
        super().__init__(model, name, year)
        self.battery = 40
        
    def describe_battery(self):
        return f"The battery life is {self.battery}."

future_car = ElectricCar('New', 'BMW', 2023)
print(future_car.describe_it())
print(future_car.describe_battery())