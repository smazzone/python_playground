class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        print("initializing a car...")

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Fill gas tanks."""
        print("filling gas tank...")


#from classes_car import Car as Car

#When you create a child class, the parent class 
# must be part of the current file and must appear 
# before the child class in the file

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles. It extends a Car."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        print("initializing a new electric car...")
        self.battery_size = 75

    def describe_battery_size(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    #overriding a method in the base class
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank! It's an Electric Car!")

my_tesla = ElectricCar('tesla','model X',2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery_size()
my_tesla.fill_gas_tank()




