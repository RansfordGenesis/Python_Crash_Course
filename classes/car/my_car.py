from car import Car

my_car = Car("New", "BMW", 2023)
print(my_car.describe_it())

my_car.update_odometer(250)
print(my_car.read_odometer())

my_car.increment_odometer(120)
print(my_car.read_odometer())