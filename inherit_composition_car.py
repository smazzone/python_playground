from classes_car import Car
from battery_composition import Battery as Battery
from random import randint

# When you create a child class, the parent class 
# must be either part of the current file and must appear 
# before the child class in the file
# or you can import it from another module


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles. It extends a Car."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        print("initializing a new electric car...")
        self.battery = Battery()

    def describe_battery_size(self):
        """Print a statement describing the battery size."""
        self.battery.describe_battery()

    def get_battery_range(self):
        self.battery.get_range()

    #overriding a method in the base class
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank! It's an Electric Car!")

my_tesla = ElectricCar('tesla','model X',randint(2015,2021))
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery_size()
my_tesla.fill_gas_tank()
my_tesla.get_battery_range()



