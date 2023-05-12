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
        
class Battery:
    def __init__(self, battery=40):
        self.battery = battery
        
    def describe_battery(self):
        print(f"The battery life is {self.battery}.")
        
class ElectricCar(Car):
    
    def __init__(self, model, name, year):
        super().__init__(model, name, year)
        self.battery = Battery()
        
        

future_car = ElectricCar('New', 'BMW', 2023)
print(future_car.describe_it())
future_car.battery.describe_battery()